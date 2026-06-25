from django.db import models

# Create your models here.
class Product(models.Model):
    category_choices=[('Electronics', 'Electronics'),
        ('Groceries', 'Groceries'),
        ('Clothing', 'Clothing'),
        ('Stationery', 'Stationery'),
        ('Furniture', 'Furniture')]
    product_name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50, choices=category_choices)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    supplier_name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name