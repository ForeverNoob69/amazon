from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Customer(models.Model):
#     user = models.OneToOneField(User,null=True,blank=True,on_delete=models.SET_NULL)
#     name = models.CharField(max_length=100,null=True)
#     email = models.CharField(max_length=100,null=True)

#     def __str__(self):
#         return self.name or str(self.id)


class Rating(models.Model):
    customer = models.CharField(max_length=200,null=True,blank=True)
    product_id = models.CharField(max_length=200)

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/images')
    rating = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    date = models.DateField(auto_now_add=True,blank=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.product) + " Order: (" + str(self.order)+")"

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    order = models.ForeignKey(Order,blank=True,null=True,on_delete=models.SET_NULL)
    address = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    zipcode = models.CharField(max_length=50,null=True)

    def __str__(self):
        return str(self.order)
