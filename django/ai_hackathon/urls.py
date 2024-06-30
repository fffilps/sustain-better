"""
URL configuration for ai_hackathon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from ai_hackathon import settings
from rest_framework.routers import DefaultRouter
from ai_hackathon_api.views import CompanyViewSet, GenerateCompanyReportView, CompanyReportViewSet, CompanyReportView, CompanyEmotionsViewSet, FormatCompanyEmotionsView, CompanyView, GenerateCompanyEmotionsView, CompaniesView, FileUploadView
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'companyReportViewSet', CompanyReportViewSet)
router.register(r'companyEmotionsViewSet', CompanyEmotionsViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include((router.urls, 'ai_hackathon_api'), namespace='ai_hackathon_api')),
    path('api/companies', CompaniesView.as_view(), name='ai_hackathon_api'),
    path('api/generateCompanyReport', GenerateCompanyReportView.as_view(), name='ai_hackathon_api'),
    path('api/generateEmotions', GenerateCompanyEmotionsView.as_view(), name='ai_hackathon_api'),
    path('api/companyReport', CompanyReportView.as_view(), name='ai_hackathon_api'),
    path('api/formatCompanyEmotions', FormatCompanyEmotionsView.as_view(), name='ai_hackathon_api'),
    path('api/company', CompanyView.as_view(), name='ai_hackathon_api'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)