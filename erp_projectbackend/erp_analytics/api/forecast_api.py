from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# pylint: disable=no-member
from erp_analytics.models.forecast import Forecast , ForecastType
from erp_analytics.serializers.forecast_serializer import ForecastSerializer


class ForecastAPIView(APIView):
    def post(self, request):
        category = request.data.get('category')
        period = request.data.get('period')

        if not category or not period:
            return Response({"error": "Category and period are required."}, status=400)

        try:
            forecast_data = Forecast(category, int(period))

            # Save forecast to DB
            created_forecasts = []
            for entry in forecast_instance:
                forecast_instance = Forecast.objects.create(
                    category=category,
                    month=entry['month'],
                    predicted_value=entry['predicted_value']
                )
                created_forecasts.append(forecast_instance)

            serializer = ForecastSerializer(created_forecasts, many=True)
            return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

    def get(self, request):
        forecasts = Forecast.objects.all().order_by('-month')
        serializer = ForecastSerializer(forecasts, many=True)
        return Response(serializer.data)
