__author__ = 'Duy'

import os, sys

"""
    Tuy tung may ma thiet lap bien moi truong
"""
sys.path.append("/home/duy/Work/NextG/git-repos/ComicReader/Sources/comic")
sys.path.append("/home/duy/Work/NextG/git-repos/ComicReader/Sources/comic/comic")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","comic.settings")

from django.utils import timezone
from comicreader.models import *


"""
    Ham nay them danh muc vao csdl
    Input: Danh sach cac doi tuong Category
    Output: 1 neu them thanh cong
            0 neu xay ra loi
"""
def insert_categories(categories):
    try:
        for cat in categories:
            cat.save()
    except:
        return 0
    return 1


"""
    Ham nay them ebook vao csdl
    Input: doi tuong Ebook
    Output: 1 neu them thanh cong
            0 neu xay ra loi
"""
def insert_ebook(ebook):
    try:
        ebook.save()
    except:
        return 0
    return 1


"""
    Ham nay cap nhat ebook va them vao bang danh muc - ebook
    Input: Cac thuoc tinh cua ebook, danh sach cac doi tuong Category
    Output: 1 neu them thanh cong
            0 neu xay ra loi
"""
def update_ebook_and_add_bookcat(id,name,author,cover,description,update,complete,check,category):
    try:
        # get and update ebook with provided id
        ebook = Ebook.objects.get(pk=id)
        (ebook.name,ebook.author,ebook.cover,ebook.description,ebook.update,ebook.complete,ebook.check) = (name,author,cover,description,update,complete,check)
        ebook.save()

        # get categories in db
        categories = []
        for item in category:
            categories.append(Category.objects.filter(name=item)[0])

        # update bookcat
        for cat in categories:
            bookcat = Bookcat(ebook=ebook,category=cat)
            bookcat.save()
    except:
        return 0
    return 1


"""
    Ham nay them chapter vao csdl
    Input: Doi tuong Chapter, ebook_id
    Output: 1 neu them thanh cong
            0 neu xay ra loi
"""
def insert_chapter(chapter, ebook_id):
    try:
        ebook = Ebook.objects.get(pk=ebook_id)
        chapter.ebook = ebook
        chapter.status = "true"
        chapter.save()
    except:
        return 0
    return 1


"""
    Ham nay them image vao csdl
    Input: Doi tuong Image, chapter_id
    Output: 1 neu them thanh cong
            0 neu xay ra loi
"""
def insert_image(image, chapter_id):
    try:
        chapter = Chapter.objects.get(pk=chapter_id)
        image.chapter = chapter
        image.status = 0
        image.save()
    except:
        return 0
    return 1


""" TEST DATA """
# chapter = Chapter(name="abc",url="xyz")
# print insert_chapter(chapter,2)

# image = Image(url="aaa",name="bbb")
# print insert_image(image, 1)
# cat = Category(name='cat3', description='aloxo')
# cat2 = Category(name='cat4', description='aloxo')
# print insert_categories([cat, cat2])

# ebook = Ebook(url='https://blogtruyen.com/dragonball',totalchap=200)
# print insert_ebook(ebook)

#print update_ebook_and_add_bookcat(2,'yaiba','ozawa','1','',timezone.now(),1,1,['cat3','cat4'])