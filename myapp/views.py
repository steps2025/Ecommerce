from django.http import HttpResponse
from .models import Category, Subcategory,Product
from django.shortcuts import render, get_object_or_404


def index(request):
    categories = Category.objects.prefetch_related('subcategories').all()
    
    return render(request, "shopify/index.html", context={'categories': categories})

def about(request):
    return render(request, "shopify/about.html")

def contact(request):
    return render(request, "shopify/contact.html")

def products(request,category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategory = Subcategory.objects.filter(category= category)
    return render(request, "shopify/products.html", {
        'category': category,
        'subcategory': subcategory
    })

def specific_subcategory(request,subproduct_id):
    subcategory = get_object_or_404(Subcategory,id=subproduct_id)
    products = Product.objects.filter(subcategory=subcategory)
    return render( request,"shopify/specific_subproduct.html",{
        'subcategory': subcategory,
        'products': products,
    })

def single_product(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "shopify/single-product.html",{'product':product})


