# Generated by Django 3.0.7 on 2021-10-22 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_remove_case_cases_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='cases_teacher',
        ),
    ]
