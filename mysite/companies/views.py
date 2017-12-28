from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import Stockserializer

class StockList(APIView):
    def get(self,request):
        stocks = Stock.objects.all()
        serializer = Stockserializer(stocks,many=True)
        return Response(serializer.data)
        pass
    def post(self):
        pass
