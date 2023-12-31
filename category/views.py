from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from category import models

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
            description = request.POST.get('description')
            new_category = Category(
                cat_image=cat_image,
                category_name=category_name,
                description=description
            )
           
            new_category.save()
            return redirect('category:category')
        return render(request,'admin_side/add_category.html')

    else:
        # Handle the case where the user is not a superuser (optional)
        return redirect('admin_login')




login_required(login_url='admin_login')
def edit_category(request, cat_id):
    if request.user.is_superuser:
        if request.method=='POST':
            category_name=request.POST.get('category_name')
           
            description=request.POST.get('description')
            cat = Category.objects.get(id=cat_id)
            if Category.objects.filter(category_name = category_name ,  description = description).exists():
                messages.error(request,'already taken')
                print('already taken')
                return redirect('category:category')
            cat.category_name = category_name 
           
            cat.description  = description
            cat_image=request.FILES.get('cat_image')
            if cat_image:
                cat.cat_image = cat_image
            else:
                pass
            cat.save()
            
            cat=Category.objects.all().order_by('id')
            context={
                cat:'cat'
            }
            return redirect('category:category')
    return render(request,'admin_side/edit_category.html')


def delete_category(request,cat_id): 
    
    try :
         category_to_delete = Category.objects.get(id=cat_id)
         category_to_delete.delete()
         messages.success(request,'delete successfully')
    except Category.DoesNotExist:
        messages.error(request,'item does not exist')
    return redirect ('category:category')
    