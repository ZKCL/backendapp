# Generated by Django 3.0.7 on 2021-10-19 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='chat_preference',
            field=models.CharField(choices=[('0', 'ChatApp'), ('1', 'Llamada')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('D', 'Disponible'), ('A', 'Asignado'), ('S', 'Solicitud Cierre'), ('C', 'Cerrado')], default='Disponible', max_length=1),
        ),
    ]
