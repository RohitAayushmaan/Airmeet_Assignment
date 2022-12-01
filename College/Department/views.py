from django.shortcuts import render
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from .models import student
from .serializers import studentSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.

class studentList(APIView):
    def get(self,request):
        student1=student.objects.all()

        serializer=studentSerializer(student1,many=True)
        filter_backends = [filters.SearchFilter]
        filter_fields=('accountNumber')
        search_fields = ('accountNumber')

        return Response(serializer.data)



    def post(self):
        pass

