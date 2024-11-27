from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('',views.LoginPageView.as_view(), name='login'),
    path('', views.HomePageView.as_view(), name='home'),

]
