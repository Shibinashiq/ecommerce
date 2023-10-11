
from django.urls import path 
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('shop',views.shop,name='shop'),
    path('contact',views.contact,name='contact'),
    path('blog',views.contact,name='blog.html'),
    path('about_us',views.about_us,name='about_us.html'),
    path('contact_page',views.contact_page,name='contact_page.html'),
    path('otp',views.otp_page,name='otp'),
    path('user_login',views.user_login, name='user_login'),
    path('user_signup',views.user_signup, name='user_signup'),
    path('admin_dashboard.html', views.admin_dashboard, name='admin_dashboard'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_users',views.admin_users,name='admin_users'),
    path('user_block/<int:user_id>/', views.user_block, name='user_block'),
    path('user_unblock/<int:user_id>/',views.user_unblock,name='user_unblock'),
    
    
]
