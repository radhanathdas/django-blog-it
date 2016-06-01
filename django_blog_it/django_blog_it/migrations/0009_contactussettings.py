# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog_it', '0008_post_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=254)),
                ('reply_to_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_admin', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=500)),
                ('body_user', models.TextField()),
                ('body_admin', models.TextField()),
            ],
        ),
    ]
