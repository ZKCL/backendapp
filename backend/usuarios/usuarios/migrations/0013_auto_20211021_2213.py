# Generated by Django 3.0.7 on 2021-10-22 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_case_cases_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='case_client',
        ),
        migrations.RemoveField(
            model_name='case',
            name='case_teacher',
        ),
        migrations.RemoveField(
            model_name='case',
            name='cases_client',
        ),
    ]
