from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from django import forms
from django.shortcuts import render, HttpResponseRedirect
from yfinance import Ticker

from .models import Portfolio
from .forms import ProductForm
from .forms import CompanySearchForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Portfolio
from .models import Compagny
import yfinance as yf
from django.shortcuts import get_list_or_404

import numpy as np
import requests


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


def send_password_reset_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:

            error_message = "Cette adresse e-mail n'est pas enregistrée dans notre système."
            return render(request, 'password_reset_form.html', {'error_message': error_message})


        token = get_random_string(length=32)


        user.profile.reset_password_token = token
        user.profile.save()
        subject = 'Réinitialisation de mot de passe'
        html_message = render_to_string('motdepasse_reinitialisé_message.html', {'context': 'values'})
        plain_message = strip_tags(html_message)
        from_email = 'votre@email.com'
        to_email = 'destinataire@email.com'

        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)


        return render(request, 'password_reset_done.html')
class SignUpView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def portfolio(request):
    portfolios = Portfolio.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user

            form.save()

            return redirect('portfolio')
    else:
        form = ProductForm()

    for portfolio in portfolios:

        company_name = portfolio.company_name

        try:
            ticker = yf.Ticker(company_name)
            current_price = ticker.history(period="1d")["Close"].iloc[-1]
            setattr(portfolio, 'current_price', current_price)

            info = ticker.info
            company_type = info.get('quoteType', 'Type inconnu')
            setattr(portfolio, 'company_type', company_type)


        except:
            setattr(portfolio, 'current_price', "Données non disponibles")
            setattr(portfolio, 'company_type', "Type inconnu")
    context = {

        "portfolios": portfolios,
        "form": form,

    }
    return render(request, 'portfolio.html', context)


def delete_data(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        value = request.POST.get('value')

        portfolios = get_list_or_404(Portfolio, company_name=company_name, value=value)
        for portfolio in portfolios:
            portfolio.delete()

        return redirect('portfolio')


def search_company(request):
    if request.method == 'POST':
        form = CompanySearchForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            company = Ticker(company_name)
            history = company.history(period='1y')
            chart_type = request.POST.get('chart-type', 'price')
            df = yf.download(company_name, start='2019-11-01')
            df['EMA12'] = df.Close.ewm(span=12).mean()
            df['EMA26'] = df.Close.ewm(span=26).mean()
            df['MACD'] = df.EMA12 - df.EMA26
            df['signal'] = df.MACD.ewm(span=9).mean()

            macd_data = []
            Buy, Sell = [], []
            for i in range(2, len(df)):
                if df.MACD.iloc[i] > df.signal.iloc[i] and df.MACD.iloc[i - 1] < df.signal.iloc[i - 1]:
                    Buy.append(i)
                elif df.MACD.iloc[i] < df.signal.iloc[i] and df.MACD.iloc[i - 1] > df.signal.iloc[i - 1]:
                    Sell.append(i)

            for index, row in df.iterrows():
                macd_data.append({
                    'Date': index.strftime('%Y-%m-%d'),
                    'MACD': row['MACD'],
                    'signal': row['signal']
                })

            # algorithme 2

            ma = 14
            comp_close = history['Close']
            history['returns'] = np.log(comp_close).diff()
            history['ma'] = comp_close.rolling(ma).mean()
            history['ratio'] = comp_close / history['ma']
            percentiles = [5, 95]
            ratio=history['ratio']
            p = np.percentile(ratio.dropna(), percentiles)


            context = {
                'company': company,
                'history': history,
                'macd_data': macd_data,
                'p': p[0],
                'p1':p[1],
                'Buy': Buy,
                'Sell': Sell,
                'chart_type' : chart_type
            }
            return render(request, 'search_result.html', context)
    else:
        form = CompanySearchForm()
        company = "Company not found"
        return render(request, 'search_company.html', {'company': company, 'form': form})

from django.shortcuts import render
def choix(request):
  return  render(request,'choix.html')