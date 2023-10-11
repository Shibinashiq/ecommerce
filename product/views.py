from django.shortcuts import redirect, render
from product.models import Product
from category.models import Category
from brand.models import Brand
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# def product(request):
    
#     return render (request, 'product.html')

def product(request):
    product=Product.objects.all()
    brand = Brand.objects.all()
    category = Category.objects.all()
    context = {
        'brand':brand,
        'category':category,
        'product':product,
    }
    return render(request,'admin_side/product.html',context)


def add_product(request):
    if request.user.is_superuser:
        if request.method=='POST':
            product_name=request.POST.get('product_name')
            product_price=request.POST.get('product_price')
            product_brand=request.POST.get('product_brand')
            product_offer=request.POST.get('product_offer')
            product_category=request.POST.get('product_category')
            product_quantity=request.POST.get('product_quantity')
            product_image = request.FILES.get('product_image')
            new_product=Product (
                 product_name= product_name,
                 product_brand=product_brand,
                 product_offer=product_offer,
                 product_category=product_category,
                 product_quantity=product_quantity,
                 product_price=product_price,
                 product_image = product_image
                            
            )     
            new_product.save()
        return redirect('product:product')
    
    return render(request,'admin_side/add_product.html')

@login_required(login_url='admin_login')
def edit_product(request, product_id):
    if request.user.is_superuser:
        product = Product.objects.get(id=product_id)  # Get the product by ID
        
        if request.method == 'POST':
            product_name = request.POST.get('product_name')
            product_price = request.POST.get('product_price')
            product_brand = request.POST.get('product_brand')
            product_offer = request.POST.get('product_offer')
            product_category = request.POST.get('product_category')
            product_quantity = request.POST.get('product_quantity')
            product_image = request.FILES.get('product_image')

            # Check if a product with the same name and image already exists
            if Product.objects.filter(product_name=product_name, product_image=product_image).exclude(id=product_id).exists():
                messages.error(request, 'A product with the same name and image already exists.')
                return redirect('product:product')

            # Update the product attributes
            product.product_name = product_name
            product.product_price = product_price
            product.product_brand = product_brand
            product.product_offer = product_offer
            product.product_category = product_category
            product.product_quantity = product_quantity
            
            if product_image:
                product.product_image = product_image

            product.save()

            return redirect('product:product')

    #
    return render(request, 'admin_side/edit_product.html', {'product': product})



def delete_product(request,product_id):
    try:
        product_to_delete=Product.objects.get(id=product_id)
        product_to_delete.delete()
        messages.success(request,'deleted successfully')
    except Product.DoesNotExist:
        messages.error(request,'item does not exist')
    return redirect('product:product')