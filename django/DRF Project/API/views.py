import io
from django.shortcuts import render
from django.views import View
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Class Base Views
# class Student_api(APIView):
#     def get(self, request, pk=None, format=None):
#         # id = request.data.get('id')
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(id = id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     def put(self, request, pk, format=None):
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated!!'}, status=status.HTTP_205_RESET_CONTENT)
#         return Response(serializer.errors)
    
    
#     def patch(self, request, pk, format=None):
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, partial=True, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated!!'}, status=status.HTTP_206_PARTIAL_CONTENT)
#         return Response(serializer.errors)
    
        
#     def delete(self, requset, pk, format=None):
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted!!!!'})

# Function Base View
@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def Student_Api(request,pk = None):
    if request.method == 'GET': 
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated!!'}, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated!!'}, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted!!!!'})


# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello Wprld'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'This Is Post'})

# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({'msg':'This Is Get Request'})
    
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'This Is Post Request','data':request.data})

# @api_view(['PUT'])
# def hello_world(request):
#     if request.method == 'PUT':
#         print(request.data)
#         return Response({'msg':'This Is Put Request'})

# Class Base View
# @method_decorator(csrf_exempt, name='dispatch')
# class StudentAPI(View):
#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Your Data Save'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#             # return JsonResponse(res, safe=False)
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id = id)
#         # Id's All Data Updated In Databse
#         serializer = StudentSerializer(stu, data=pythondata)
#         # Id's specific data Updated In Databse
#         serializer = StudentSerializer(stu, data=pythondata, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Your Data Updated'}
#             # json_data = JSONRenderer().render(res)
#             # return HttpResponse(json_data, content_type='application/json')
#             return JsonResponse(res, safe=False)
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res = {'msg': 'Your Data Deleted'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res, safe=False)

# Function Base View
# Create your views here.

# singal row fetch
# def Student_details(request,pk):
#     stu = Student.objects.get(id = pk)
#     print(stu,'stu')
#     ser = StudentSerializer(stu)
#     # print('ser',ser)
#     # print(ser.data,'data')
#     # json_data = JSONRenderer().render(ser.data)
#     # print(json_data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(ser.data,safe=False)

# # All Data Fetch
# def Student_all(request):
#     stu = Student.objects.all()
#     print(stu,'stu')
#     ser = StudentSerializer(stu, many=True)
#     # print('ser',ser)
#     # print(ser.data,'data')
#     # json_data = JSONRenderer().render(ser.data)
#     # print(json_data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(ser.data,safe=False)

# Create Data

# @csrf_exempt
# def student_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         print(json_data,'json_data')
#         stream = io.BytesIO(json_data)
#         print('stream',stream)
#         pythondata = JSONParser().parse(stream)
#         print(pythondata,'python')
#         serializer = StudentSerializer(data=pythondata)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             # res = {'msg': 'Your Data Save'}
#             # json_data = JSONRenderer().render(res)
#             # print(json_data)
#             # return HttpResponse(json_data, content_type='application/json')
#             return JsonResponse(serializer.data, safe=False)
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

# Fetch Data From Database
# @csrf_exempt
# def student_create(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

#     # Create Data    
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Your Data Save'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#             # return JsonResponse(res, safe=False)
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')

#     # Update Date On Database
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id = id)
#         # Id's All Data Updated In Databse
#         serializer = StudentSerializer(stu, data=pythondata)
#         # Id's specific data Updated In Databse
#         serializer = StudentSerializer(stu, data=pythondata, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Your Data Updated'}
#             # json_data = JSONRenderer().render(res)
#             # return HttpResponse(json_data, content_type='application/json')
#             return JsonResponse(res, safe=False)
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res = {'msg': 'Your Data Deteled'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res, safe=False)