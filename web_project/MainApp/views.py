from django.shortcuts import render , get_object_or_404 , redirect
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib import messages
from .models import Listing , Realtors , Contact
from .search_choices import  bedroom_choice , price_choice , city_choice 
from django.core.mail import send_mail


def home(request) :
    lists = Listing.objects.order_by('-list_date').filter(published=True)[:3]
    
    context = {'lists':lists , 
              'bedroom_choice' : bedroom_choice , 
              'price_choice' : price_choice , 
              'city_choice' : city_choice 
              }
    
    return render(request , 'home.html' , context )  



def listings(request) :
    lists =  Listing.objects.order_by('-list_date').filter(published=True)
    #Paginator
    paginator = Paginator(lists, 3) 
    page = request.GET.get('page')
    listing_paged = paginator.get_page(page)
    return render(request, 'listings.html' , {'listing_paged': listing_paged})


def listing_details(request, listing_id):
   listing = get_object_or_404(Listing , pk=listing_id)
    
   return render(request, 'listing.html' , {'listing' : listing})


def search(request) :
    
    query_list = Listing.objects.order_by('-list_date')
    
    #Keyword
    if "keywords" in request.GET :
        keywords = request.GET["keywords"]
        if keywords :
            query_list = query_list.filter(description__icontains=keywords) #keywords inside description field
    
    #City 
    if "city" in request.GET :
        city = request.GET["city"]
        if city :
            query_list = query_list.filter(city__iexact=city) #city exactly in cities
    
    #State
    if "state" in request.GET :
        state = request.GET["state"]
        if city :
           query_list = query_list.filter(state__iexact=state) #city exactly in State
    
    #Badroom
    if "bedroom" in request.GET :
        bedroom = request.GET["bedroom"]
        if city :
           query_list = query_list.filter(bedroom__lte=bedroom) # lte = less than 
    
    #Price
    if "price" in request.GET :
        price = request.GET["price"]
        if price :
            query_list = query_list.filter(price__lte=price)  # lte = less than 
            

    context = {
              'bedroom_choice' : bedroom_choice , 
              'price_choice' : price_choice , 
              'city_choice' : city_choice ,
              'lists' : query_list ,
              'values' : request.GET
              }
    
    return render(request , 'search.html' , context )



def about(request) : 
    realtors = Realtors.objects.order_by('-hire_date')
    
    #Get Mvp
    mvp_realtor = Realtors.objects.all().filter(id_mvp=True)
    
    context = {'realtors' : realtors , 
               'mvp_realtor' : mvp_realtor 
               }
    
    return render(request, 'about.html' , context)


# CONTACT FORM
def contact(request) :
    if request.method == "POST" :
        listing = request.POST["listing"]
        listing_id = request.POST["listing_id"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]
        
        #  Check if user has already  make an inquiry!
        if request.user.is_authenticated :
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted :
                messages.error(request, 'YoU have already make an inquiry!')
                return redirect('home')
        
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
        phone=phone, message=message, user_id=user_id)
        
    
        contact.save()
        
        # Send Email
        send_mail(
            "Property listing Inquiry",
            "Your have made an Inquiry successfully, for" + listing + "Sign into your acccount and make payment",
            'ajdourelhassa2096@gmail.com',   
            [realtor_email, 'diesemartfirma2096@gmail.com'],
            fail_silently=False
        )
        
        
        messages.success(request, "Your Request has been Submitted successfully!")
        return redirect('home')