from django.db import models
import datetime
# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    email=models.CharField(max_length=30)
class productdetails(models.Model):
    product_id=models.IntegerField()
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='pics')
    desc=models.CharField(max_length=100)
    price=models.IntegerField()
class auctiondetails(models.Model):
    product_id=models.IntegerField()
    product_specifications=models.TextField()
    current_bid=models.IntegerField()
    closing_time=models.DateTimeField()
class auction_history(models.Model):
    product_id=models.IntegerField()
    username=models.CharField(max_length=30)
    auction_value=models.IntegerField()
    phone_no=models.IntegerField(default=0)
    email=models.CharField(max_length=30,default="")
    date=models.DateField(default=datetime.datetime.now)
