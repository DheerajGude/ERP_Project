from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from erp_analytics.models.supplier import Supplier
from erp_analytics.serializers.supplier_serializer import SupplierSerializer
# pylint: disable=no-member

class SupplierListAPI(APIView):
    def get(self, request):
        suppliers = Supplier.objects.all().order_by('name')
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return None

    def get(self, request, pk):
        supplier = self.get_object(pk)
        if not supplier:
            return Response({"error": "Supplier not found"}, status=404)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    def put(self, request, pk):
        supplier = self.get_object(pk)
        if not supplier:
            return Response({"error": "Supplier not found"}, status=404)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        supplier = self.get_object(pk)
        if not supplier:
            return Response({"error": "Supplier not found"}, status=404)
        supplier.delete()
        return Response({"message": "Supplier deleted"}, status=204)
