from django.shortcuts import render, redirect
from django.contrib import messages

from erp_analytics.forms.forecast_form import ForecastForm

# pylint: disable=unused-argument

def forecast_overview(request):
    return render(request, 'forecast/overview.html')  # Create this template if needed

def forecast_dashboard(request):
    form = ForecastForm()
    forecast_data = []
    chart_labels = []
    chart_values = []

    if request.method == 'POST':
        form = ForecastForm(request.POST)
        if form.is_valid():
            try:
                category = form.cleaned_data['category']
                period = form.cleaned_data['period']
                forecast_data = ForecastForm(category, period)

                if forecast_data:
                    chart_labels = [entry['month'] for entry in forecast_data]
                    chart_values = [entry['predicted_value'] for entry in forecast_data]
                else:
                    messages.warning(request, "No forecast data available for selected criteria.")

            except Exception as e:
                messages.error(request, f"Error during forecasting: {str(e)}")
        else:
            messages.error(request, "Invalid input. Please check the form.")

    context = {
        'form': form,
        'forecast_data': forecast_data,
        'chart_labels': chart_labels,
        'chart_values': chart_values,
    }
    return render(request, 'erp_analytics/forecast_dashboard.html', context)
