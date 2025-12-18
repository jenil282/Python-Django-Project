from django.shortcuts import render,redirect
from django.urls import reverse
from .models import*
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    # cid=Main_category.objects.all()
    # s_cid = Sub_category.objects.select_related('Main_category').all()
    cid = Main_category.objects.prefetch_related('sub_category_set').all()

    context = {
        'cid': cid
    }
    # print(s_cid)
    # context={
    #     'cid':cid,
    #     's_cid':s_cid,
    # }

    return render(request,'index.html',context)

def shopdetail(request, id):
    cid = Main_category.objects.all()

    main_sub_cat = Main_category.objects.get(id=id)
    display_item = Main_category.objects.all()
    s_cid = Sub_category.objects.filter(Main_category=main_sub_cat)
    colors = Color.objects.all()
    prices = Price.objects.all()
    size = Size.objects.all()
    products = Product.objects.filter(Sub_category_id=id)

    
    if request.method == "POST":
        
        selected_colors = request.POST.getlist("colors")  
        if selected_colors:
            products = products.filter(color_key_id__in=selected_colors)

       
        selected_prices = request.POST.getlist("price")  
        if selected_prices:
            products = products.filter(price_key_id__in=selected_prices)
        
        selected_size =request.POST.get("size")
        if selected_size:
            products= products.filter(size_key_id__in=selected_size)
            
        
    paginator = Paginator(products, 6)  # 6 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)



    context = {
        "cid": cid,
        "main_sub_cat": main_sub_cat,
        "s_cid": s_cid,
        "display_item": display_item,
        'products': products,
        'colors': colors,
        'prices': prices,
        'size':size,

    }

    return render(request, 'shop.html', context)


def shoplist(request):
    cid = Main_category.objects.prefetch_related('sub_category_set').all()
    colors=Color.objects.all()
    products = Product.objects.all()
        
    if request.method == "POST":
        selected_colors = request.POST.getlist("colors")  
        products = products.filter(color_key__in=selected_colors)
    
    paginator = Paginator(products, 6)  # 6 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)



    context = {
        'cid': cid,
        'products':products,
        'colors':colors,

    }

    return render(request, 'shop.html',context)


    
def detail(request):
    cid = Main_category.objects.prefetch_related('sub_category_set').all()

    context = {
        'cid': cid
    }
    return render(request,'detail.html',context)

def contact(request):
    cid = Main_category.objects.prefetch_related('sub_category_set').all()

    context = {
        'cid': cid
    }
    return render(request,'contact.html',context)

def checkout(request):
    cid = Main_category.objects.prefetch_related('sub_category_set').all()

    context = {
        'cid': cid
    }
    return render(request,'checkout.html',context)

def cart_view(request):
    cid = Main_category.objects.prefetch_related('sub_category_set').all()
    products = Cart.objects.all()
    subtotal=0
    shipping=60
    discount_percentage=25
    tax_percentage=18        
    
    for i in products:
        subtotal+=i.total
    total=subtotal+shipping
    
    discount = subtotal * discount_percentage / 100
    discounted_subtotal = subtotal - discount
    
    tax = discounted_subtotal * tax_percentage / 100

    total = discounted_subtotal + shipping + tax
    
    
    Coupon_amount = 0
    msg = ""
    if request.method=="POST":
        code=request.POST.get("code")

    
        try:
            code= Coupon_Code.objects.get(code=code)
            Coupon_amount=code.price
            total -= Coupon_amount
            
        except Coupon_Code.DoesNotExist:
            msg = "Coupon Code Not Valid"
            

    

    context = {
    'cid': cid,
    'products': products,
    'subtotal': subtotal,
    'shipping': shipping,
    'discount_percentage': discount_percentage,
    'discount': discount,
    'tax_percentage':tax_percentage,
    'tax':tax,
    'total': total,
    'Coupon_amount':Coupon_amount,   
    'msg':msg, 
    }
    return render(request, 'cart.html', context)
    
def cart(request, id):
    cid = Main_category.objects.prefetch_related('sub_category_set').all()

    if id:
        product = Product.objects.get(id=id)
        name = product.name

        cart_item = Cart.objects.filter(name=name).first() 

        if cart_item:
            cart_item.quantity += 1
            cart_item.total = cart_item.quantity * cart_item.price
            cart_item.save()

            # products = Cart.objects.all()
            # context = {
            #         'cid': cid,
            #         'products': products,
            #     }
            # return render(request, 'cart.html',context)

        else:
            Cart.objects.create(
                image=product.image,
                name=product.name,
                price=product.price,
                quantity=1,
                total=product.price
            )


    products = Cart.objects.all()
    
    subtotal=0
    shipping=60
    discount_percentage=25
    tax_percentage=18
    
    for i in products:
        subtotal+=i.total
    total=subtotal+shipping
    
    discount = subtotal * discount_percentage / 100
    discounted_subtotal = subtotal - discount
    
    tax = discounted_subtotal * tax_percentage / 100

    total = discounted_subtotal + shipping + tax
    
    Coupon_amount = 0
    msg = ""
    if request.method=="POST":
        code=request.POST.get("code")

    
        try:
            code= Coupon_Code.objects.get(code=code)
            Coupon_amount=code.price
            total -= Coupon_amount
            
        except Coupon_Code.DoesNotExist:
            msg = "Coupon Code Not Valid"
            

    context = {
    'cid': cid,
    'products': products,
    'subtotal': subtotal,
    'shipping': shipping,
    'discount_percentage': discount_percentage,
    'discount': discount,
    'tax_percentage':tax_percentage,
    'tax':tax,
    'total': total, 
    'Coupon_amount':Coupon_amount,   
    'msg':msg,   
    }
    return render(request, 'cart.html', context)



def cart_quant_sub(request, id):
    cart_item = Cart.objects.get(id=id)
    print(cart_item)
    if request.method == "POST":
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.total = cart_item.quantity * cart_item.price
        else:
            cart_item.quantity = 1 
        cart_item.save()

    # return redirect("cart_view")
    return redirect(f"{reverse('cart_view')}#cart")

def cart_quant_add(request, id):
    cart_item= Cart.objects.filter(id=id).first()
    print(cart_item)
    if request.method =="POST":
        if cart_item:
            cart_item.quantity +=1
            cart_item.total = cart_item.quantity * cart_item.price
            cart_item.save()
        
    # return redirect("cart_view")
    return redirect(f"{reverse('cart_view')}#cart")

def cart_quant_remove(request, id):
    if request.method=="POST":
        Cart.objects.filter(id=id).delete()
        # Cart.objects.all().delete()

    
    return redirect(f"{reverse('cart_view')}#cart")

def user_register(request):
    if request.method=="POST":
        fname=request.POST.get("f_name")
        print(fname)
        lname=request.POST.get("lname")
        user_name=request.POST.get("user_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        User_Register.objects.create(fname=fname,lname=lname,user_name=user_name,email=email,password=password)
        return redirect("user_login")
    return render(request,'register_user.html')
    
    
def user_login(request):

    if "email" in request.session:
        return redirect("index")

    if request.method == "POST":
        user_name = request.POST.get("user_name", "").strip()
        password = request.POST.get("password")

        try:
            user = User_Register.objects.get(user_name__iexact=user_name)

            if user.password == password:

                request.session['user_name'] = user.user_name
                request.session['email'] = user.email

                return redirect("index")

            else:
                return render(request, "login.html", {"msg": "Incorrect Password"})

        except User_Register.DoesNotExist:
            return render(request, "login.html", {"msg": "Incorrect Username"})

    return render(request, "login.html")



def logout(request):
    request.session.flush() 
    return redirect("user_login")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
# def show(request):
#     user = Test.objects.all()
#     user = Test.objects.order_by("name")

#     context = {
#             'user':user
#         }
        
#     return render(request, 'test.html', context)


# def create(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         age = request.POST['age']
#         email = request.POST['email']
#         phone_no = request.POST['phone']
#         name =name.capitalize()
        
#         if len(phone_no)==10:
#             phone_no_int = int(phone_no) 
#             Test.objects.create(
#                 name=name,
#                 age=age,
#                 email=email,
#                 phone_no=phone_no_int
#             )

#         return redirect("show")
    
    
#     return redirect("show")

# def update(request, id):
#     user = Test.objects.get(id=id)

#     if request.method == "POST":
#         name = request.POST.get('name')
#         age = request.POST.get("age")
#         email = request.POST.get("email")
#         phone_no = request.POST.get("phone")
#         user.name=name
#         user.age=age
#         user.email=email
#         user.phone_no=phone_no
#         user.save()

#         return redirect("show")

#     context = {
#         "user": user,
#         "error": "Phone number is invalid. It must be 10 digits.",
#     }
#     return render(request, "update.html", context)


# def delete(request, id):
#     user = Test.objects.get(id=id)
#     if request.method == "POST":
#         user.delete()
#         return redirect("show")

#     return redirect("show")





