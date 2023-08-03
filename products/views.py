from django.shortcuts import render
from .models import prod
# Create your views here.
def products(request):
    return render(request,'products/products.html',{'f':prod.objects.all()})

def product(request):
    return render(request,'products/product.html')