from django.db import models
import datetime


# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    # change the name of the table in admin sect
    class Meta:
        verbose_name_plural = "categories"


# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pthone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# products
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=240, blank=True, default="", null=True)
    image = models.ImageField(upload_to="uploads/product")
    # product on sale
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


# customer models
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default="", blank=True, null=True)
    phone = models.CharField(max_length=20, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
