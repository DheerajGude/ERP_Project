from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from erp_analytics.models.sales import SalesOrder
from erp_analytics.serializers.sales_serializer import SaleSerializer
# pylint: disable=no-member


class SalesListAPI(APIView):
    def get(self, request):
        sales = SalesOrder.objects.all().order_by('-date')
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return SalesOrder.objects.get(pk=pk)
        except SalesOrder.DoesNotExist:
            return None

    def get(self, request, pk):
        sale = self.get_object(pk)
        if not sale:
            return Response({"error": "Sale not found"}, status=404)
        serializer = SaleSerializer(sale)
        return Response(serializer.data)

    def put(self, request, pk):
        sale = self.get_object(pk)
        if not sale:
            return Response({"error": "Sale not found"}, status=404)
        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        sale = self.get_object(pk)
        if not sale:
            return Response({"error": "Sale not found"}, status=404)
        sale.delete()
        return Response({"message": "Sale deleted"}, status=204)
