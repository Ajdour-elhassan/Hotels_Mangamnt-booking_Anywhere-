from django.contrib import admin
from .models import Realtors , Listing , Contact


class ListingAdmin(admin.ModelAdmin) :
  list_display = ('id','title', 'price', 'list_date', 'published', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('published',)
  search_fields = ('title', 'description', 'city', 'address', 'state', 'zipcode', 'price')
  list_per_page = 25
  
admin.site.register(Listing, ListingAdmin)  

class RealtorAdmin(admin.ModelAdmin) :
  list_display = ('id','name', 'phone', 'email', 'id_mvp' , 'hire_date')
  list_display_links = ('id', 'name')
  list_filter = ('name',)
  search_fields = ('name',)
  list_per_page = 25
  
admin.site.register(Realtors, RealtorAdmin)


class ContactAdmin(admin.ModelAdmin) :
  list_display = ('id','name','listing','email','contact_date')
  lits_display_link = ('id','name')
  search_field = ('name', 'email','listing')
  listing_per_page = 25
  
  
admin.site.register(Contact, ContactAdmin)
    


