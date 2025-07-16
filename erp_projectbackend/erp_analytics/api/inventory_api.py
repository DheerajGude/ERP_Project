from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from erp_analytics.models.inventory import Stock
from erp_analytics.serializers.inventory_serializer import InventoryItemSerializer
# pylint: disable=no-member

class InventoryListAPI(APIView):
    def get(self, request):
        items = Stock.objects.all().order_by('name')
        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            return None

    def get(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({"error": "Inventory item not found"}, status=404)
        serializer = InventoryItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({"error": "Inventory item not found"}, status=404)
        serializer = InventoryItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({"error": "Inventory item not found"}, status=404)
        item.delete()
        return Response({"message": "Inventory item deleted"}, status=204)
