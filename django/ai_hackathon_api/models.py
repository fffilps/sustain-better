from django.db import models

# Create your models here.
class Company(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	youtube_url = models.CharField(max_length=200, default="")
	is_good = models.BooleanField()

	def __str__(self):
		return self.name

class CompanyReport(models.Model):
	id = models.AutoField(primary_key=True)
	year = models.IntegerField()
	pdf = models.FileField()
	pdf_name = models.CharField(default="",max_length=200)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('year', 'company',)

	def __str__(self):
		return self.company.name + " " + self.year

# Create your models here.
class CompanyEmotions(models.Model):
	id = models.AutoField(primary_key=True)
	year = models.IntegerField()
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	emotions = models.JSONField()
	ai_gen_path = models.CharField(default="",max_length=200)

	class Meta:
		unique_together = ('year', 'company',)

	def __str__(self):
		return self.company.name + " " + self.year