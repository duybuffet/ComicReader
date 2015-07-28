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


if __name__ == '__main__':
    # insert_categories(crawlCategory())
    insert_ebooks(crawlAllEbook())

    #pass