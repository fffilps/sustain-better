# Generated by Django 5.0.6 on 2024-06-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ai_hackathon_api", "0011_post_status_alter_poststatus_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="img_bin_verified",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="img_waste_verified",
            field=models.TextField(null=True),
        ),
    ]
