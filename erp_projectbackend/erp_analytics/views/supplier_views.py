# pyright: reportGeneralTypeIssues=false
# pylint: disable=no-member
# pylint: disable=unused-argument
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from erp_analytics.models.supplier import Supplier
from erp_analytics.forms.supplier_forms import SupplierForm



# ✅ View all suppliers
def supplier_list(request):
    suppliers = Supplier.objects.all().order_by('name')
    return render(request, 'erp_analytics/supplier/list.html', {
        'suppliers': suppliers,
    })


# ✅ View supplier details
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'erp_analytics/supplier/detail.html', {'supplier': supplier})


# ✅ Add a new supplier
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier added successfully.")
            return redirect('supplier_list')
        else:
            messages.error(request, "Error adding supplier. Please correct the form.")
    else:
        form = SupplierForm()
    return render(request, 'erp_analytics/supplier/create.html', {'form': form})


# ✅ Edit supplier information
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier updated successfully.")
            return redirect('supplier_detail', pk=pk)
        else:
            messages.error(request, "Error updating supplier.")
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'erp_analytics/supplier/edit.html', {'form': form})


# ✅ Delete supplier
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, "Supplier removed successfully.")
        return redirect('supplier_list')
    return render(request, 'erp_analytics/supplier/confirm_delete.html', {'supplier': supplier})
