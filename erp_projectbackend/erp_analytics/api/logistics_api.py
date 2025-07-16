from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from erp_analytics.models.logistics import Shipment
from erp_analytics.serializers.logistic_serilizer import LogisticsSerializer
# pylint: disable=no-member

class LogisticsListAPI(APIView):
    def get(self, request):
        logistics = Shipment.objects.all().order_by('-dispatch_date')
        serializer = LogisticsSerializer(logistics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LogisticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogisticsDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Shipment.objects.get(pk=pk)
        except Shipment.DoesNotExist:
            return None

    def get(self, request, pk):
        logistics = self.get_object(pk)
        if not logistics:
            return Response({"error": "Logistics entry not found"}, status=404)
        serializer = LogisticsSerializer(logistics)
        return Response(serializer.data)

    def put(self, request, pk):
        logistics = self.get_object(pk)
        if not logistics:
            return Response({"error": "Logistics entry not found"}, status=404)
        serializer = LogisticsSerializer(logistics, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        logistics = self.get_object(pk)
        if not logistics:
            return Response({"error": "Logistics entry not found"}, status=404)
        logistics.delete()
        return Response({"message": "Logistics entry deleted"}, status=204)
