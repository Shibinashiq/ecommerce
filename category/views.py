from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from category.models import Category


def category(request):
    cat=Category.objects.all()
    context={
            'cat': cat
        }
    return render(request,'admin_side/category.html',context)




@login_required(login_url='admin_login')
def add_category(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            category_name = request.POST.get('name')
            cat_image = request.FILES.get('image')
            brand = request.POST.get('brand')
            description = request.POST.get('description')
            print('hii')
            new_category = Category(
                cat_image=cat_image,
                category_name=category_name,
                brand=brand,
                description=description
            )
           
            new_category.save()
            return redirect('category:category')
        return render(request,'admin_side/add_category.html')

    else:
        # Handle the case where the user is not a superuser (optional)
        return redirect('admin_login')




login_required(login_url='admin_login')
def edit_category(request):
    return render(request,'admin_side/edit_category.html')
