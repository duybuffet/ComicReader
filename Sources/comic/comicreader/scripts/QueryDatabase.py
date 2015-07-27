__author__ = 'sang'
# -*- coding: utf-8 -*-
import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

env = "comic.settings"

# setup_environ(settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from comicreader.models import *


def getEbook():
    listEbook = []
    sql= 'SELECT id, url FROM ebook'
    for eb in Ebook.objects.raw(sql):
        listEbook.append(eb)
    return listEbook

def getChapter():
    listChap = []
    sql= 'SELECT id, url FROM chapter'
    for chap in Chapter.objects.raw(sql):
        listChap.append(chap)
    return listChap

def getDownload():
    listImage = []
    sql= 'SELECT a.id, a.name, b.id, b.name, c.id, c.name, c.url FROM ebook a, chapter b, image c WHERE a.id = b.ebook_id AND b.ebook_id = chapter_id;'
    for image in Image.objects.raw(sql):
        listImage.append(image)
    return listImage
if __name__ == '__main__':
    getEbook()
    getChapter()
    getDownload()