from django.urls import path

from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path('delete_data/', views.delete_data, name='delete_data'),
]
