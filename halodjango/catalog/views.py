from django.shortcuts import render, get_object_or_404
from .models import Product, ProductFeature

def index(request):
    featured_products = Product.objects.filter(in_stock=True)[:3]
    return render(request, 'catalog/index.html', {'featured_products': featured_products})

def product_list(request):
    category = request.GET.get('category')
    if category:
        products = Product.objects.filter(category=category, in_stock=True)
    else:
        products = Product.objects.filter(in_stock=True)
    
    categories = Product.objects.values_list('category', flat=True).distinct()
    context = {
        'products': products,
        'categories': categories,
        'current_category': category
    }
    return render(request, 'catalog/product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:3]
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'catalog/product_detail.html', context)

def contact(request):
    return render(request, 'catalog/contact.html')
