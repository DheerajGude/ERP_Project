from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from erp_analytics.models.finance import Transaction
from erp_analytics.serializers.finance_serializer import FinanceSerializer
# pylint: disable=no-member

class FinanceListAPI(APIView):
    def get(self, request):
        finances = Transaction.objects.all().order_by('-date')
        serializer = FinanceSerializer(finances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FinanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinanceDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return None

    def get(self, request, pk):
        finance = self.get_object(pk)
        if not finance:
            return Response({"error": "Finance record not found"}, status=404)
        serializer = FinanceSerializer(finance)
        return Response(serializer.data)

    def put(self, request, pk):
        finance = self.get_object(pk)
        if not finance:
            return Response({"error": "Finance record not found"}, status=404)
        serializer = FinanceSerializer(finance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        finance = self.get_object(pk)
        if not finance:
            return Response({"error": "Finance record not found"}, status=404)
        finance.delete()
        return Response({"message": "Finance record deleted"}, status=204)
