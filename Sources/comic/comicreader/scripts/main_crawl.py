__author__ = 'sang'

import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

env = "comic.settings"

# setup_environ(settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crawl import *
from database_utility import *
from database_query_utility import *


if __name__ == '__main__':
    # insert_categories(crawlCategory())
    #insert_ebooks(crawlAllEbook())
    for i in range(3, 501):
        print update_ebook_and_add_bookcat(crawlInforEbook(getEbooksId(i)[0]))
    #for i in range(100, 501):
     #    print insert_images(crawImagesOfChapter(getChapterById(i)[0]))
    #pass