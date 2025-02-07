from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()  # ดึงข้อมูลสินค้าทั้งหมด
    return render(request, 'clothing_store/product_list.html', {'products': products})

def index(request):
    return render(request, 'clothing_store/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # ตรวจสอบว่าชื่อผู้ใช้และรหัสผ่านถูกต้อง
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "เข้าสู่ระบบสำเร็จ!")
            return redirect("index")  # เปลี่ยนเป็นหน้าแรกของคุณ
        else:
            messages.error(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง!")

    return render(request, "clothing_store/login.html")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # ตรวจสอบว่ารหัสผ่านตรงกันหรือไม่
        if password != confirm_password:
            messages.error(request, "รหัสผ่านไม่ตรงกัน!")
            return render(request, "clothing_store/register.html")

        # ตรวจสอบว่ามีชื่อผู้ใช้นี้อยู่แล้วหรือไม่
        if User.objects.filter(username=username).exists():
            messages.error(request, "ชื่อผู้ใช้นี้มีอยู่แล้ว!")
            return render(request, "clothing_store/register.html")

        # สร้างผู้ใช้ใหม่
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # ให้ล็อกอินอัตโนมัติหลังจากสมัครเสร็จ
        login(request, user)
        messages.success(request, "สมัครสมาชิกสำเร็จ!")
        return redirect("index")  # เปลี่ยนเป็นหน้าหลักหลังสมัครเสร็จ

    return render(request, "clothing_store/register.html")