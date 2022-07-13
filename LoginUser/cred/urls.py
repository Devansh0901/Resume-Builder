from django.contrib import admin
from django.urls import path,include
from cred import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout')
]