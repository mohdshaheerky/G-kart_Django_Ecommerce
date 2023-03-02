from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    product=Product.objects.all().filter(is_available=True)
    context={
        'products':product
    }
    return render(request,'home.html',context)
