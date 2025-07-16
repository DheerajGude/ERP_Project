from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from erp_analytics.models.sales import SalesOrder
from erp_analytics.forms.sales_form import SaleForm
# pylint: disable=no-member
# pylint: disable=unused-argument

# ✅ List all sales records
from django.shortcuts import render
from erp_analytics.models.sales import Sales
 # or wherever your Sales model is

def sales_list(request):
    sales_data = Sales.objects.all()
    return render(request, 'erp_analytics/sales/list.html', {
        'sales': sales_data
    })


# ✅ View individual sale detail
def sales_detail(request, pk):
    sale = get_object_or_404(SalesOrder, pk=pk)
    return render(request, 'erp_analytics/sales/detail.html', {'sale': sale})


# ✅ Create a new sale entry
def sales_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sale record created successfully.")
            return redirect('sales_list')
        else:
            messages.error(request, "Error creating sale record.")
    else:
        form = SaleForm()
    return render(request, 'erp_analytics/sales/create.html', {'form': form})


# ✅ Update an existing sale entry
def sales_update(request, pk):
    sale = get_object_or_404(SalesOrder, pk=pk)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            messages.success(request, "Sale record updated.")
            return redirect('sales_detail', pk=pk)
        else:
            messages.error(request, "Update failed. Please correct the errors.")
    else:
        form = SaleForm(instance=sale)
    return render(request, 'erp_analytics/sales/edit.html', {'form': form})


# ✅ Delete a sale record
def sales_delete(request, pk):
    sale = get_object_or_404(SalesOrder, pk=pk)
    if request.method == 'POST':
        sale.delete()
        messages.success(request, "Sale record deleted.")
        return redirect('sales_list')
    return render(request, 'erp_analytics/sales/confirm_delete.html', {'sale': sale})
