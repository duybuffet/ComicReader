from django.shortcuts import render
from django.http import HttpResponse
import json
import models
from scripts import database_query_utility
from comicreader.constants import *
# Create your views here.

def index(request):
    pass

def getebook(request):
    ebook_id = request.REQUEST.get('ebook_id')
    if request.method =='GET':
        id = int(ebook_id)
        ebooks = database_query_utility.getEbooksId(id)
        if len(ebooks)>0:
            name = ebooks[0].name
            data = {'ebook_id': ebooks[0].id, 'ebook':{'id': ebooks[0].id,'name': ebooks[0].name,'cover': ebooks[0].cover, 'description': ebooks[0].description,'author': ebooks[0].author}}
            data_json = json.dumps(data)
            return HttpResponse(data_json, content_type='application/json', status=200)
        else:
            data = {'error': 'Data not found'}
            data_json = json.dumps(data)
            return HttpResponse(data_json, content_type='application/json', status=404)
    else:
        pass

#--------------dang sua--------------

def listEbooks(request):
    type = request.REQUEST.get('type')
    search_type = request.REQUEST.get('search_type')
    key_word = request.REQUEST.get('key_word')
    if request.method == 'GET':
        response_data = {}
        response_data['result'] = 'failed'
        response_data['message'] = 'You messed up'
        listEbook = []
        if type == API_KEYWORD_TYPE_NEW:
            # false
            listAllEbook = database_query_utility.getEbooks()
            totalEbook = len(listAllEbook)
            for i in range(totalEbook-6, totalEbook-1):
                listEbook.append(listAllEbook[i])
        elif type == API_KEYWORD_TYPE_CATEGORY:
            listEbook = database_query_utility.getEbooksByCategoy(key_word)
        elif type == API_KEYWORD_TYPE_READ_MOST:
            listEbook = database_query_utility.getEbooksByView()
        elif type == API_KEYWORD_TYPE_FAVORITE:
            listEbook = database_query_utility.getEbooksByFavorite()
        elif type == API_KEYWORD_TYPE_SEARCH:
            if search_type == API_KEYWORD_SEARCH_TYPE_AUTHOR:
                listEbook = database_query_utility.getEbooksByNameAuthor(key_word)
            elif search_type == API_KEYWORD_SEARCH_TYPE_EBOOK:
                listEbook = database_query_utility.getEbookByNameEbook(key_word)
            else:
                pass
        else:
            pass
        response = HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
        return  response
    else:
        pass



def get_chapter(request):
    """
    :param request:
    :param chapter_id:
    :return:
    """
    chapter_id = request.REQUEST.get('chapter_id', '')
    response_data = {}
    if request.method == 'GET':
        images_o = []
        images = database_query_utility.get_images_of_chapter(chapter_id)
        for image in images:
            images_o.append(image)

        response_data['chapter_id'] = chapter_id
        response_data['images'] = images_o
        response = HttpResponse(json.dumps(response_data), content_type="application/json", status=200)

        return response
    else:
        response_data['error'] = 'NOT FOUND!'
        response = HttpResponse(json.dumps(response_data), content_type="application/json", status=404)
        return response


def feedback(request):
    chapter_id = request.REQUEST.get('chapter_id', '')
    ebook_id = request.REQUEST.get('ebook_id','')
    title = request.REQUEST.get('title', '')
    content =request.REQUEST.get('content','')
    response_data = {}
    if request.method == "GET":
        feedback = Feedback()
        feedback.ebook_id = ebook_id
        feedback.chapter_id = chapter_id
        feedback.title = title
        feedback.description = content
        print database_query_utility.insert_feedback(feedback)
        response_data['masseger'] = 'FeedBack successful'
        response = HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
        return response

    else:
        response_data['error'] = 'Request error!'
        response = HttpResponse(json.dumps(response_data), content_type="application/json", status=404)
        return response
