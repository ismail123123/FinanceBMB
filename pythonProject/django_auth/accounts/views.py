# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import JsonResponse
from .models import UserChart
from django.views.generic import CreateView


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def update_chart(request):
    if request.method == 'POST':
        label1 = request.POST.get('label1')
        label2 = request.POST.get('label2')
        label3 = request.POST.get('label3')
        value1 = request.POST.get('value1')
        value2 = request.POST.get('value2')
        value3 = request.POST.get('value3')

        user_chart = UserChart(user=request.user, label1=label1, label2=label2, label3=label3, value1=value1,
                               value2=value2, value3=value3)
        user_chart.save()

        return JsonResponse({'message': 'Chart updated successfully'})

    return render(request, 'update_chart.html')
