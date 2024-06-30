from rest_framework import serializers
from .models import Company, Role, SustainB3trUser, TaskType, PostStatus

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ['id', 'name']

class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Role
		fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = SustainB3trUser
		fields = ['id', 'username', 'password', 'wallet', 'role']

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ['id', 'name']

class TaskTypeViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskType
		fields = ['id', 'name']

class PostStatusViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostStatus
		fields = ['id', 'status']
		
		