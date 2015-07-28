# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_request', models.DateTimeField(null=True, blank=True)),
                ('num_request', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'access_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bookcat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'bookcat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('url', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('status', models.CharField(max_length=45, null=True, blank=True)),
                ('update', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'chapter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('last_date', models.DateTimeField()),
                ('block', models.IntegerField()),
            ],
            options={
                'db_table': 'device',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('url', models.TextField(null=True, blank=True)),
                ('cover', models.TextField(null=True, blank=True)),
                ('author', models.CharField(max_length=225, null=True, blank=True)),
                ('update', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('complete', models.IntegerField(null=True, blank=True)),
                ('check', models.IntegerField(null=True, blank=True)),
                ('totalchap', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ebook',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'favorite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.TextField(null=True, blank=True)),
                ('send_date', models.DateField(null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'feedback',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField()),
                ('status', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_view', models.IntegerField()),
            ],
            options={
                'db_table': 'view_count',
                'managed': False,
            },
        ),
    ]
