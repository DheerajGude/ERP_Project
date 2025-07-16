from django.db import models
from django.utils import timezone


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=100, default='India')
    gst_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class SupplierItem(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    lead_time_days = models.PositiveIntegerField(default=7)

    def __str__(self):
        return f"{self.item_name} by {self.supplier.name}"


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Ordered', 'Ordered'),
        ('Received', 'Received'),
        ('Cancelled', 'Cancelled'),
    ]

    po_number = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    expected_delivery = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return f"PO #{self.po_number} - {self.supplier.name}"


class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(SupplierItem, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()

    def total_price(self):
        return self.quantity * self.purchase_order

    def __str__(self):
        return f"{self.quantity} x {self.quantity}"
