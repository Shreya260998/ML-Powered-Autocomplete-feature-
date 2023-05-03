from django.contrib import admin
from django.urls import path
from ..project import views
urlpatterns = [   
  path('', views.SignupPage, name="signup"),
  path('signup', views.login, name="login"),
  path('login', views.home, name="home")      
]