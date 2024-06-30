from django.contrib import admin
from .models import Company, CompanyReport, CompanyEmotions

admin.site.register(Company)
admin.site.register(CompanyReport)
admin.site.register(CompanyEmotions)