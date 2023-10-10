# category/urls.py
from django.urls import path
from . import views

app_name='product'

    
urlpatterns = [
      path('add_product/', views.add_product, name='add_product'),
    
]
