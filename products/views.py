from django.shortcuts import render
from .models import prod
# Create your views here.
def products(request):
    d= prod.objects.all().count()
    data= prod.objects.all()
    return render(request,'products/products.html',{'f':data , 'd':d})

def product(request):
    return render(request,'products/product.html')