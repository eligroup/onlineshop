from django.urls import path
from . import views

urlpatterns = [
    path("about_us/", views.AboutUsPageView.as_view(), name="about_us"),
    path("", views.HomePageView.as_view(), name="home"),

]
