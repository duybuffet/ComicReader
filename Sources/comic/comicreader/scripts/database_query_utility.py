__author__ = 'phuong'
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
from comicreader.constants import *
from django.db.models import Q

def getEbooks():
    """
    Lay thong tin tu CSDL de lam input cho viec crawl chapter
    :return: list object ebook
    """
    listEbook = []
    sql= 'SELECT id, url FROM ebook'
    for eb in Ebook.objects.raw(sql):
        listEbook.append(eb)
    return listEbook

def getChapters():
    """
    Lay thong tin tu CSDL de lam input cho viec crawl image
    :return: list cac object chapter
    """
    listChap = []
    sql= 'SELECT id, url FROM chapter'
    for chap in Chapter.objects.raw(sql):
        listChap.append(chap)
    return listChap

def getImageUrls():
    """
    Lay thong tin tu CSDL de thuc hien viec download image
    :return: dictionary
    """
    #sql= 'SELECT a.id, a.name, b.id, b.name, c.id, c.name, c.url FROM ebook a, chapter b, image c WHERE a.id = b.ebook_id AND b.ebook_id = chapter_id;'
    filters = Q(status__in=[IMAGE_STATUS_DOWNLOAD_FAILED, IMAGE_STATUS_PENDING])
    images = Image.objects.filter(filters).values("url", "name", "chapter__name", "chapter_id", "chapter__ebook__id", "chapter__ebook__name")
    print images
    return images

if __name__ == '__main__':
    getEbooks()
    getChapters()
    getImageUrls()