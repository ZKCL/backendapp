# Generated by Django 3.0.7 on 2021-10-22 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20211021_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='cases_client',
        ),
    ]
