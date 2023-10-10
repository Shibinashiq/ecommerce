from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from brand.models import Brand
from django.contrib import messages
# Create your views here.
def brand(request):
    brand = Brand.objects.all()
    context = {
        'brand':brand
    }
    
    return render(request,'admin_side/brand.html',context)



login_required(login_url='admin_login')
def add_brand(request):
    if request.user.is_superuser:
        if request.method=='POST':
            Brand_name=request.POST.get('brand_name')
            Brand_image=request.FILES.get('brand_image')
            
            print('!!!!!!!!!!!!!!!!!!!',Brand_image)
            
            new_brand=Brand(
                Brand_name=Brand_name,
                Brand_image=Brand_image,
            )
            new_brand.save()
            return redirect ('brand:brand')
        return render(request,'admin_side/add_brand.html')
    else:
        return redirect('admin_login')


login_required(login_url='admin_login')
def edit_brand(request,brand_id):
    print('function is calling')
    if request.user.is_superuser:
        if request.method=='POST':
            brand_name=request.POST.get('brand_name')
            brand_image=request.FILES.get('brand_image')
            var=Brand.objects.get(id=brand_id)
         
            # if Brand.objects.filter(brand_name=brand_name,brand_image=brand_image).exists():
            #     messages.error(request,'already taken')
            #     return redirect('brand:brand')
            var.Brand_name=brand_name
            var.Brand_image=brand_image
            if brand_image:
                var.Brand_image=brand_image
            else:
                pass
            var.save()
            var=Brand.objects.all().order_by('id')
            
            context={
                'var':var
            }
            return redirect('brand:brand')
        
        
    return render(request,'admin_side/brand.html')


def delete_brand(request,brand_id):
    try:
        brand_to_delete=Brand.objects.get(id=brand_id)
        brand_to_delete.delete()
        messages.success(request,'delete successfully')
    except Brand.DoesNotExist:
        messages.error(request,'item does not exist')
    
    return redirect('brand:brand')