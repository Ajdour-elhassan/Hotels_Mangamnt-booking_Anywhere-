from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('' , views.home , name='home'),
    path('about' , views.about , name='about'),
    path('dashboard' , views.dashboard , name='dashboard'),
    path('lists', views.listings , name="listings"),
    path('listings/<int:list_id>' , views.list , name="list"),
    
]  + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    