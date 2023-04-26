from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

# singal row fetch
def Student_details(request,pk):
    stu = Student.objects.get(id = pk)
    print(stu,'stu')
    ser = StudentSerializer(stu)
    print('ser',ser)
    print(ser.data,'data')
    json_data = JSONRenderer().render(ser.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')

# All Data Fetch
def Student_all(request):
    stu = Student.objects.all()
    print(stu,'stu')
    ser = StudentSerializer(stu, many=True)
    print('ser',ser)
    print(ser.data,'data')
    json_data = JSONRenderer().render(ser.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')