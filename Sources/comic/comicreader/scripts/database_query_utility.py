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
from django.db.models import Q, F
from django.db.models import Count
from django.db.models.functions import *

def getEbooks():
    """
    Lay thong tin tu CSDL de lam input cho viec crawl chapter
    :return: list object ebook
    """
    ebook = Ebook.objects.filter().values("id","url")
    return ebook

def getEbookById(ebook_id):
    """
    Lay thong tin tu CSDL de lam input cho viec crawl chapter
    :return: list object ebook
    """
    filters = Q(id= ebook_id)
    ebook = Ebook.objects.filter(filters).values("id","url","name","cover","description","author")
    return ebook

def getAllChapterEbook(ebook_id):
    """
    Lay list chapter cua 1 ebook
    :param ebook_id:
    :return: list chapter
    """
    filters = Q(ebook_id= ebook_id)
    listChapters = Chapter.objects.filter(filters).values("id","url","name")
    return listChapters

def getChapterById(chapter_id):
    filters = Q(id= chapter_id)
    chapter = Chapter.objects.filter(filters).values("id","url")
    return chapter


def getChapters():
    """
    Lay thong tin tu CSDL de lam input cho viec crawl image
    :return: list cac object chapter
    """
    chapters = Image.objects.filter().values("id","url")
    print chapters
    return chapters

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

def getImageUrls(image_id):
    """
    Lay thong tin tu CSDL de thuc hien viec download image
    :return: dictionary
    """
    #sql= 'SELECT a.id, a.name, b.id, b.name, c.id, c.name, c.url FROM ebook a, chapter b, image c WHERE a.id = b.ebook_id AND b.ebook_id = chapter_id;'
    filters = Q(status__in=[IMAGE_STATUS_DOWNLOAD_FAILED, IMAGE_STATUS_PENDING],
                id= image_id)
    images = Image.objects.filter(filters).values("id","url", "name", "chapter__name", "chapter_id", "chapter__ebook__id", "chapter__ebook__name")
    return images

def getAllImageUrls():
    """
    Lay thong tin tu CSDL de thuc hien viec download image
    :return: dictionary
    """
    #sql= 'SELECT a.id, a.name, b.id, b.name, c.id, c.name, c.url FROM ebook a, chapter b, image c WHERE a.id = b.ebook_id AND b.ebook_id = chapter_id;'
    filters = Q(status__in=[IMAGE_STATUS_DOWNLOAD_FAILED, IMAGE_STATUS_PENDING])
    images = Image.objects.filter(filters).values("id","url", "name", "chapter__name", "chapter_id", "chapter__ebook__id", "chapter__ebook__name")
    return images


def get_images_of_chapter(chapter_id):
    """
    :param chapter_id
    :return:
    """
    filters = Q(chapter_id=chapter_id)
    images = Image.objects.filter(filters).values('real_path')
    return images

def insert_feedback(feedback):
    """
    insert data to the table feedback
    :param feedback: object insert
    :return: 1: Successful
             0: Fail
    """
    try:
        feedback =  Feedback(chapter_id=feedback.id,ebook_id=feedback.ebook_id,title=feedback.title,description=feedback.description,send_date=datetime.datetime.now(),status=0)
        print feedback
        feedback.save()
    except Exception as inst:
        return 0
    return 1





# ------------------------------bat dau Hieu viet method-----------------------------------
def getEbooksNew():
    """
    search ebook new limit 10
    :return: list object Ebook
    """
    filters = Q()
    ebooks = Ebook.objects.filter(filters).order_by('update').reverse().values('id','name','cover','update')[:API_LIMIT_ELEMENT_SEARCH]
    return ebooks


def getEbooksByCategoy(category):
    """
    search ebook by catergory
    :param category:
    :return: list object Ebook
    """
    filters = Q(name=category)
    categorys = Category.objects.filter(filters).values('id')
    print categorys[0]['id']
    filters = Q(category_id=categorys[0]['id'])
    ebooks = Bookcat.objects.filter(filters).values('ebook__id','ebook__name','ebook__cover','ebook__update')
    return ebooks

def getEbooksByView():
    """
    search ebook by views
    :return:list object Ebook
    """
    filters = Q()
    ebooks = ViewCount.objects.filter(filters).order_by('num_view').values('ebook__id','ebook__name','ebook__cover','ebook__update')
    return ebooks


def getEbooksByFavorite():
    """
    search ebook by favorite
    :return: list object Ebook
    """
    filters = Q()
    ebooks = Favorite.objects.filter(filters)\
        .values('ebook_id')\
        .annotate(count_device=Count('device_id'))\
        .order_by('count_device').reverse()\
        .values('ebook__name','ebook__cover','ebook__update','ebook__id')
    return ebooks

def getEbooksByNameAuthor(nameAuthor):
    """
    search ebook by name author
    :param nameauthor: name author
    :return:list object Ebook
    """
    filters = Q(author__contains=nameAuthor)
    ebooks = Ebook.objects.filter(filters).values('id','name','cover','update')
    return ebooks


def getEbooksByNameEbook(nameEbook):
    """
    search ebook by name ebook
    :param nameauthor: name ebook
    :return:list object Ebook
    """
    filters = Q(name__contains=nameEbook)
    ebooks = Ebook.objects.filter(filters).values('id','name','cover','update')
    return ebooks

#----------------------------------ket thuc Hieu viet method----------------------------------------------

if __name__ == '__main__':
    pass