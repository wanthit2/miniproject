from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True, verbose_name="รหัสสินค้า")
    name = models.CharField(max_length=100, verbose_name="ชื่อสินค้า")
    description = models.TextField(blank=True, verbose_name="รายละเอียดสินค้า")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ราคาสินค้า")
    quantity = models.PositiveIntegerField(verbose_name="จำนวนในสต็อก")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่เพิ่มสินค้า")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไขล่าสุด")

    def __str__(self):
        return self.name