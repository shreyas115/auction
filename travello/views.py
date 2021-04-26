from django.shortcuts import render
from .models import productdetails, auctiondetails
# Create your views here.
def index(request):
    products=productdetails.objects.all()
    return render(request,"index.html",{"products":products})
def contact(request):
    return render(request,"contact.html")    
def destinations(request):
    #products=productdetails.objects.all()
    auctionProduct = auctiondetails.objects.get(product_id=int(request.GET['prodId']))
    product = productdetails.objects.get(product_id=int(request.GET['prodId']))
    print('auctioned product', auctionProduct)
    return render(request,"destinations.html", {"selectedProduct":product, "auctionedProduct": auctionProduct})
   
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
 