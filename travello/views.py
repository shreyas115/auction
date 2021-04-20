from django.shortcuts import render
from .models import productdetails
# Create your views here.
def index(request):
    products=productdetails.objects.all()
    return render(request,"index.html",{"products":products})
def contact(request):
    return render(request,"contact.html")    
def destinations(request):
    return render(request,"destinations.html")
def news(request):
    return render(request,"news.html")
def elements(request):
    return render(request,"elements.html")    