# Generated by Django 3.0.7 on 2021-10-22 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_auto_20211021_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Client'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Teacher'),
        ),
    ]
