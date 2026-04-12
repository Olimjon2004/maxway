from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to='products')
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    cost = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'


class Customer(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Order(models.Model):
    pyment_type = models.IntegerField(null=False, blank=False)
    status = models.CharField(blank=False, null=False, default=1)
    address = models.CharField(max_length=100, blank=False, null=False)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    

class OrderProduct(models.Model):
    count = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)

