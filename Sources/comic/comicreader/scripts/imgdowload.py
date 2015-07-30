__author__ = 'sang'
# -*- coding: utf-8 -*-
import urllib
import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

env = "comic.settings"

# setup_environ(settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.conf import settings
from comicreader.models import *
from database_utility import *
from database_query_utility import *

def dirNameEbook(ebookname):
    """
    Kiểm tra thư mục đã tồn tại hay không. Nếu chưa đã tồn tại thì tạo thư mục mới sau đó trả về đường dẫn tới thư mục đó.

    :param ebookname:Tên thư mục
    :return path: đường dẫn tới thư mục
    """

    path = os.path.join(settings.PATH_DATA_IMAGE, ebookname)
    if not os.path.exists(path):
        os.mkdir(os.path.join(path),0755)
    else:
        #print 'Folder %s exits' %ebookname
        pass
    return  path

def dirNameChapter(ebook_path,chaptername):
    """
    :param chaptername:
    :return:
    """
    path =  os.path.join(ebook_path,chaptername)
    if not os.path.exists(path):
        os.mkdir(path,0755)
    else:
        #print 'Folder %s exits' %chaptername
        pass
    return  path

def download_photo(path, img_url, filename):
    """
    :param path:
    :param filename:
    :return:
    """
    file_path = "%s/%s" % (path, filename)
    downloaded_image = file(file_path, "wb")
    image_on_web = urllib.urlopen(img_url)
    while True:
        buf = image_on_web.read(65536)
        if len(buf) == 0:
            break
        downloaded_image.write(buf)
    downloaded_image.close()
    image_on_web.close()

    image = Image()
    image.url = img_url
    image.real_path = file_path
    return image


if __name__ == '__main__':
    for i in range(1,1000):
        images = getImageUrls(i)
        if images:
            image = images[0]
            path = dirNameChapter(dirNameEbook(image['chapter__ebook__name']),image['chapter__name'])
            file_name = str(image['id'])+'_'+ image['name']
            update_image(download_photo(path,image['url'],file_name))
        else:
            pass
