from django.db import models

# Create your models here.
class Main_category(models.Model):
    category_name=models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
    
class Sub_category(models.Model):
    Main_category=models.ForeignKey(Main_category,on_delete=models.CASCADE,blank=True,null=True)
    sub_category_name=models.CharField(max_length=50)
    def __str__(self):
        return self.sub_category_name
    
class Color(models.Model):
    color_name=models.CharField(max_length=20)
    def __str__(self):
        return self.color_name
    
class Price(models.Model):
    product_price=models.IntegerField()
    def __str__(self):
        return str(self.product_price)
    
class Size(models.Model):
    size_name=models.CharField(max_length=10)
    def __str__(self):
        return str(self.size_name)
    
    
class Product(models.Model): 
    Sub_category=models.ForeignKey(Sub_category,on_delete=models.CASCADE,blank=True,null=True)
    color_key=models.ForeignKey(Color,on_delete=models.CASCADE,blank=True,null=True)
    price_key=models.ForeignKey(Price,on_delete=models.CASCADE,blank=True,null=True)
    size_key=models.ForeignKey(Size,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to="products/")
    
    def __str__(self):
        return self.name
    
    
class User_Register(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    user_name=models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.fname
    

class Cart(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)
    total=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
    
    
# class Test(models.Model):
#     name=models.CharField(max_length=100)
#     age=models.IntegerField(max_length=100)
#     email=models.EmailField(max_length=50)
#     phone_no=models.IntegerField(max_length=15)

#     def __str__(self):
#         return self.name