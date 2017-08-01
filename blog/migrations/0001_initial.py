# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyblogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('blog_title', models.CharField(max_length=20)),
                ('blog_text', models.TextField()),
                ('blog_date', models.DateField()),
                ('blog_bread', models.IntegerField(default=0)),
                ('blog_comment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
