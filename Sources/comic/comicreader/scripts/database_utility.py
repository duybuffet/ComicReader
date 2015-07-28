__author__ = 'Duy'

import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

env = "comic.settings"

# setup_environ(settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env)

from django.utils import timezone
from comicreader.models import *


def insert_categories(categories):
    """
    Insert categories into database
    :param: categories - list of Category objects
    :return: 1 if success
             0 otherwise
    """
    try:
        for cat in categories:
            cat.save()
    except:
        return 0
    return 1


def insert_ebooks(ebooks):
    """
    Insert ebooks into database
    :param: ebooks - list of Ebook objects
    :return: 1 if success
             0 otherwise
    """
    try:
        for ebook in ebooks:
            ebook.save()
    except:
        return 0
    return 1


def update_ebook_and_add_bookcat(dict_ebook_cats):
    """
    Update an ebook and insert bookcat into database
    :param: dict_ebook_cats - a dictionary contains an ebook and list of category names
    :return: 1 if success
             0 otherwise
    """
    try:
        # get and update ebook with provided id
        ebook_update = dict_ebook_cats.get("ebook")
        ebook = Ebook.objects.get(pk=ebook_update.id)
        (ebook_update.url, ebook_update.totalchap) = (ebook.url, ebook.totalchap)
        ebook_update.save()

        # get categories in db
        categories = []
        categories_name = dict_ebook_cats.get("categories")
        for item in categories_name:
            categories.append(Category.objects.filter(name=item)[0])

        # update bookcat
        for cat in categories:
            bookcat = Bookcat(ebook=ebook,category=cat)
            bookcat.save()
    except:
        return 0
    return 1


def insert_chapters(dict_chapters_ebook_id):
    """
    Insert chapters into database
    :param: dict_chapters_ebook_id - a dictionary contain chapters and ebook_id
    :return: 1 if success
             0 otherwise
    """
    try:
        ebook = Ebook.objects.get(pk=dict_chapters_ebook_id.get("ebook_id"))
        for chapter in dict_chapters_ebook_id.get("chapters"):
            chapter.ebook = ebook
            chapter.status = 0
            chapter.save()
    except:
        return 0
    return 1


def insert_images(dict_images_chapter_id):
    """
    Insert images into database
    :param: dict_images_chapter_id - a dictionary contains images and chapter_id
            chapter_id - id of chapter that the images belonged to
    :return: 1 if success
             0 otherwise
    """
    try:
        chapter = Chapter.objects.get(pk=dict_images_chapter_id.get("chapter_id"))
        for image in dict_images_chapter_id.get("images"):
            image.chapter = chapter
            image.status = 0
            image.save()
    except:
        return 0
    return 1

""" TEST DATA """
# chapter = Chapter(name="def",url="xyz")
# chapter2 = Chapter(name="def",url="xyz322323")
# print insert_chapters({"ebook_id":1, "chapters":[chapter, chapter2]})

# image = Image(url="aaa",name="bbb")
# print insert_images({"chapter_id":3,"images":[image]})
# cat = Category(name='cat3', description='aloxo')
# cat2 = Category(name='cat4', description='aloxo')
# print insert_categories([cat, cat2])
#
# ebook = Ebook(id=1, cover='test',name='yugioh', url='https://blogtruyen.com/yugioh',totalchap=169)
# print insert_ebooks([ebook])

# print update_ebook_and_add_bookcat({"ebook" : ebook,"categories" : ['cat3','cat4']})