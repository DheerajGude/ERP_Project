# erp_analytics/views.py
# pylint: disable=no-member, unused-argument

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from erp_analytics.models.sales import Sales


# Import all required models
from erp_analytics.models.customer import Customer
from erp_analytics.models.employee import Employee, Attendance
from erp_analytics.models.sales import SalesOrder
from erp_analytics.models.inventory import Product
from erp_analytics.models.forecast import Forecast
from erp_analytics.models.supplier import Supplier
from erp_analytics.models.finance import Transaction
from erp_analytics.models.logistics import Shipment

# ============================
# Home + Auth Views
# ============================

def home_view(request):
    return render(request, 'home.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

class AdminLoginView(LoginView):
    template_name = 'admin_login.html'

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    return render(request, 'register.html')

# ============================
# Dashboards (Role-Based)
# ============================

def hr_dashboard(request):
    return render(request, 'dashboards/hr_dashboard.html')

def manager_dashboard(request):
    return render(request, 'dashboards/manager_dashboard.html')

def employee_dashboard(request):
    return render(request, 'dashboards/employee_dashboard.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

# ============================
# CUSTOMER MODULE (UI Views)
# ============================

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        Customer.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('customer_list')
    return render(request, 'customers/customer_form.html')

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.address = request.POST.get('address')
        customer.save()
        return redirect('customer_list')
    return render(request, 'customers/customer_form.html', {'customer': customer})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})

# ============================
# EMPLOYEE MODULE (UI Views)
# ============================

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        data = request.POST
        Employee.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            role=data.get('role'),
            department=data.get('department'),
            date_of_joining=data.get('date_of_joining'),
            is_active=data.get('is_active') == 'on'
        )
        return redirect('employee_list')
    return render(request, 'employees/employee_form.html')

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        data = request.POST
        employee.name = data.get('name')
        employee.email = data.get('email')
        employee.phone = data.get('phone')
        employee.role = data.get('role')
        employee.department = data.get('department')
        employee.date_of_joining = data.get('date_of_joining')
        employee.is_active = data.get('is_active') == 'on'
        employee.save()
        return redirect('employee_list')
    return render(request, 'employees/employee_form.html', {'employee': employee})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

# ============================
# SALES MODULE (UI Views)
# ============================

def sales_list(request):
    query = request.GET.get('q')
    sales_qs = Sales.objects.all()

    if query:
        sales_qs = sales_qs.filter(customer__name__icontains=query)  # or product_name__icontains=query

    paginator = Paginator(sales_qs, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'erp_analytics/sales/list.html', {
        'sales': page_obj
    })

def sales_detail(request, pk):
    order = get_object_or_404(SalesOrder, pk=pk)
    return render(request, 'sales/sales_detail.html', {'order': order})

def sales_create(request):
    return render(request, 'sales/sales_form.html')

def sales_update(request, pk):
    return render(request, 'sales/sales_form.html')

def sales_delete(request, pk):
    return render(request, 'sales/sales_confirm_delete.html')

# ============================
# INVENTORY MODULE (UI Views)
# ============================

def inventory_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

# ============================
# SUPPLIER MODULE (UI Views)
# ============================

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

# ============================
# FORECAST MODULE (UI Views)
# ============================

def forecast_dashboard(request):
    forecasts = Forecast.objects.all()
    return render(request, 'forecast/forecast_dashboard.html', {'forecasts': forecasts})

# ============================
# FINANCE MODULE (UI Views)
# ============================

def finance_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'finance/finance_list.html', {'transactions': transactions})

# ============================
# LOGISTICS MODULE (UI Views)
# ============================

def logistics_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'logistics/logistics_list.html', {'shipments': shipments})

def logistics_detail(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)
    return render(request, 'logistics/logistics_detail.html', {'shipment': shipment})

def logistics_create(request):
    return render(request, 'logistics/logistics_form.html')

def logistics_update(request, pk):
    return render(request, 'logistics/logistics_form.html')

def logistics_delete(request, pk):
    return render(request, 'logistics/logistics_confirm_delete.html')
