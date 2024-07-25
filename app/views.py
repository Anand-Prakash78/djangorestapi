from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers
    
    #make a route like cpmapny/{company_id}/employee
    @action(detail=True,methods =['get'])
    def employee(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(Company=company)
            emp_serializer=EmployeeSerializers(emps,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e :
            return Response("Some have occured.")
    
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    
