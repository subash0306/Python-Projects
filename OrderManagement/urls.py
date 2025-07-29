from django.urls import path
from .views import *

urlpatterns = [
    path('all/customers/', CustomerList),
    path('add/customers/', CustomerAdd),
    path('Update/customer/<int:id>/', CustomerUpdate, name='customer_update'),
    path('Delete/customer/<int:id>/', CustomerDelete, name='customer_delete')
]