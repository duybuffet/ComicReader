__author__ = 'sang'

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^ebook', views.getebook, name='get-ebooks'),
    #/ebook?ebook_id=3
    url(r'^listebook', views.listEbooks, name='list-ebooks'),
    #/listebook?type=search&search_type=author&key_word=abc

    #url get images of chapter by index
    url(r'^chapter/$', views.get_chapter, name= 'Chapter_byID'),
    #url receive feedback from user
    url(r'^feedback/$', views.feedback, name= 'FeedBack'),
    url(r'^image/$', views.get_image, name='GetImage'),
]