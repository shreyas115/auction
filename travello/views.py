from django.shortcuts import render
from .models import productdetails, auctiondetails, auction_history, user
from django.http import HttpResponseRedirect
from django.contrib import messages

def index(request):
    products=productdetails.objects.all()
    return render(request,"index.html",{"products":products})
def login(request):
    if(request.method=="POST"):
        userName=request.POST['userName']
        password=request.POST['password']
        print(userName)
        print(password)
        if(user.objects.all().filter(username=userName,  password=password).exists()):
            return HttpResponseRedirect('/index')
        messages.success(request, 'Invalid credentials')
    return render(request,"login.html")    
def destinations(request):
    if(request.method=="POST"):
        prodId=request.POST['ProdId']
        name=request.POST['bidname']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        amt=request.POST['bidamnt']
        ins=auction_history(username=name, phone_no=phoneno, email=email, auction_value=amt,product_id=prodId) 
        ins.save()   
    auctionProduct = auctiondetails.objects.get(product_id=int(request.GET['prodId']))
    auctionHistory = auction_history.objects.filter(product_id=int(request.GET['prodId']))
    product = productdetails.objects.get(product_id=int(request.GET['prodId']))
    return render(request,"destinations.html", {"selectedProduct":product, "auctionedProduct": auctionProduct, "auctionHistory":auctionHistory}) 
def news(request):
    return render(request,"news.html")
def elements(request):
    return render(request,"elements.html")   
def search(request):
    products=productdetails.objects.all().filter(name__icontains=request.GET['prodName'], 
                                                desc__icontains=request.GET['manufacturerName'])
    filteredProducts = []
    for product in products:
        if(request.GET['searchPrice'] == "" or product.price <= int(request.GET['searchPrice'])):
            filteredProducts.append(product)
    return render(request,"search.html",{"products":filteredProducts})   
 