from django.shortcuts import render

from .forms import RawProductForm
from .models import Product

def product_create_view(request):
    form=RawProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=RawProductForm()
    context={
        'form':form
    }
    return render(request,"product_templates/product_create.html",context)

def product_detail_view(request):
    obj = Product.objects.get(id=8)
    context={
        'object':obj
    }
    return render(request,"product_templates/detail.html",context)