from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, Order, OrderItem  # ✅ Import ที่ถูกต้อง

def product_list(request):
    products = Product.objects.all()  # ดึงข้อมูลสินค้าทั้งหมด
    return render(request, 'clothing_store/product_list.html', {'products': products})

def index(request):
    return render(request, 'clothing_store/index.html')

# 🛒 View สำหรับแสดงตะกร้าสินค้า
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'clothing_store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

# ➕ เพิ่มสินค้าลงตะกร้า
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1  # เพิ่มจำนวนสินค้า
    cart_item.save()
    return redirect('cart')

# ❌ ลบสินค้าจากตะกร้า
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')

# 💳 Checkout ระบบสั่งซื้อ
@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price() for item in cart_items)

    if request.method == 'POST':
        # ✅ สร้างออเดอร์ใหม่
        order = Order.objects.create(user=request.user, total_price=total_price)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
        
        cart_items.delete()  # ✅ ลบสินค้าทั้งหมดออกจากตะกร้า
        return redirect('order_complete')

    return render(request, 'clothing_store/checkout.html', {'cart_items': cart_items, 'total_price': total_price})

def about_view(request):
    return render(request, 'clothing_store/about.html')


def login_view(request):
    return render(request, 'clothing_store/login.html')  # ✅ ตรวจสอบชื่อไฟล์ให้ถูกต้อง