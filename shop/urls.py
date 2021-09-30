from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    path('store', views.store, name='store'),
    url(r'^product$', views.product, name='product'),
    path('checkout', views.checkout, name='checkout'),
    # path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    # url(r'^contact/$', views.contact, name='contact'),
    # url(r'^login/$', views.user_login, name='login'),
]
