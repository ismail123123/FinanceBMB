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
import json
import pandas as pd
import pandas_datareader as data
import requests


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


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
        except:
            setattr(portfolio, 'current_price', "Données non disponibles")
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
            data = []
            company_name = form.cleaned_data['company_name']

            company = Ticker(company_name)
            history = company.history(period='1y')

            context = {
                'company': company,

                'history': history
            }
        return render(request, 'search_result.html', context)
    else:

        form = CompanySearchForm()
        company = "Company not found"
    return render(request, 'search_company.html', {'company': company, 'form': form})
