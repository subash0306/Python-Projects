from django.shortcuts import render, redirect
from .forms import *
from .models import *


def ProductsAdd(request):
    
    context = {
        'product_form' : Product_Form()
    }
    if request.method == "POST":
        product_form = Product_Form(request.POST)
        if product_form.is_valid():
            product_form.save()

    return render(request, 'product_add.html', context)

def ShowProducts(request):
    context = {
        'show_products' : Product.objects.all()
    }
    
    return render(request, 'products.html', context)

def DeleteProducts(request, id):
    selected_product = Product.objects.get(id = id)
    selected_product.delete()
    return redirect('/Inventory/products/')

def UpdateProduct(request, id):
    selected_product = Product.objects.get(id = id)
    context = {
        "product_form" : Product_Form(instance=selected_product)
    }
    if request.method == 'POST':
        product_form = Product_Form(request.POST, instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            return redirect('/Inventory/products/')
        
    return render(request, 'product_add.html', context)