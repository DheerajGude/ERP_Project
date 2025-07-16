# pylint: disable=unused-argument, no-member
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from erp_analytics.models.employee import Employee, Role, Department
# pylint: disable=unused-argument

@csrf_exempt
def employee_list(request):
    if request.method == "GET":
        name = request.GET.get('name', '')
        employees = Employee.objects.all()
        if name:
            employees = employees.filter(name__icontains=name)

        data = list(employees.values())
        return JsonResponse(data, safe=False)

@csrf_exempt
def employee_create(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Fetch related objects (if foreign keys)
            role = get_object_or_404(Role, id=data.get("role"))
            department = get_object_or_404(Department, id=data.get("department"))

            employee = Employee.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                phone=data.get("phone"),
                role=role,
                department=department,
                doj=data.get("doj"),
                is_active=data.get("is_active", True),
                photo=data.get("photo")
            )
            return JsonResponse({"message": "Employee created", "id": employee.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(id=pk)

        if request.method == "GET":
            return JsonResponse({
                "id": employee.id,
                "name": employee.name,
                "email": employee.email,
                "phone": employee.phone,
                "role": employee.role.id if employee.role else None,
                "department": employee.department.id if employee.department else None,
                "doj": str(employee.doj),
                "photo": employee.photo,
                "is_active": employee.is_active
            })

    except ObjectDoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def employee_update(request, pk):
    try:
        employee = Employee.objects.get(id=pk)

        if request.method == "PUT":
            data = json.loads(request.body)

            employee.name = data.get("name", employee.name)
            employee.email = data.get("email", employee.email)
            employee.phone = data.get("phone", employee.phone)

            # Safely get Role and Department if provided
            if data.get("role"):
                employee.role = get_object_or_404(Role, id=data.get("role"))
            if data.get("department"):
                employee.department = get_object_or_404(Department, id=data.get("department"))

            employee.doj = data.get("doj", employee.doj)
            employee.photo = data.get("photo", employee.photo)
            employee.is_active = data.get("is_active", employee.is_active)
            employee.save()

            return JsonResponse({"message": "Employee updated"})

    except ObjectDoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def employee_delete(request, pk):
    try:
        employee = Employee.objects.get(id=pk)

        if request.method == "DELETE":
            employee.delete()
            return JsonResponse({"message": "Employee deleted"})

    except ObjectDoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
