# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, db_comment='รหัสหมวดหมู่')
    category_name = models.CharField(max_length=50, db_comment='ชื่อหมวดหมู่')

    class Meta:
        managed = False
        db_table = 'category'


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True, db_comment='รหัสสั่งซื้อ')
    customer_id = models.IntegerField(db_comment='รหัสลูกค้า')
    total_price = models.IntegerField(db_comment='ราคารวมทั้วหมด')
    order_date = models.DateField(db_comment='วันที่สั่งซื้อ')
    status = models.CharField(max_length=50, db_comment='สถานะ')
    payment_method = models.CharField(max_length=50, db_comment='วิธีชำระเงิน')
    shipping_address = models.CharField(max_length=50, db_comment='ที่อยู่ในการจัดส่ง')
    tracking_number = models.IntegerField(db_comment='หมายเลขติดต่อ')
    created_at = models.DateTimeField(db_comment='สร้างเมื่อ')
    update_at = models.DateTimeField(db_comment='แก้ไขเมื่อ')

    class Meta:
        managed = False
        db_table = 'order'


class OrderDetail(models.Model):
    order_detail_id = models.IntegerField(primary_key=True, db_comment='รหัสรายละเอียดของสินค้า')
    order_id = models.IntegerField(db_comment='รหัสสั่งซื้อ')
    product_id = models.IntegerField(db_comment='รหัสสินค้า')
    quantity = models.IntegerField(db_comment='ปริมาณ')
    subtotal_price = models.IntegerField(db_comment='ราคารวมยอด')

    class Meta:
        managed = False
        db_table = 'order_detail'


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True, db_comment='รหัสการชำระเงิน')
    order_id = models.IntegerField(db_comment='รหัสสินค้า')
    payment_method = models.IntegerField(db_comment='วิธีการชำระเงิน')
    amount = models.IntegerField(db_comment='จำนวน')
    payment_date = models.DateField(db_comment='วันที่ชำระเงิน')
    status = models.IntegerField(db_comment='สถานะ')

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True, db_comment='รหัสสินค้า')
    name_product = models.CharField(db_column='Name_Product', max_length=50, db_comment='ชื่อสินค้า')  # Field name made lowercase.
    description = models.CharField(max_length=200, db_comment='คำอธิบาย')
    price = models.IntegerField(db_comment='ราคา')
    size = models.CharField(max_length=10, db_comment='ไซส์')
    color = models.CharField(max_length=10, db_comment='สี')
    stock = models.IntegerField(db_comment='จำนวนสินค้า')
    category_id = models.IntegerField(db_comment='รหัสหมวดหมู่')
    seller_id = models.IntegerField(db_comment='รหัสผู้ขาย')
    created_at = models.DateTimeField(db_comment='วันที่สร้างสินค้า')
    update_at = models.DateTimeField(db_comment='วันที่แก้ไข')

    class Meta:
        managed = False
        db_table = 'product'


class Review(models.Model):
    customer_id = models.IntegerField(db_comment='รหัสลูกค้า')
    product_id = models.IntegerField(db_comment='รหัสสินค้า')
    rating = models.IntegerField(db_comment='ตวามพึงพอใจในสินค้า')
    comment = models.CharField(max_length=50, db_comment='คอมเม้น')
    review_date = models.DateField(db_comment='วันที่ตรวจสอบ')
    review_id = models.IntegerField(primary_key=True, db_comment='รหัสรีวิว')

    class Meta:
        managed = False
        db_table = 'review'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=10, db_comment='ไอดีผู้ใช้')
    username = models.CharField(max_length=50, db_comment='ชื่อผู้ใช้')
    email = models.CharField(max_length=50, db_comment='อีเมล')
    password = models.IntegerField(db_comment='รหัส')
    address = models.CharField(max_length=50, db_comment='ที่อยู่')
    phone = models.IntegerField(db_comment='เบอร์โทร')
    created_at = models.DateField(db_comment='วันที่ใช้งาน')

    class Meta:
        managed = False
        db_table = 'user'
