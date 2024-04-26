from django.urls import path

from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path('delete_data/', views.delete_data, name='delete_data'),
    path('search_company/', views.search_company, name="search_company"),
    path('choix/', views.choix, name="choix"),
]
