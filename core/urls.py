from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.HomePageView.as_view(), name='home'),
    path('burro', views.BurroPageView.as_view(), name='burro'),

]