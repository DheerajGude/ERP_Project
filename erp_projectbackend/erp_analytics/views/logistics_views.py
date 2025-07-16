from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from erp_analytics.models.logistics import DeliveryStatus ,Employee,Shipment,Vehicle
from erp_analytics.forms.logistics_forms import LogisticsForm
# pylint: disable=no-member
# pylint: disable=unused-argument

# ✅ List all logistics/shipments
def logistics_list(request):
    logistics_entries = DeliveryStatus.objects.all().order_by('-dispatch_date')
    total_shipments = logistics_entries.count()
    delayed_shipments = logistics_entries.filter(status='Delayed').count()

    return render(request, 'erp_analytics/logistics/list.html', {
        'logistics_entries': logistics_entries,
        'total_shipments': total_shipments,
        'delayed_shipments': delayed_shipments,
    })


# ✅ View details of a logistics record
def logistics_detail(request, pk):
    entry = get_object_or_404(DeliveryStatus, pk=pk)
    return render(request, 'erp_analytics/logistics/detail.html', {'entry': entry})


# ✅ Create a new logistics record
def logistics_create(request):
    if request.method == 'POST':
        form = LogisticsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Logistics entry created successfully.")
            return redirect('logistics_list')
        else:
            messages.error(request, "Form submission failed. Please check fields.")
    else:
        form = LogisticsForm()
    return render(request, 'erp_analytics/logistics/create.html', {'form': form})


# ✅ Update an existing logistics record
def logistics_update(request, pk):
    entry = get_object_or_404(DeliveryStatus, pk=pk)
    if request.method == 'POST':
        form = LogisticsForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Logistics entry updated.")
            return redirect('logistics_detail', pk=pk)
        else:
            messages.error(request, "Update failed. Please fix the errors.")
    else:
        form = LogisticsForm(instance=entry)
    return render(request, 'erp_analytics/logistics/edit.html', {'form': form})


# ✅ Delete a logistics record
def logistics_delete(request, pk):
    entry = get_object_or_404(DeliveryStatus, pk=pk)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, "Logistics entry deleted.")
        return redirect('logistics_list')
    return render(request, 'erp_analytics/logistics/confirm_delete.html', {'entry': entry})
