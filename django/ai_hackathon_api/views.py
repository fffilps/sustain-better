import json
import boto3
from django.shortcuts import render

from .emotions_json_formatter import EmotionsUploader
from .aws_sdxl import SDXL

from .models import Company, CompanyReport, CompanyEmotions
from .serializers import CompanySerializer, CompanyReportSerializer, CompanyEmotionsSerializer
from .sustainability_report_downloader import SustainabilityReportDownloader
from wsgiref.util import FileWrapper
from django.http import HttpResponse, Http404, JsonResponse
import os
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

class CompanyReportViewSet(viewsets.ModelViewSet):
	queryset = CompanyReport.objects.all()
	serializer_class = CompanyReportSerializer

class CompanyEmotionsViewSet(viewsets.ModelViewSet):
	queryset = CompanyEmotions.objects.all()
	serializer_class = CompanyEmotionsSerializer

class GenerateCompanyEmotionsView(APIView):
    def put(self, request, format=None):
        company_name = request.GET.get('companyName', '')
        report_year = request.GET.get('reportYear', '')
        if not (company_name):
             return JsonResponse("companyName is a required PUT param!")
        
        try:
             company_obj = Company.objects.get(name=company_name)

             emotions = CompanyEmotions.objects.filter(company=company_obj)
             for emotion in emotions:
                  sdxl = SDXL(emotion.emotions, company_name, report_year)
                  img_bytes = sdxl.get_bytes()
                  sdxl.save_image(img_bytes)
                  
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)

        return JsonResponse(success_json("Successfully updated CompanyEmotions object"), status=200)

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

     
class CompanyView(APIView):
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

class FormatCompanyEmotionsView(APIView):
     def get(self, request, format=None):
        company_name = request.GET.get('companyName', '')

        if not company_name:
             return JsonResponse("Missing companyName GET param!")
        
        company_emotions = EmotionsUploader()
        company_emotions.walk_dir()

        return JsonResponse(success_json("Successfully formatted Company emotions"), status=200)
     
class GenerateCompanyReportView(APIView):
    def get(self, request, format=None):
        company_name = request.GET.get('companyName', '')

        if not company_name:
             return JsonResponse("Missing companyName GET param!")
        
        report_downloader = SustainabilityReportDownloader(company_name)
        report_downloader.call_company_api()


        return JsonResponse(success_json("Successfully generated Company reports"), status=200)

class CompanyReportView(APIView):
    def get_company(self, company_name):
        try:
            return Company.objects.get(name=company_name)
        except Company.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        report_url = request.GET.get('reportUrl', '')

        if not report_url:
             return JsonResponse("Missing reportUrl GET param!", status=404)
        
        short_report = open(report_url, 'rb')
        response = HttpResponse(FileWrapper(short_report), content_type='application/pdf')
        return response
        
    def delete(self, request, format=None):
        company_name = request.GET.get('companyName', '')

        if not (company_name):
             return JsonResponse(success_json("companyName is a required GET param!"), status=404)
        
        try:
            company_obj = self.get_company(company_name)
            reports = CompanyReport.objects.filter(company=company_obj)
            if len(reports) > 0:
                for report in reports:
                    print("deleting report " + str(report.year))
                    report.delete()
                msg = "Successfully deleted reports for: " + company_name
                return JsonResponse(success_json(msg), status=204)
        except Exception as e:
             return JsonResponse(fail_json(str(e)), status=404)
        
        return JsonResponse(fail_json("Delete was not successfully, probably didn't exist"), status=404)
    
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