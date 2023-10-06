from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login
from django.views.decorators.cache import never_cache

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
    
    if request.method=='POST':
    
       username=request.POST['username']
       email=request.POST['email'] 
       password=request.POST['password']
       confirm_password=request.POST['confirm_password']
       if password==confirm_password:
           try:
               
                user=User.objects.create(username=username,email=email,password=make_password(password))
                user.save()
                auth.login(request, user)

                messages.success(request,"your account has been created successfully")
                return redirect ('home')       
           except IntegrityError:
               messages.error(request,'User is already exists')
       else:
           messages.error(request,'Password is already taken')
    return render(request,'user/user_signup.html')






      # admin section



@never_cache
def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')
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
       
    
    return render(request,'admin/admin_login.html')



def admin_users(request):
    register_details=User.objects.all()
    context ={
        'register_details':register_details
    }
        
    return render(request,'admin/admin_users.html',context)

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

