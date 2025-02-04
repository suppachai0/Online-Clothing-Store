from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # ดึงข้อมูลสินค้าทั้งหมด
    return render(request, 'clothing_store/product_list.html', {'products': products})

def index(request):
    return render(request, 'clothing_store/index.html')
# Create your views here.
