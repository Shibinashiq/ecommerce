# category/urls.py
from django.urls import path
from . import views

app_name='product'

    
urlpatterns = [
    path('product',views.product,name='product'),
    path('add_product/', views.add_product, name='add_product'),
   path('edit_product/<int:product_id>/', views.edit_product, name='edit_product')

    
]
