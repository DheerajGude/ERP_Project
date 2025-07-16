from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from erp_analytics.models.finance import Transaction
from erp_analytics.forms.finance_form import FinanceForm
# pylint: disable=no-member
# pylint: disable=unused-argument

# ✅ List all finance records
def finance_list(request):
    finances = Transaction.objects.all().order_by('-date')
    total_income = sum(f.amount for f in finances if f.transaction_type == 'Income')
    total_expense = sum(f.amount for f in finances if f.transaction_type == 'Expense')
    balance = total_income - total_expense

    context = {
        'finances': finances,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'erp_analytics/finance_list.html', context)


# ✅ Finance detail view
def finance_detail(request, pk):
    finance = get_object_or_404(Transaction, pk=pk)
    return render(request, 'erp_analytics/finance_detail.html', {'finance': finance})


# ✅ Create finance record
def finance_create(request):
    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction recorded.")
            return redirect('finance_list')
    else:
        form = FinanceForm()
    return render(request, 'erp_analytics/finance_form.html', {'form': form})


# ✅ Update finance record
def finance_update(request, pk):
    finance = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = FinanceForm(request.POST, instance=finance)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction updated.")
            return redirect('finance_detail', pk=pk)
    else:
        form = FinanceForm(instance=finance)
    return render(request, 'erp_analytics/finance_form.html', {'form': form})


# ✅ Delete transaction
def finance_delete(request, pk):
    finance = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        finance.delete()
        messages.success(request, "Transaction deleted.")
        return redirect('finance_list')
    return render(request, 'erp_analytics/finance_confirm_delete.html', {'finance': finance})
