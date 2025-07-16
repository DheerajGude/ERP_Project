from django.contrib import admin

from erp_analytics.models.customer import Customer
from erp_analytics.models.employee import Employee
from erp_analytics.models.employee import Attendance
from erp_analytics.models.sales import SalesOrder
from erp_analytics.models.inventory import Product
from erp_analytics.models.forecast import Forecast
from erp_analytics.models.supplier import Supplier
from erp_analytics.models.finance import Transaction
from erp_analytics.models.logistics import Shipment


admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(SalesOrder)
admin.site.register(Product)
admin.site.register(Forecast)
admin.site.register(Supplier)
admin.site.register(Transaction)
admin.site.register(Shipment)
