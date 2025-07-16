from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .forecast_views import forecast_overview

from django.shortcuts import render

def logistics_shipping(request):
    return render(request, 'logistics/logistics_shipping.html')  # or any appropriate template


# ---------- HOMEPAGE ----------
def home_view(request):
    return render(request, 'home.html')


# ---------- LOGIN VIEWS ----------
class CustomLoginView(LoginView):
    template_name = 'login.html'


class AdminLoginView(LoginView):
    template_name = 'admin_login.html'


# ---------- CUSTOMER VIEWS ----------
from .customer_views import (
    customer_list,
    customer_detail,
    customer_create,
    customer_update,
    customer_delete
)


# ---------- EMPLOYEE VIEWS ----------
from .employee_views import (
    employee_list,
    employee_detail,
    employee_create,
    employee_update,
    employee_delete
)


# ---------- SALES VIEWS ----------
from .sales_views import (
    sales_list,
    sales_detail,
    sales_create,
    sales_update,
    sales_delete
)


# ---------- INVENTORY VIEWS ----------
from .inventory_views import (
    inventory_list,
    inventory_detail,
    inventory_create,
    inventory_update,
    inventory_delete
)


# ---------- FORECAST VIEWS ----------
from .forecast_views import (
    forecast_dashboard,
)


# ---------- SUPPLIER VIEWS ----------
from .supplier_views import (
    supplier_list,
    supplier_detail,
    supplier_create,
    supplier_update,
    supplier_delete
)


# ---------- FINANCE VIEWS ----------
from .finance_views import (
    finance_list,
    finance_detail,
    finance_create,
    finance_update,
    finance_delete
)


# ---------- LOGISTICS VIEWS ----------
from .logistics_views import (
    logistics_list,
    logistics_detail,
    logistics_create,
    logistics_update,
    logistics_delete
)
