from django.shortcuts import render

def index(request):
    return render(request, "clothing_store/index.html")

def product_list(request):
    return render(request, "clothing_store/product_list.html")

def login_view(request):
    return render(request, "clothing_store/login.html")

def about_view(request):
    return render(request, "clothing_store/about.html")  # ตรวจสอบว่ามีไฟล์ about.html
