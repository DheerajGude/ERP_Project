from django.db import models
from .customer import Customer
from erp_analytics.models.customer import Customer
from erp_analytics.models.inventory import Product


class Sales(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField()
    customer_name = models.CharField(max_length=100)
    invoice_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.product_name} - {self.invoice_id}"

class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.full_name} - {self.product.name} ({self.quantity})"
