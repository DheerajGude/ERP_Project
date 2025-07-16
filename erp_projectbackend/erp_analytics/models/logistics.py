from django.db import models
from django.utils import timezone
from erp_analytics.models.sales import SalesOrder
from erp_analytics.models.employee import Employee



class Logistics(models.Model):
    name = models.CharField(max_length=100)
    logistics_partner = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    dispatch_date = models.DateField()
    expected_delivery = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=[
            ('Dispatched', 'Dispatched'),
            ('In Transit', 'In Transit'),
            ('Delivered', 'Delivered'),
            ('Delayed', 'Delayed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Dispatched'
    )
    tracking_id = models.CharField(max_length=100, unique=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.tracking_id}"

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Truck', 'Truck'),
        ('Van', 'Van'),
        ('Bike', 'Bike'),
        ('Ship', 'Ship'),
        ('Air', 'Air Cargo'),
    ]

    vehicle_number = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    driver = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    capacity_in_kg = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.vehicle_number} ({self.vehicle_type})"


class Shipment(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    estimated_arrival = models.DateTimeField()
    actual_arrival = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Delayed', 'Delayed'),
        ('Cancelled', 'Cancelled'),
    ], default='Pending')
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Shipment #{self.departure_time} - {self.status}"

    def is_delayed(self):
        return self.actual_arrival and self.actual_arrival > self.estimated_arrival


class DeliveryStatus(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='delivery_updates')
    status_time = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=255)
    status_note = models.CharField(max_length=255)

    def __str__(self):
        return f"Shipment: {self.shipment}"

