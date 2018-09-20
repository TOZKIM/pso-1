# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-28 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20, verbose_name='\uacfc\ubaa9')),
                ('name', models.TextField(max_length=10, verbose_name='\uc774\ub984')),
                ('contents', models.TextField(verbose_name='\ub0b4\uc6a9')),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]