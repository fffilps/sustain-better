# Generated by Django 5.0.6 on 2024-06-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ai_hackathon_api", "0006_companyemotions"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="youtube_url",
            field=models.CharField(default="", max_length=200),
        ),
    ]