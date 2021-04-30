from django.urls import path
from . import views



urlpatterns = [
    path('creat_an_account/' , views.register , name='register'),
    path('login' , views.login , name='login'),
    path('logout' , views.logoutView , name='logout'),
    path('dashboard' , views.dashboard , name='dashboard'),
]  


