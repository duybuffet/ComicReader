# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AccessHistory(models.Model):
    device = models.ForeignKey('Device')
    request_date = models.DateTimeField(blank=True, null=True)
    num_request = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'access_history'


class Bookcat(models.Model):
    ebook = models.ForeignKey('Ebook')
    category = models.ForeignKey('Category')

    class Meta:
        managed = False
        db_table = 'bookcat'


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Chapter(models.Model):
    ebook = models.ForeignKey('Ebook')
    name = models.TextField()
    url = models.TextField()
    status = models.CharField(max_length=45, blank=True, null=True)
    update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chapter'


class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    last_date = models.DateTimeField()
    block = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'device'


class Ebook(models.Model):
    name = models.TextField()
    url = models.TextField()
    cover = models.TextField()
    author = models.CharField(max_length=225, blank=True, null=True)
    update = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    complete = models.IntegerField(blank=True, null=True)
    check = models.IntegerField(blank=True, null=True)
    ebook_source = models.TextField(blank=True, null=True)
    source = models.ForeignKey('SourceEbook', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebook'


class Favorite(models.Model):
    ebook = models.ForeignKey(Ebook)
    device = models.ForeignKey(Device)

    class Meta:
        managed = False
        db_table = 'favorite'


class Feedback(models.Model):
    id = models.IntegerField(primary_key=True)
    device = models.ForeignKey(Device, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    send_date = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class Image(models.Model):
    chapter = models.ForeignKey(Chapter)
    url = models.TextField()
    status = models.IntegerField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'image'


class SourceEbook(models.Model):
    url = models.TextField()
    total_chap = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'source_ebook'


class ViewCount(models.Model):
    num_view = models.IntegerField()
    ebook = models.ForeignKey(Ebook)

    class Meta:
        managed = False
        db_table = 'view_count'
