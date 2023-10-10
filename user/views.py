import random
from django.db import IntegrityError
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login
from django.views.decorators.cache import never_cache
from django.contrib.auth import login
from .utils import send_otp
from datetime import datetime, timedelta
import pyotp
from django .contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home(request):
    return render (request, 'user/home.html')


def shop(request):
    return render (request,'user/shop_grid.html')

def contact(request):
    return render(request ,'user/contact_page.html')
def blog(request):
    return render(request, 'user/blog.html')
def about_us(request):
    return render(request,'user/about_us.html')
def contact_page(request):
    return render(request,'user/contact_page.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)
        if user is not None:
              
            login(request,user)
            
            messages.success(request,'Login successfully')
            return redirect('home')
        else :
            messages.error(request,'Bad credential Please create new account')
            return redirect('user_signup')
    return render(request, 'user/user_login.html')



def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        username_is_exist = User.objects.get(username=username).exists()
        if username_is_exist :
            messages.error(request, 'User already exists')
            return redirect('user_signup')
        email_is_exist=User.objects.get(username=username).exist()
        if email_is_exist:
            messages.error(request, 'email already exists')
            return redirect('user_signup')    
        
        if password == confirm_password:
            
                
                send_otp(request,email)
                request.session['username']=username
                request.session['email']=email
                request.session['password']=password
                # user = User.objects.create(username=username, email=email, password=make_password(password))
                # user.save()
                return redirect('otp')
        else:
            pass
    return render(request, 'user/user_signup.html')
 
def otp_page(request):
    error_message = None
    if request.method == 'POST':
        otp = request.POST['otp']
        username = request.session['username']  
        otp_secret_key = request.session['otp_secret_key']  # Use square brackets here
        otp_valid_until = request.session['otp_valid_date']  # Use square brackets here
        
        if otp_secret_key and otp_valid_until is not None:
            valid_until = datetime.fromisoformat(otp_valid_until)

            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=60)
                if totp.verify(otp):
                    
                    username=request.session['username']
                    email=request.session['email']
                    password=request.session['password']
                    user = User.objects.create(username=username, email=email, password=make_password(password))
                    user.save()
                    login(request, user)
                    del request.session['email']
                    del request.session['password']
                    del request.session['username']
                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']
                    return redirect(home)
                else:
                    error_message='invalid OTP'
            else:
               error_message='OTP expired'
        else:
            error_message='Oops,something went wrong'
    return render(request, 'user/otp.html', {'error_message':error_message})





@never_cache
def admin_dashboard(request):
    return render(request,'admin_side/admin_dashboard.html')
@never_cache
def admin_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request,'invalid user please try again')
            return redirect('admin_login')
       
    
    return render(request,'admin_side/admin_login.html')



def admin_users(request):
    register_details=User.objects.all()
    context ={
        'register_details':register_details
    }
        
    return render(request,'admin_side/admin_users.html',context)

def user_block(request,user_id):
    user=User.objects.get(id=user_id)
    user.is_blocked=True
    user.save()
    messages.success(request,f'User{user.username} is blocked successfully')
    return redirect ('admin_users')
    
def user_unblock(request,user_id):
    user=User.objects.get(id=user_id)
    user.is_blocked=False
    user.save()
    messages.success(request,f'User{user.username} is unblocked successfully')
    return redirect ('admin_users')



def product(request):
    
    return render (request, 'product.html')







def form(request):
    return render(request,'admiin/form.html')

