from django.contrib import admin
from django.urls import path, include
from myapp import views  # เพิ่ม import views จาก myapp

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.lit_views, name='lit_views'), # เส้นทางสำหรับหน้าแรก
]
