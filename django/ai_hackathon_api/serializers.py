from rest_framework import serializers
from .models import Company, CompanyReport, CompanyEmotions

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ['id', 'name', 'is_good', 'youtube_url']

class CompanyReportSerializer(serializers.ModelSerializer):
	company_name = serializers.ReadOnlyField(source='company.name')

	class Meta:
		model = CompanyReport
		fields = "__all__"

class CompanyEmotionsSerializer(serializers.ModelSerializer):
	company_name = serializers.ReadOnlyField(source='company.name')

	class Meta:
		model = CompanyEmotions
		fields = "__all__"