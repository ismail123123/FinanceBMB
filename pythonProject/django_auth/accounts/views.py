from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from django import forms
from django.shortcuts import render, HttpResponseRedirect
from . models import Portfolio
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Portfolio
import yfinance as yf
from django.shortcuts import get_list_or_404
from .models import Company
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
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
       ticker = yf.Ticker(company_name)
       current_price = ticker.history(period="1d")["Close"].iloc[-1]
       setattr(portfolio, 'current_price', current_price)

   context = {

      "portfolios": portfolios,
      "form" : form,

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

def search(Listview):

    model = Company
    template_name = 'search_result.html'
queryset = City.objects.filter(name__icontains='Boston') # new