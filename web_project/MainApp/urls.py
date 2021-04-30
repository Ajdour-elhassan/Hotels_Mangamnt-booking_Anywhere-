from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('lists', views.listings , name="listings"),
    path('listing_details/<int:listing_id>' , views.listing_details, name="listing_details"),
    path('search' , views.search, name='search'),
    path('about' , views.about , name='about'),
    path('contact', views.contact, name='contact')
] 



