from django.db import models
from datetime import datetime 

class Realtors (models.Model):
  name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to="Realtors_photo")
  description = models.TextField()
  phone = models.IntegerField()
  email = models.EmailField(max_length=50)
  id_mvp = models.BooleanField(default=False)
  hired_date = models.DateTimeField(default=datetime.now , blank=True) 
  
  def __str__(self) :
    return self.name


class Listing(models.Model) :
  realtor = models.ForeignKey(Realtors , on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=300)
  address = models.CharField(max_length=300)
  city = models.CharField(max_length=300)
  state = models.CharField(max_length=300)
  zipcode = models.CharField(max_length=300)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedroom = models.IntegerField()
  bedrooms = models.DecimalField(max_digits=2 , decimal_places=1)
  gerage = models.IntegerField(default=0)
  saft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5 , decimal_places=1)
  main_photo = models.ImageField(upload_to='listing_photo')
  photo_1 = models.ImageField(upload_to='listing_photo' , blank=True)
  photo_2 = models.ImageField(upload_to='listing_photo' , blank=True)
  photo_3 = models.ImageField(upload_to='listing_photo' , blank=True)
  photo_4 = models.ImageField(upload_to='listing_photo' , blank=True)
  photo_4 = models.ImageField(upload_to='listing_photo' , blank=True)
  published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now , blank=True)

  def __str__(self) :
    return self.title
  
