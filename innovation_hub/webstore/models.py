from django.db import models
import datetime


# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Customers
class Customer(models.Model): ...


class Product(models.Model): ...


class Order(models.Model): ...
