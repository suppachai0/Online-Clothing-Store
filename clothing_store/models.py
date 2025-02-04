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
