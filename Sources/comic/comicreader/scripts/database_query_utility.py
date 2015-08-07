__author__ = 'phuong'
import os
import sys
import logging

# config logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
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
    ebook = Ebook.objects.filter(filters).values("id","url","name","cover","description","author","update")
    return ebook

def getAllChapterEbook(ebook_id):
    """
    Lay list chapter cua 1 ebook
    :param ebook_id:
    :return: list chapter
    """
    filters = Q(ebook_id= ebook_id)
    listChapters = Chapter.objects.filter(filters).values("id","url","name","update")
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
    Change log : 1/8/2015 - Duy - Change from values('real_path') to values('id')
    :param chapter_id
    :return:
    """
    filters = Q(chapter_id=chapter_id)
    images = Image.objects.filter(filters).values('id') # old : values('real_path')
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
        feedback.save()
    except Exception as inst:
        return 0
    return 1





# ------------------------------bat dau Hieu viet method-----------------------------------

def getEbooksBy18():
    """
    search ebook 18+
    :return: list id of ebook 18+
    """
    logging.info("Start function getEbooksBy18()")
    filters = Q(name__in=API_BLOCK_CATEGORY)
    ebooks = Category.objects.filter(filters).values('bookcat__ebook__id')
    listEbook = []
    for ebook in ebooks:
        listEbook.append(ebook['bookcat__ebook__id'])
    logging.info("End function getEbooksBy18()")
    return listEbook


def getEbooksNew():
    """
    search ebook new limit 10
    :return: list object Ebook
    """
    logging.info("Start function getEbooksNew()")
    listEbook18 = getEbooksBy18()
    filters = Q()
    ebooks = Ebook.objects.filter(filters).order_by('update').reverse().values('id','name','cover','update')[:API_LIMIT_ELEMENT_SEARCH]
    listEbook = []
    for ebook in ebooks:
        if ebook['id'] in listEbook18:
            pass
        else:
            data = {'id' :ebook['id'], 'cover' : convertCover(ebook['cover']), 'name' : ebook['name'], 'update' : convertDate(str(ebook['update']))}
            listEbook.append(data)
    logging.info("End function getEbooksNew()")
    return listEbook


def getEbooksByCategoy(category):
    """
    search ebook by catergory
    :param category:
    :return: list object Ebook
    """
    logging.info("Start function getEbooksByCategoy()")
    listEbook18 = getEbooksBy18()
    filters = Q(name=category)
    ebooks = Category.objects.filter(filters).values('bookcat__ebook__id','bookcat__ebook__name','bookcat__ebook__cover','bookcat__ebook__update')
    listEbook = []
    for ebook in ebooks:
        if ebook['bookcat__ebook__id'] in listEbook18:
            pass
        else:
            data = {'id' :ebook['bookcat__ebook__id'], 'cover' :  convertCover(ebook['bookcat__ebook__cover']), 'name' : ebook['bookcat__ebook__name'], 'update' : convertDate(str(ebook['bookcat__ebook__update']))}
            listEbook.append(data)
    logging.info("End function getEbooksByCategoy()")
    return listEbook


def getEbooksByView():
    """
    search ebook by views
    :return:list object Ebook
    """
    logging.info("Start function getEbooksByView()")
    listEbook18 = getEbooksBy18()
    filters = Q()
    ebooks = ViewCount.objects.filter(filters).order_by('num_view').values('ebook__id','ebook__name','ebook__cover','ebook__update')
    listEbook = []
    for ebook in ebooks:
        if ebook['ebook__id'] in listEbook18:
            pass
        else:
            data = {'id' :ebook['ebook__id'], 'cover' :  convertCover(ebook['ebook__cover']), 'name' : ebook['ebook__name'], 'update' : convertDate(str(ebook['ebook__update']))}
            listEbook.append(data)
    logging.info("End function getEbooksByView()")
    return listEbook


def getEbooksByFavorite():
    """
    search ebook by favorite
    :return: list object Ebook
    """
    logging.info("Start function getEbooksByFavorite()")
    listEbook18 = getEbooksBy18()
    filters = Q()
    ebooks = Favorite.objects.filter(filters)\
        .values('ebook_id')\
        .annotate(count_device=Count('device_id'))\
        .order_by('count_device').reverse()\
        .values('ebook__name','ebook__cover','ebook__update','ebook__id')
    listEbook = []
    for ebook in ebooks:
        if ebook['ebook__id'] in listEbook18:
            pass
        else:
            data = {'id' :ebook['ebook__id'], 'cover' :  convertCover(ebook['ebook__cover']), 'name' : ebook['ebook__name'], 'update' : convertDate(str(ebook['ebook__update']))}
            listEbook.append(data)
    logging.info("End function getEbooksByFavorite()")
    return listEbook

def getEbooksByNameAuthor(nameAuthor):
    """
    search ebook by name author
    :param nameauthor: name author
    :return:list object Ebook
    """
    logging.info("Start function getEbooksByNameAuthor()")
    listEbook18 = getEbooksBy18()
    filters = Q(author__contains=nameAuthor)
    ebooks = Ebook.objects.filter(filters).values('id','name','cover','update')
    listEbook = []
    for ebook in ebooks:
        if ebook['id'] in listEbook18:
            pass
        else:
            data = {'id' :ebook['id'], 'cover' :  convertCover(ebook['cover']), 'name' : ebook['name'], 'update' : convertDate(str(ebook['update']))}
            listEbook.append(data)
    logging.info("End function getEbooksByNameAuthor()")
    return listEbook



def getEbooksByNameEbook(nameEbook):
    """
    search ebook by name ebook
    :param nameauthor: name ebook
    :return:list object Ebook
    """
    logging.info("Start function getEbooksByNameEbook()")
    listEbook18 = getEbooksBy18()
    filters = Q(name__contains=nameEbook)
    ebooks = Ebook.objects.filter(filters).values('id','name','cover','update')
    listEbook = []
    for ebook in ebooks:
        if ebook['id'] in listEbook18:
            pass
        else:
            data = {'id' :ebook['id'], 'cover' :  convertCover(ebook['cover']), 'name' : ebook['name'], 'update' : convertDate(str(ebook['update']))}
            listEbook.append(data)
    logging.info("End function getEbooksByNameEbook()")
    return listEbook


def getTotalEbookInCategory():
    """
    search total ebook in category
    :return: list total and name category
    """
    logging.info("Start function getTotalEbookInCategory()")
    cover = ''
    listEbook18 = getEbooksBy18()
    filters = Q()
    ebooks = Category.objects.filter(filters)\
        .values('bookcat__category_id')\
        .annotate(totalEbook=Count('bookcat__ebook_id'))\
        .values('name','totalEbook','id')
    listEbook = []
    for ebook in ebooks:
        if len(Bookcat.objects.filter(category_id = ebook['id'])) > 0:
            book_cat = Bookcat.objects.filter(category_id = ebook['id']).values("ebook_id")[0]
            cover = Ebook.objects.filter(pk=book_cat["ebook_id"]).values("cover")[0]["cover"]
        if ebook['name'] in API_BLOCK_CATEGORY:
            pass
        else:
            data = {'name' :ebook['name'], 'total' : ebook['totalEbook'], 'id' : ebook['id'], 'cover' : cover}
            listEbook.append(data)
    logging.info("End function getTotalEbookInCategory()")
    return listEbook



def getEbooksHot():
    """
    ebook hot
    :return:list object Ebook
    """
    logging.info("Start function getEbooksHot()")
    listEbook18 = getEbooksBy18()
    filters = Q(id__in=API_ID_EBOOK_HOT)
    ebooks = Ebook.objects.filter(filters).values('id','name','cover','update')
    listEbook = []
    for ebook in ebooks:
        if ebook['id'] in listEbook18:
            pass
        else:
            data = {'id' :ebook['id'], 'cover' :  convertCover(ebook['cover']), 'name' : ebook['name'], 'update' : convertDate(str(ebook['update']))}
            listEbook.append(data)
    logging.info("End function getEbooksHot()")
    return listEbook

def getTotalImageInChapter(id):
    """
    search total image in chapter
    :return: list total image and id chapter
    """
    logging.info("Start function getTotalImageInChapter()")
    listEbook18 = getEbooksBy18()
    filters = Q(chapter_id=id)
    ebooks = Image.objects.filter(filters)\
        .values('chapter_id')\
        .annotate(totalImage=Count('id'))\
        .values('chapter_id', 'totalImage')
    total = ''
    for ebook in ebooks:
        if ebook['chapter_id'] in listEbook18:
            pass
        else:
            total= ebook['totalImage']
    logging.info("End function getTotalImageInChapter()")
    return total

def getAllEbook():
    """
    get id and name of All Ebook
    :return: list object Ebook
    """
    logging.info("Start method getAllEbook()")
    listEbook18 = getEbooksBy18()
    filters = Q()
    ebooks = Ebook.objects.filter(filters).values('id','name')
    listEbook = []
    for ebook in ebooks:
        if ebook['id'] in listEbook18 or ebook['name'] == None:
            pass
        else:
            data = {'id' :ebook['id'], 'name' : ebook['name']}
            print data
            listEbook.append(data)
    logging.info("End method getAllEbook()")
    return listEbook


def convertDate(date):
    """
    convert date: yyyy-dd-mm
    :param date: string
    :return:string
    """
    return date[:10]

def convertCover(url):
    """
    convert url
    :param date: string
    :return:string
    """
    url = url.replace('\r','')
    url = url.replace('\n','')
    if url.endswith('.png'):
        url = "http://os-jpupacic-omis.skole.hr/upload/os-jpupacic-omis/images/static3/1241/Image/jpg_1666-boy-with-books-in-their-hands.jpg"
    return url

#-----------------------------fix real_path of images -------------------------
def fixPath(id):
    """

    fix real_path of Images
    :return:
    """
    Old_path = API_PATH_ABS
    path = getPath(id)
    if path!=None:
        filters = Q(id=id)
        Image.objects.filter(filters).update(real_path=path.replace(Old_path,''))


def getPath(id):
    """
    get real_path of images
    :return:  real_path (text)
    """
    filters = Q(id=id)
    images = Image.objects.filter(filters).values('id','real_path')
    path = ''
    for image in images:
        path = image['real_path']
    return path


def getUrl(id):
    """
    get real_path of images
    :return:  real_path (text)
    """
    filters = Q(id=id)
    images = Image.objects.filter(filters).values('id','url')
    path = ''
    for image in images:
        path = image['url']
    return path
#----------------------------------ket thuc Hieu viet method----------------------------------------------

def get_image_path_by_id(image_id):
    """
    Get real path of given image_id
    :param image_id: id of image
    :return:url of image
    """
    logging.info("Start function get_image_path_by_id()")
    logging.debug("image_id : %s"%image_id)

    path = ""
    try:
        path = os.path.join(API_PATH_ABS, Image.objects.filter(pk=image_id)[0].real_path)
    except Exception as inst:
        logging.error(type(inst))
        logging.error(inst)

    logging.info("End function get_image_path_by_id()")
    print path
    return path

def get_ebooks_by_cat(cat_id):
    """
    Get list of ebooks that have category_id
    :param category_id:
    :return: list ebooks having category_id
    """
    result = []
    logging.info("Start function get_ebooks_by_cat()")
    try:
        list_ebook_id = Bookcat.objects.filter(category_id=cat_id).values("ebook_id")
        list_ebook = Ebook.objects.filter(pk__in = list_ebook_id)
        for ebook in list_ebook:
            result.append({'id' : ebook.id, 'name' : ebook.name, 'cover' : convertCover(ebook.cover), 'update' : convertDate(str(ebook.update))})
        logging.info("End function get_ebooks_by_cat()")
        return result
    except Exception as inst:
        logging.error(type(inst))
        logging.error(inst)
        return []


if __name__ == '__main__':
    for i in range(1300,14000):
        if '+' in getUrl(i):
            print str(i)+'    '+getUrl(i)
    pass