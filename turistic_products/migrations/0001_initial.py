# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TuristicProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(-1, b'Eliminado'), (0, b'Inactivo'), (1, b'Activo')], default=1, max_length=2)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified_date', models.DateTimeField(null=True)),
                ('deleted_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('createdby_id', models.IntegerField(default=0)),
                ('modifiedby_id', models.IntegerField(default=0)),
                ('synckey', models.CharField(default='', max_length=512)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=512)),
                ('calification', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
