from django.contrib import admin
from .models import productdetails, auctiondetails, auction_history

# Register your models here.

admin.site.register(productdetails)
admin.site.register(auctiondetails)
admin.site.register(auction_history)