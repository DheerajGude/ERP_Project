from django.db import models
from django.utils import timezone
from erp_analytics.models.supplier import Supplier


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, default='pcs')
    reorder_level = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.sku})"

    def profit_margin(self):
        return self.selling_price - self.cost_price


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stocks')
    quantity_available = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product',)

    def __str__(self):
        return f"{self.product.name} – {self.quantity_available} {self.product.unit}"

    def is_below_reorder_level(self):
        return self.quantity_available <= self.product.reorder_level


class StockMovement(models.Model):
    MOVEMENT_TYPE = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
        ('ADJUSTMENT', 'Adjustment'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPE)
    reference_note = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_movement_type_display()} | {self.product.name} | {self.quantity}"
