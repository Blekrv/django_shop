from django.shortcuts import render

# Create your views here.


def homepage(request):
    # posts = Posts.objects.all()
    return render(request, 'pages/index.html')


def store(request):
    # posts = Posts.objects.all()
    return render(request, 'pages/store.html')


def product(request):
    # posts = Posts.objects.all()
    return render(request, 'pages/product.html')


def checkout(request):
    # posts = Posts.objects.all()
    return render(request, 'pages/checkout.html')
