from django.shortcuts import render

# Create your views here.


def product(request):
    return render(request,'admin_side/product.html')


def add_product(request):
    if request.user.is_superuser:
        if request.method=='POST':
            product_name=request.POST.get('name')
    
    return render(request,'admin_side/add_product.html')