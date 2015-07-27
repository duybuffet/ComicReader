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
    for eb in Ebook.objects.raw('SELECT * FROM ebook'):
        listEbook.append(eb)
    return listEbook


def getChapter(ebook_id):
    listChap = []
    for chap in Chapter.objects.raw('SELECT * FROM chapter WHERE ebook_id = %s', [ebook_id]):
        listChap.append(chap)
    return listChap


def getChapter(chapter_id):
    listimage = []
    for image in Image.objects.raw('SELECT * FROM image WHERE chapter_id = %s', [chapter_id]):
        listimage.append(image)
    return listimage

if __name__ == '__main__':
    for chap in getChapter(3):
        print chap.url
