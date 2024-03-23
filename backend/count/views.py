from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.


class CountDetails(APIView):

    def get(self, request):
        try:
            total = TotalCount.objects.get(id=1)
            return Response(str(total.total), status=status.HTTP_200_OK)
        except TotalCount.DoesNotExist:
            return Response(0, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            data = request.data
            count = Count.objects.create(number=data)
            total, created = TotalCount.objects.get_or_create(id=1)
            total.numbers.add(count)
            total.save()
            return Response(str(total.total), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
