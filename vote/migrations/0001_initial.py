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
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('v_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Id')),
                ('v_vote', models.BooleanField(default=False, verbose_name='Vote')),
                ('v_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='v_project', to='project.Project', verbose_name='Project')),
                ('v_voter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='v_employee', to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
            ],
        ),
    ]
