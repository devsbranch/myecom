from django.shortcuts import render
from django.http import HttpResponse
from .models import Iteam,Category
from .serializers import IteamSerializers,CategorySerializers

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def iteamCreate(request):
    serializer = IteamSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def iteamUpdate(request, pk):
    itm = Iteam.objects.get(id=pk)
    serializer = IteamSerializers(instance=itm, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def iteamlist(request):
    itm = Iteam.objects.all()
    serializer = IteamSerializers(itm, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def iteamDetails(request, pk):
    itm = Iteam.objects.get(id=pk)
    serializer = IteamSerializers(itm, many=False)
    return Response(serializer.data)


@api_view(['GET','DELETE'])
def iteamdelate(request, pk):
    itm = Iteam.objects.get(id=pk)
    itm.delete()

    return Response('iteam deleted')

@api_view(['POST'])
def addcategory(request):
    serializer=CategorySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data)

@api_view(['DELETE'])
def removecategory(request, pk):
    cat=Category.objects.get(id=pk)
    cat.delete()

    return  Response('category deleted')

