# Generated by Django 5.0.6 on 2024-06-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ai_hackathon_api", "0004_alter_companyreport_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="companyreport",
            name="pdf_name",
            field=models.CharField(default="", max_length=200),
        ),
    ]