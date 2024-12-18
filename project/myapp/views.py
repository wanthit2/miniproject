from django.shortcuts import render
from .models import Product  # ใช้ Product ถ้ามีโมเดล

def lit_views(request):
    products = Product.objects.all()  # ดึงข้อมูลจากฐานข้อมูล
    return render(request, 'lit.html', {'products': products})

def home(request):
    return render(request, 'home.html')

    
