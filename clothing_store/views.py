from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, "clothing_store/index.html")

def product_list(request):
    return render(request, "clothing_store/product_list.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    return render(request, "clothing_store/login.html")

def register_view(request):
    return render(request, "clothing_store/register.html")

def dashboard_view(request):
    return render(request, "clothing_store/dashboard.html")

def profile_view(request):
    return render(request, "clothing_store/profile.html")

def logout_view(request):
    logout(request)
    return redirect("login")
