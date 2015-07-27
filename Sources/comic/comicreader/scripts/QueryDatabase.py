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

for eb in Ebook.objects.raw('SELECT * FROM ebook'):
    print eb.url