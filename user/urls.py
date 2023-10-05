
from django.urls import path 
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('shop',views.shop,name='shop'),
    path('contact',views.contact,name='contact'),
    path('blog',views.contact,name='blog.html'),
    path('about_us',views.about_us,name='about_us.html'),
    path('contact_page',views.contact_page,name='contact_page.html'),
    path('user_login',views.user_login, name='user_login'),
    path('user_signup',views.user_signup, name='user_signup'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin_login/', views.admin_login, name='admin_login')
    
]
