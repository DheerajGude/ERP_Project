from django.urls import path
from erp_analytics import views

# API modules
from erp_analytics.api import (
    customer_api,
    employee_api,
    sales_api,
    inventory_api,
    supplier_api,
    finance_api,
    logistics_api,
    forecast_api
)

urlpatterns = [

    # ===================== HOME / LOGIN =====================
    path('', views.home_view, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('admin-login/', views.AdminLoginView.as_view(), name='admin_login'),

    # ===================== CUSTOMERS =====================
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    # ===================== EMPLOYEES =====================
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    # ===================== SALES =====================
    path('sales/', views.sales_list, name='sales_list'),
    path('sales/<int:pk>/', views.sales_detail, name='sales_detail'),
    path('sales/create/', views.sales_create, name='sales_create'),
    path('sales/<int:pk>/edit/', views.sales_update, name='sales_update'),
    path('sales/<int:pk>/delete/', views.sales_delete, name='sales_delete'),
    
    # ===================== INVENTORY =====================
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('inventory/create/', views.inventory_create, name='inventory_create'),
    path('inventory/<int:pk>/edit/', views.inventory_update, name='inventory_update'),
    path('inventory/<int:pk>/delete/', views.inventory_delete, name='inventory_delete'),

    # ===================== FORECAST =====================
    path('forecast/', views.forecast_dashboard, name='forecast_dashboard'),
    path('forecast/overview/', views.forecast_overview, name='forecast_overview'),
    # =================== LOGISTICS ===================
    path('logistics/', views.logistics_shipping, name='logistics_shipping'),



    # ===================== SUPPLIERS =====================
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/edit/', views.supplier_update, name='supplier_update'),
    path('suppliers/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),

    # ===================== FINANCE =====================
    path('finance/', views.finance_list, name='finance_list'),
    path('finance/<int:pk>/', views.finance_detail, name='finance_detail'),
    path('finance/create/', views.finance_create, name='finance_create'),
    path('finance/<int:pk>/edit/', views.finance_update, name='finance_update'),
    path('finance/<int:pk>/delete/', views.finance_delete, name='finance_delete'),

    # ===================== LOGISTICS =====================
    path('logistics/', views.logistics_list, name='logistics_list'),
    path('logistics/<int:pk>/', views.logistics_detail, name='logistics_detail'),
    path('logistics/create/', views.logistics_create, name='logistics_create'),
    path('logistics/<int:pk>/edit/', views.logistics_update, name='logistics_update'),
    path('logistics/<int:pk>/delete/', views.logistics_delete, name='logistics_delete'),

    # ===================== REST API ROUTES =====================

    # Customers
    path('api/customers/', customer_api.CustomerListAPI.as_view(), name='api_customer_list'),
    path('api/customers/<int:pk>/', customer_api.CustomerDetailAPI.as_view(), name='api_customer_detail'),

    # Employees
    path('api/employees/', employee_api.EmployeeListAPI.as_view(), name='api_employee_list'),
    path('api/employees/<int:pk>/', employee_api.EmployeeDetailAPI.as_view(), name='api_employee_detail'),

    # Sales
    path('api/sales/', sales_api.SalesListAPI.as_view(), name='api_sales_list'),
    path('api/sales/<int:pk>/', sales_api.SalesDetailAPI.as_view(), name='api_sales_detail'),

    # Inventory
    path('api/inventory/', inventory_api.InventoryListAPI.as_view(), name='api_inventory_list'),
    path('api/inventory/<int:pk>/', inventory_api.InventoryDetailAPI.as_view(), name='api_inventory_detail'),

    # Suppliers
    path('api/suppliers/', supplier_api.SupplierListAPI.as_view(), name='api_supplier_list'),
    path('api/suppliers/<int:pk>/', supplier_api.SupplierDetailAPI.as_view(), name='api_supplier_detail'),

    # Finance
    path('api/finance/', finance_api.FinanceListAPI.as_view(), name='api_finance_list'),
    path('api/finance/<int:pk>/', finance_api.FinanceDetailAPI.as_view(), name='api_finance_detail'),

    # Logistics
    path('api/logistics/', logistics_api.LogisticsListAPI.as_view(), name='api_logistics_list'),
    path('api/logistics/<int:pk>/', logistics_api.LogisticsDetailAPI.as_view(), name='api_logistics_detail'),

    # Forecast
    path('api/forecast/', forecast_api.ForecastAPIView.as_view(), name='api_forecast'),
]
