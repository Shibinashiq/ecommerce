from django.shortcuts import render

# Create your views here.
def category(request):
    return render(request,'admin/category.html')
    
