# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkstand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=10)),
                ('create_time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-create_time'],
            },
        ),
    ]