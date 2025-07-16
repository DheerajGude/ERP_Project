from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from erp_analytics.models.inventory import Stock
from erp_analytics.forms.inventory_form import InventoryItemForm
# pylint: disable=no-member
# pylint: disable=unused-argument

# ✅ List all inventory items
def inventory_list(request):
    items = Stock.objects.all().order_by('name')
    total_items = items.count()
    low_stock_items = items.filter(quantity__lte=10).count()  # example threshold

    return render(request, 'erp_analytics/inventory/list.html', {
        'items': items,
        'total_items': total_items,
        'low_stock_items': low_stock_items,
    })


# ✅ Inventory item detail view
def inventory_detail(request, pk):
    item = get_object_or_404(Stock, pk=pk)
    return render(request, 'erp_analytics/inventory/detail.html', {'item': item})


# ✅ Create new inventory item
def inventory_create(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inventory item added successfully.")
            return redirect('inventory_list')
        else:
            messages.error(request, "Error in form. Please correct and try again.")
    else:
        form = InventoryItemForm()
    return render(request, 'erp_analytics/inventory/create.html', {'form': form})


# ✅ Update inventory item
def inventory_update(request, pk):
    item = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Inventory item updated successfully.")
            return redirect('inventory_detail', pk=pk)
        else:
            messages.error(request, "Form submission error.")
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'erp_analytics/inventory/edit.html', {'form': form})


# ✅ Delete inventory item
def inventory_delete(request, pk):
    item = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Inventory item deleted successfully.")
        return redirect('inventory_list')
    return render(request, 'erp_analytics/inventory/confirm_delete.html', {'item': item})
