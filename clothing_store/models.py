from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # ชื่อสินค้า
    description = models.TextField(blank=True, null=True)  # รายละเอียด
    price = models.DecimalField(max_digits=10, decimal_places=2)  # ราคา
    stock = models.PositiveIntegerField()  # จำนวนสินค้าในสต็อก
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # รูปภาพสินค้า
    created_at = models.DateTimeField(auto_now_add=True)  # วันที่สร้าง
    updated_at = models.DateTimeField(auto_now=True)  # วันที่อัปเดตล่าสุด

    def __str__(self):
        return self.name
# Create your models here.
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity  # คำนวณราคารวมของสินค้าในตะกร้า

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ผู้ใช้ที่สั่งซื้อ
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # ราคารวม
    created_at = models.DateTimeField(auto_now_add=True)  # วันที่สร้างออเดอร์
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')  # สถานะออเดอร์

    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # เชื่อมกับออเดอร์
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # สินค้า
    quantity = models.PositiveIntegerField()  # จำนวน
    price = models.DecimalField(max_digits=10, decimal_places=2)  # ราคาต่อหน่วย

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"
