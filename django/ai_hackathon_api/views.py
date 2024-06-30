import json
import boto3
from django.shortcuts import render
from .models import Company, Role, SustainB3trUser, User, Post, Task, TaskType, PostStatus
from .serializers import CompanySerializer, RoleSerializer, UserSerializer
from wsgiref.util import FileWrapper
from django.http import HttpResponse, Http404, JsonResponse
import os
from django.core import serializers

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


def success_json(msg, data ={}):
     return {
          "message": msg,
          "data": data
          }

def fail_json(msg):
     return {
          "error": msg
          }

class CompanyViewSet(viewsets.ModelViewSet):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
    
class RoleViewSet(viewsets.ModelViewSet):
	queryset = Role.objects.all()
	serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = SustainB3trUser.objects.all()
	serializer_class = UserSerializer

class PostStatusView(APIView):
     def get(self, request, format=None):
        try:
          obj = PostStatus.objects.all()
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully retrieved PostStatus object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
     
     def post(self, request, *args, **kwargs):
        status = request.data['status']
        try:
          obj = PostStatus.objects.get_or_create(status=status)
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully retrieved PostStatus object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
     
     def delete(self, request, format=None):
        print("delete api call")
        # id = request.data['id']
        status = request.data['status']

        try:
          print("delete api call 2")
          obj = PostStatus.objects.get(status=status)
          obj.delete()
          return JsonResponse(success_json("Successfully deleted PostStatus object"), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
        
class CompaniesView(APIView):
     def get(self, request, format=None):
        company_type = request.GET.get('type', '')
        try:
             if not company_type:
               companies = Company.objects.all().values()
               return JsonResponse(success_json("Successfully Got Companies", list(companies)), status=200)
             elif company_type == 'good':
               companies = Company.objects.filter(is_good=True).all().values()
               return JsonResponse(success_json("Successfully Got Companies", list(companies)), status=200)
             elif company_type == 'bad':
               companies = Company.objects.filter(is_good=False).all().values()
               return JsonResponse(success_json("Successfully Got Companies", list(companies)), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)

        return JsonResponse(success_json("Successfully updated Company object"), status=200)

class TaskTypeView(APIView):
     def get(self, request, format=None):
        try:
          obj = TaskType.objects.all()
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully retrieved Role object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
     
     def post(self, request, *args, **kwargs):
        name = request.data['name']
        try:
          obj = TaskType.objects.get_or_create(name=name)
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully retrieved Role object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
        
class RolesView(APIView):
     def get(self, request, format=None):
        try:
          obj = Role.objects.all()
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully retrieved Role object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)

class TaskView(APIView):
     def get(self, request, format=None):
        name = request.GET.get('name', '')
        try:
          if name:
              obj = Task.objects.get(name=name)
          else:
              obj = Task.objects.all()
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
        
        data = serializers.serialize('json', obj)
        return JsonResponse(success_json("Successfully retrieved Task object", data), status=200)
     
     def post(self, request, *args, **kwargs):
        type = request.data['type']
        amount_b3tr = request.data['amount_b3tr']
        company = request.data['company']

        if not type:
             return JsonResponse("Missing name POST param!", status=404)
        try:
             task_type = TaskType.objects.get(name=type)
             co_obj = Company.objects.get(name=company)

             obj = Task.objects.get_or_create(amount_b3tr=amount_b3tr, type=task_type, company=co_obj)
        except Role.DoesNotExist as e:
             print("RoleView:")
             return JsonResponse(fail_json(str(e)), status=404)
     
        return JsonResponse(success_json("Successfully updated Role object"), status=200)
     
class RoleView(APIView):
     def get(self, request, format=None):
        name = request.GET.get('name', '')
        try:
          if name:
              obj = Role.objects.get(name=name)
          else:
              obj = Role.objects.all()
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
        
        data = serializers.serialize('json', obj)
        return JsonResponse(success_json("Successfully retrieved Role object", data), status=200)
     
     def post(self, request, *args, **kwargs):
        name = request.data['name']

        if not name:
             return JsonResponse("Missing name POST param!", status=404)
        try:
             obj = Role.objects.get_or_create(name=name)
        except Role.DoesNotExist as e:
             print("RoleView:")
             return JsonResponse(fail_json(str(e)), status=404)
     
        return JsonResponse(success_json("Successfully updated Role object"), status=200)

class UsersView(APIView):
     def get(self, request, format=None):
        try:
          obj = SustainB3trUser.objects.all()
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully got the User object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)

class UserView(APIView):
     def get(self, request, format=None):
        wallet = request.GET.get('wallet', '')
        try:
             if wallet:
               print("wallet " + wallet)
               obj = SustainB3trUser.objects.get(wallet=wallet)
               data = serializers.serialize('json', obj)

               return JsonResponse(success_json("Successfully got the User object", data), status=200)
             else: 
               obj = SustainB3trUser.objects.all()
               data = serializers.serialize('json', obj)

               return JsonResponse(success_json("Successfully got the User object", data), status=200)
              
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
     
     def post(self, request, *args, **kwargs):
        wallet = request.data['wallet']
        username = request.data['username']
        password1 = request.data['password1']
        password2 = request.data['password2']
        role = request.data['role']
        if password1 != password2:
            return JsonResponse("Passwords don't match in POST params!", status=404)
        if not wallet:
            return JsonResponse("Missing wallet POST param!", status=404)

        try:
          role_obj = Role.objects.get(name=role)
          obj = SustainB3trUser.objects.get(wallet=wallet)
          obj.username = username
          obj.password1 = password1
          obj.role = role_obj
          obj.save()
        except SustainB3trUser.DoesNotExist as e:
          print("UserView post:")
          new_obj = SustainB3trUser.objects.create(wallet=wallet, username=username,password=password1,role=role_obj)
          print(new_obj.wallet)
          return JsonResponse(fail_json(str(e)), status=404)
     
        return JsonResponse(success_json("Successfully updated User object"), status=200)

class PostsView(APIView):
     def get(self, request, format=None):
        try:
          obj = Post.objects.all()
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully retrieved Post object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)

class PostView(APIView):
     def get(self, request, format=None):
        try:
          obj = Post.objects.get()
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully retrieved Post object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
        
     def post(self, request, *args, **kwargs):
        title = request.data['title']
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        img_bin = request.data['img_bin']
        img_waste = request.data['img_waste']
        task_id = request.data['task_id']
        wallet = request.data['wallet']
        company = request.data['company'] 

        try:
          co_obj = Company.objects.get(name=company)
        except Company.DoesNotExist as e:
          print("PostView post:")
          return JsonResponse(fail_json(str(e)), status=404)
        
        try:
          user_obj = SustainB3trUser.objects.get(wallet=wallet)
        except SustainB3trUser.DoesNotExist as e:
          print("PostView post:")
          return JsonResponse(fail_json(str(e)), status=404)
        
        try:
          task_obj = Task.objects.get(id=task_id)
        except Task.DoesNotExist as e:
          print("PostView post:")
          return JsonResponse(fail_json(str(e)), status=404)
        
        try:
          obj = Post.objects.create(
               title=title, 
               latitude=latitude,
               longitude=longitude,
               img_bin=img_bin,
               img_waste=img_waste,
               task_id=task_obj,
               user_id=user_obj, 
               company=co_obj
          )
        
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully posted Post object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
              
class CompanyView(APIView):
     def get(self, request, format=None):
        try:
          obj = Company.objects.all()
          data = serializers.serialize('json', obj)
          return JsonResponse(success_json("Successfully retrieved Company object", data), status=200)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
        
     def post(self, request, format=None):
        company_name = request.data['companyName']

        if not (company_name):
             return JsonResponse("companyName is required GET param!")
        
        try:
             obj = Company.objects.get(name=company_name)
             return JsonResponse(success_json("Company object already exists"), status=200)
        except Exception as e:
             obj = Company.objects.create(name=company_name)
             return JsonResponse(success_json("Created the Company object"), status=200)

        return JsonResponse(success_json("Successfully updated Company object"), status=200)
     
     def put(self, request, format=None):
        company_name = request.GET.get('companyName', '')
        youtube_url = request.GET.get('youtubeUrl', '')

        if not (company_name and youtube_url):
             return JsonResponse("companyName and youtubeUrl are required GET param!")
        
        try:
             obj = Company.objects.get(name=company_name)
             obj.youtube_url = youtube_url
             obj.save()
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)

        return JsonResponse(success_json("Successfully updated Company object"), status=200)

# aws bucket
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        file_url = handle_file_upload(file)
        return Response({'file_url': file_url})

def handle_file_upload(file):
    import boto3
    s3 = boto3.client('s3')
    bucket_name = 'carbonsustain-bucket-sustainability-reports'
    file_key = f'media/{file.name}'

    s3.upload_fileobj(file, bucket_name, file_key)
    file_url = f'https://{bucket_name}.s3.amazonaws.com/{file_key}'
    return file_url