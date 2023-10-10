from django.urls import path
from . import views


app_name='brand'


urlpatterns = [
path('brand/', views.brand, name='brand'),
path('add_brand/', views.add_brand, name='add_brand'), 
path('edit_brand/<int:brand_id>/', views.edit_brand, name='edit_brand'),
path('delete_brand/<int:brand_id>/', views.delete_brand, name='delete_brand')

]


