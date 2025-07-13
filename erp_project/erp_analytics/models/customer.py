from django.db import models
from django.utils import timezone


class Customer(models.Model):
    CUSTOMER_TYPES = [
        ('Retail', 'Retail'),
        ('Wholesale', 'Wholesale'),
        ('Corporate', 'Corporate'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Blacklisted', 'Blacklisted'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=100, default='India')
    customer_type = models.CharField(max_length=50, choices=CUSTOMER_TYPES, default='Retail')
    gst_number = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    def is_active(self):
        return self.status == 'Active'
+