# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-11 21:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acuse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('default', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Acuse',
                'verbose_name_plural': 'Acuses',
            },
        ),
        migrations.CreateModel(
            name='Directorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesion', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('pareja', models.CharField(blank=True, max_length=150, null=True)),
                ('cargo', models.TextField(blank=True, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(default='1', max_length=1)),
                ('modificado', models.CharField(blank=True, max_length=150, null=True)),
                ('cdmx', models.BooleanField(default=False)),
                ('num', models.CharField(max_length=4)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Directorio',
                'verbose_name_plural': 'Directorios',
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamps', models.DateTimeField(auto_now=True)),
                ('directorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directorio.Directorio')),
            ],
            options={
                'verbose_name': 'Historial',
                'verbose_name_plural': 'Historiales',
            },
        ),
        migrations.CreateModel(
            name='Obsequio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('cantidad', models.IntegerField()),
                ('entregado', models.IntegerField(blank=True, default=0, null=True)),
                ('existencia', models.IntegerField(blank=True, default=0, null=True)),
                ('default', models.BooleanField(default=False)),
                ('timestamps', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Obsequio',
                'verbose_name_plural': 'Obsequios',
            },
        ),
        migrations.AddField(
            model_name='historial',
            name='obsequio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directorio.Obsequio'),
        ),
        migrations.AddField(
            model_name='acuse',
            name='obsequio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='directorio.Obsequio'),
        ),
    ]
