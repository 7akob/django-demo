from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Heater
from .serializers import HeaterSerializer

@api_view(['GET'])
def list_headers(request):
    heaters = Heater.objects.all()
    serializer = HeaterSerializer(heaters, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_heater(request):
    serializer = HeaterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def compute_loss(request):
    temp = request.data.get("temperature", 0)
    pressure = request.data.get("pressure", 0)

    # Dummy physics
    loss = temp *0.1 - pressure * 0.05

    return Response({"thermal_loss": loss})