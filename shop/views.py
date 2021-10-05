from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Category
from cart.forms import CartAddProductForm
# Create your views here.


def homepage(request):
    # posts = Posts.objects.all()
    return render(request, 'pages/index.html')


def store(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    brand = None
    brands = Brand.objects.all()
    products = Product.objects.filter(avaliable=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.objects.filter(category=category)
    catr_product_form = CartAddProductForm()
    return render(request, 'pages/store.html', {'category': category, 'categories': categories, 'products': products, 'card_product_form': catr_product_form})


def product(request):

    return render(request, 'pages/product.html')


def checkout(request):

    return render(request, 'pages/checkout.html')
