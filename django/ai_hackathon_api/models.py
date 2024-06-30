from django.db import models
from django.contrib.auth.models import User

# admin, business, user
class Role(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name
	
class SustainB3trUser(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	wallet = models.CharField(max_length=100, unique=True)
	role = models.ForeignKey(Role, on_delete=models.CASCADE)

	def __str__(self):
		return self.wallet
	
class Company(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class TaskType(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
	
class Task(models.Model):
	id = models.AutoField(primary_key=True)
	type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
	amount_b3tr = models.FloatField()
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

# Pending, Paid, Expired
class PostStatus(models.Model):
	id = models.AutoField(primary_key=True)
	status = models.CharField(max_length=50, unique=True, default='pending', editable=False)

	def __str__(self):
		return self.status
	
class Post(models.Model):
	id = models.AutoField(primary_key=True)
	latitude = models.FloatField()
	longitude = models.FloatField()
	title = models.TextField()
	img_bin = models.ImageField()
	img_waste = models.ImageField()
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	user = models.ForeignKey(SustainB3trUser, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	status = models.ForeignKey(PostStatus, on_delete=models.CASCADE)

	def __str__(self):
		return self.title