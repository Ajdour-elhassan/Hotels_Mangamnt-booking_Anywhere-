from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .models import Listing , Realtors 


def home(request) :
    lists = Listing.objects.order_by('-list_date').filter(published=True)[:3]
    return render(request , 'home.html' , {'lists':lists})


def listings(request) :
    lists =  Listing.objects.order_by('-list_date').filter(published=True)
    #Paginator
    paginator = Paginator(lists, 3) 
    page = request.GET.get('page')
    listing_paged = paginator.get_page(page)
    return render(request, 'listings.html' , {'listing_paged': listing_paged})


def list(request, list_id):
    #listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listing.html')


def about(request) : 
    realtors = Realtors.objects.order_by('-hire_date')
    
    #Get Mvp
    mvp_realtor = Realtors.objects.all().filter(id_mvp=True)
    
    context = {'realtors' : realtors , 'mvp_realtor' : mvp_realtor }
    
    return render(request, 'about.html' , context)
    
def dashboard(request) :
    return render(request , 'dashboard.html')

def search(request) :
    return render(request , 'listings/search.html')
