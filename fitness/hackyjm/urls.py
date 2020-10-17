from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('profile/', views.profilePage, name='profile'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]