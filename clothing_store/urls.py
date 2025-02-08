from django.urls import path
from .views import index, product_list, login_view, about_view  # ตรวจสอบว่าทุกฟังก์ชันนี้มีอยู่จริงใน views.py

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product_list'),
    path('login/', login_view, name='login'),
    path('about/', about_view, name='about'),
]
