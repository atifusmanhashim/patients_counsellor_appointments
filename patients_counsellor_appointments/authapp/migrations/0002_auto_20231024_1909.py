# Generated by Django 3.2.7 on 2023-10-24 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginanalytics',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='loginanalytics',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='loginanalytics',
            name='modified_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
