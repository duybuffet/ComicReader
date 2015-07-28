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

input ={'ebookname': 'Naruto', 'chapter_name': 'Naruto Chap 002_test', 'urlimg': '', 'nameimg': '' }


def dirNameEbook(ebookname):

    """
    :param ebookname:
    :return:
    """

    path = os.path.join(settings.PATH_DATA_IMAGE, ebookname)
    if not os.path.exists(path):
        os.mkdir(os.path.join(path),0755)
    else:
        #print 'Folder %s exits' %ebookname
        pass
    return  path

def dirNameChapter(chaptername):
    """
    :param chaptername:
    :return:
    """
    path =  os.path.join(dirNameEbook(input['ebookname']),chaptername)
    if not os.path.exists(path):
        os.mkdir(path,0755)
    else:
        #print 'Folder %s exits' %chaptername
        pass
    return  path
def dowloadImage(input):
    pass

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
    return file_path

if __name__ == '__main__':
    path = dirNameChapter(input['chaptername'])
    print path
    url = input['urlimg']
    image= input['nameimg']
    print len(url)
    print len(image)
    for i in xrange(len(url)):
      print download_photo(path, url[i], image[i] )