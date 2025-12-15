"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("", views.show, name="show"),   
    # path("create/", views.create, name="create"),
    # path("update/<int:id>/", views.update, name="update"),
    # path("delete/<int:id>/", views.delete, name="delete"),


    # path('',views.create,name="show")
    path('', views.index, name='index'),
    path('shop-list', views.shoplist, name='shop-list'),
    path('shop/<int:id>', views.shopdetail, name='shop-detail'),
    path('detail', views.detail, name='detail'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    path('cart_view', views.cart_view, name='cart_view'),
    path('cart/<int:id>', views.cart, name='cart'),
    path('user_register',views.user_register, name="user_register"),
    path('user_login', views.user_login, name="user_login"),
    path('logout',views.logout, name="logout"),
    path('cart_quant_sub/<int:id>',views.cart_quant_sub, name="cart_quant_sub"),
    path('cart_quant_add/<int:id>',views.cart_quant_add, name="cart_quant_add"),
    path('cart_quant_remove/<int:id>',views.cart_quant_remove, name="cart_quant_remove"),

    

    
]

