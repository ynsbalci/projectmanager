# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-12 11:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fault',
            fields=[
                ('f_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')),
                ('f_name', models.CharField(max_length=120, verbose_name='Name')),
                ('f_defination', models.TextField(verbose_name='Defination')),
                ('f_date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('f_status', models.IntegerField(default=0, verbose_name='Status')),
                ('f_slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('f_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f_employee', to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
                ('f_task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f_task', to='task.Task', verbose_name='Task')),
            ],
            options={
                'ordering': ['f_name', 'f_id'],
            },
        ),
    ]
