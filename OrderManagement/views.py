from django.shortcuts import render, redirect
from .models import *
from .forms import *

def CustomerList(request):
    context = {
        'all_customers' : Customer.objects.all()
    }
    
    return render(request, 'customers.html', context)

def CustomerAdd(request):
    
    context = {
        'customer_form' : Customer_Form()
    }
    if request.method == "POST":
        customer_form = Customer_Form(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/Orders/all/customers')
        else:
            print("Enter the valid customerName and Date")

    return render(request, 'customers_add.html', context)

def CustomerUpdate(request, id):
    selected_customers = Customer.objects.get(id = id)
    context = {
        "customer_form" : Customer_Form(instance=selected_customers)
    }
    if request.method == 'POST':
        customer_form = Customer_Form(request.POST, instance=selected_customers)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/Orders/all/customers')
        
    return render(request, 'customers_add.html', context)

def CustomerDelete(request, id):
    selected_product = Customer.objects.get(id = id)
    selected_product.delete()
    return redirect('/Orders/all/customers')