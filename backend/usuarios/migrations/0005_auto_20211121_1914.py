# Generated by Django 3.0.7 on 2021-11-21 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20211019_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(default='', max_length=255)),
                ('valor', models.IntegerField(default=0)),
                ('orden', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('orden',),
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=32, unique=True)),
                ('texto', models.TextField(default='')),
                ('orden', models.IntegerField(default=0)),
                ('User', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('orden',),
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Opcion')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='usuarios.Pregunta')),
            ],
            options={
                'ordering': ('pregunta',),
            },
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='usuarios.Pregunta'),
        ),
        migrations.AddField(
            model_name='opcion',
            name='salto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Pregunta'),
        ),
    ]