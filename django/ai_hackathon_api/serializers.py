from rest_framework import serializers
from .models import Company, Role, SustainB3trUser, TaskType, PostStatus, Post, PostAIStats

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
		
class PostViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['id', 'latitude', 'longitude', 'title', 'img_bin', 'img_waste', 'postAIStats', 'task', 'user', 'company', 'status']

class PostAIStatsViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostAIStats
		fields = ['id', 'img_bin_color', 'img_bin_area', 'img_waste_prob', 'img_waste_classify']
