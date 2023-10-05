from django.shortcuts import render

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
    return render(request, 'user/user_login.html')

def user_signup(request):
    return render (request,'user/user_signup.html')


def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')

def admin_login(request):
    return render(request,'admin/admin_login.html')