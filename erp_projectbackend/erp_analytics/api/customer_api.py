from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from erp_analytics.models.customer import Customer
from erp_analytics.serializers.customer_serializer import CustomerSerializer
# pylint: disable=no-member

class CustomerListAPI(APIView):
    def get(self, request):
        customers = Customer.objects.all().order_by('-created_at')
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return None

    def get(self, request, pk):
        customer = self.get_object(pk)
        if not customer:
            return Response({"error": "Customer not found"}, status=404)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        if not customer:
            return Response({"error": "Customer not found"}, status=404)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        if not customer:
            return Response({"error": "Customer not found"}, status=404)
        customer.delete()
        return Response({"message": "Customer deleted"}, status=204)
