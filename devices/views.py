from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Device
from .serializers import DeviceSerializer

@api_view(['GET','POST'])
def device_list(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DeviceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Get, update, delete device its ID.
@api_view(['GET','PUT','DELETE'])
def device_detail(request,pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DeviceSerializer(device, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        device.delete()
        return Response({'device': 'Device deleted successfully'},status=status.HTTP_200_OK)



    