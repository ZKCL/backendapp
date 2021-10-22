# Generated by Django 3.0.7 on 2021-10-19 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('files', models.FileField(upload_to='documents/cases/', verbose_name='Casos')),
                ('description', models.CharField(max_length=300)),
                ('type', models.CharField(choices=[('L', 'Legal'), ('F', 'Financiera'), ('A', 'Ambos')], default='', max_length=1)),
                ('status', models.CharField(choices=[('L', 'Legal'), ('F', 'Financiera'), ('A', 'Ambos')], default='Disponible', max_length=1)),
                ('chat_preference', models.CharField(choices=[('L', 'Legal'), ('F', 'Financiera'), ('A', 'Ambos')], default='', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizacion')),
                ('finished_at', models.DateTimeField(auto_now=True, verbose_name='Fecha Cierre')),
                ('case_client', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Client')),
                ('case_teacher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Teacher')),
            ],
            options={
                'verbose_name': 'case',
                'verbose_name_plural': 'cases',
            },
        ),
    ]
