from django.shortcuts import render
from .models import productdetails, auctiondetails, auction_history, user
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Max

def index(request):
    products=productdetails.objects.all()
    return render(request,"index.html",{"products":products, "Username":request.session['userName']})

def login(request):
    if(request.method=="POST"):
        userName=request.POST['userName']
        password=request.POST['password']
        if(user.objects.all().filter(username=userName,  password=password).exists()):
            request.session['userName']=userName
            request.session['phoneno']=user.objects.get(username=userName).phone_no
            request.session['email']=user.objects.get(username=userName).email
            return HttpResponseRedirect('/index')
        messages.success(request, 'Invalid credentials')
    return render(request,"login.html")    

def destinations(request):
    if(request.method=="POST"):
        prodId=request.POST['ProdId']
        name=request.session['userName']
        phoneno=request.session['phoneno']
        email=request.session['email']
        amt=request.POST['bidamnt']
        ins=auction_history(username=name, phone_no=phoneno, email=email, auction_value=amt,product_id=prodId) 
        ins.save()   
    auctionProduct = auctiondetails.objects.get(product_id=int(request.GET['prodId']))
    auctionHistory = auction_history.objects.filter(product_id=int(request.GET['prodId']))
    product = productdetails.objects.get(product_id=int(request.GET['prodId']))
    max_bid = auction_history.objects.filter(product_id=int(request.GET['prodId'])).aggregate(maxbid=Max('auction_value'))['maxbid']
    try:
        highestBid=auction_history.objects.get(product_id=int(request.GET['prodId']), auction_value=max_bid)
    except auction_history.DoesNotExist:
        highestBid = None
    return render(request,"destinations.html", {"selectedProduct":product, "auctionedProduct": auctionProduct, "auctionHistory":auctionHistory, "highestBid":highestBid}) 

def register(request):
    if(request.method=="POST"):
        userName=request.POST['userName']
        password=request.POST['password']
        first_name=request.POST['FirstName']
        last_name=request.POST['LastName']
        phone_no=request.POST['PhoneNumber']
        email=request.POST['Email']
        if(user.objects.all().filter(username=userName).exists()):
            messages.success(request, 'Username already exists')
            return HttpResponseRedirect('/register') 
        ins=user(username=userName, password=password, first_name=first_name, last_name=last_name, phone_no=phone_no, email=email) 
        ins.save()
        return HttpResponseRedirect('/') 
    return render(request,"register.html") 

def search(request):
    products=productdetails.objects.all().filter(name__icontains=request.GET['prodName'], 
                                                desc__icontains=request.GET['manufacturerName'])
    filteredProducts = []
    for product in products:
        if(request.GET['searchPrice'] == "" or product.price <= int(request.GET['searchPrice'])):
            filteredProducts.append(product)
    return render(request,"search.html",{"products":filteredProducts})   
 