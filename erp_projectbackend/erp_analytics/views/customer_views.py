# views/customer_views.py

# pylint: disable=unused-argument

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from erp_analytics.models.customer import Customer
from erp_analytics.forms.customer_form import CustomerForm
import json
# pylint: disable=no-member

# ✅ API View (GET list / POST create)
@csrf_exempt
def customer_list(request):
    if request.method == "GET":
        name = request.GET.get('name', '')
        customers = Customer.objects.all()
        if name:
            customers = customers.filter(name__icontains=name)
        data = list(customers.values())
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            customer = Customer.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                phone=data.get("phone"),
                address=data.get("address"),
                created_at=data.get("created_at")  # optional
            )
            return JsonResponse({"message": "Customer added", "id": customer.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

# ✅ API View (GET/PUT/DELETE detail)
@csrf_exempt
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(id=pk)

        if request.method == "GET":
            return JsonResponse({
                "id": customer.id,
                "name": customer.name,
                "email": customer.email,
                "phone": customer.phone,
                "address": customer.address,
                "created_at": str(customer.created_at)
            })

        elif request.method == "PUT":
            data = json.loads(request.body)
            customer.name = data.get("name", customer.name)
            customer.email = data.get("email", customer.email)
            customer.phone = data.get("phone", customer.phone)
            customer.address = data.get("address", customer.address)
            customer.save()
            return JsonResponse({"message": "Customer updated"})

        elif request.method == "DELETE":
            customer.delete()
            return JsonResponse({"message": "Customer deleted"})

    except ObjectDoesNotExist:
        return JsonResponse({"error": "Customer not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

# ✅ HTML Form View – Create
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form': form})

# ✅ HTML Form View – Update
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_form.html', {'form': form})

# ✅ HTML Form View – Delete
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})
