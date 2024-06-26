from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("portfolio/", TemplateView.as_view(template_name="portfolio.html")),
    path("search_company/", TemplateView.as_view(template_name="search_company.html")),
    path("chatbot/", TemplateView.as_view(template_name="chatbot.html")),

]


