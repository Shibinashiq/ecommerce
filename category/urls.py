# category/urls.py
from django.urls import path
from . import views

app_name='category'


urlpatterns = [
    path('category/', views.category, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/', views.edit_category, name='edit_category'),
]
