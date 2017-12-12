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
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('s_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')),
                ('s_date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('s_vote', models.FloatField(verbose_name='Vote')),
                ('s_choise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='s_choise', to=settings.AUTH_USER_MODEL, verbose_name='Choise')),
                ('s_voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_voter', to=settings.AUTH_USER_MODEL, verbose_name='Voter')),
            ],
        ),
    ]
