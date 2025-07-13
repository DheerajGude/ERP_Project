from django.db import models
from django.utils import timezone


class ForecastType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Forecast(models.Model):
    MODULE_CHOICES = [
        ('Sales', 'Sales'),
        ('Inventory', 'Inventory'),
        ('Finance', 'Finance'),
        ('Demand', 'Demand'),
        ('Custom', 'Custom'),
    ]

    forecast_type = models.ForeignKey(ForecastType, on_delete=models.SET_NULL, null=True)
    module = models.CharField(max_length=50, choices=MODULE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Forecast Record"
        verbose_name_plural = "Forecast Records"

    def __str__(self):
        return f"{self.module} Forecast ({self.start_date} to {self.end_date})"


class ForecastResult(models.Model):
    forecast = models.ForeignKey(Forecast, on_delete=models.CASCADE, related_name='results')
    date = models.DateField()
    predicted_value = models.DecimalField(max_digits=12, decimal_places=2)
    actual_value = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.date} | Predicted: {self.predicted_value} | Actual: {self.actual_value or 'N/A'}"
