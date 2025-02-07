from django.urls import path
from .views import index, product_list, login_view, register_view  # ✅ เพิ่ม register_view

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list, name='product_list'),
    path('login/', login_view, name='login'),
    path('signup/', register_view, name='signup'),  # ✅ ใช้ register_view ตรงๆ
]
