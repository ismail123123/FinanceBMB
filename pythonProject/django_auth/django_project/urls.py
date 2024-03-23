from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView



urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("accounts.urls"), name="home"),
    path("portfolio/", include('accounts.urls')),
    path("search_company/", include('accounts.urls')),

]