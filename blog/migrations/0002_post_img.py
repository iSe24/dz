# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='1.jpg', upload_to='C:/RRR/mysite/blog/book_img'),
            preserve_default=False,
        ),
    ]
