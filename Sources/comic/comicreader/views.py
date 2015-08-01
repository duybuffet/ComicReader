from django.shortcuts import render
from django.http import HttpResponse
import json
from comicreader.models import *
from scripts import database_query_utility
from comicreader.constants import *
# Create your views here.

def index(request):
    pass

def getebook(request):
    ebook_id = request.REQUEST.get('ebook_id')
    if request.method =='GET':
        ebook = database_query_utility.getEbookById(ebook_id)
        if len(ebook)>0:
            data = {'ebook_id': ebook[0]['id'], 'ebook':{'id': ebook[0]['id'], 'name': ebook[0]['name'], 'cover': ebook[0]['cover'], 'description': ebook[0]['description'],'author': ebook[0]['author']}}
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
    #     "type": <type>
    # "search_type": <search_type>
    # "key_word": <key_word>
    # "ebooks"    : [{id :<id_ebook>, cover : <cover>, name : <name>, update : <update>}]

        response_data['type'] = type
        response_data['search_type'] = search_type
        response_data['key_word'] = key_word
        listEbook = []
        if type == API_KEYWORD_TYPE_NEW:
            Ebooks = database_query_utility.getEbooksNew()
            for ebook in Ebooks:
                listEbook.append(ebook)
        elif type == API_KEYWORD_TYPE_CATEGORY:
            Ebooks = database_query_utility.getEbooksByCategoy(key_word)
            for ebook in Ebooks:
                listEbook.append(ebook)
        elif type == API_KEYWORD_TYPE_READ_MOST:
            Ebooks = database_query_utility.getEbooksByView()
            for ebook in Ebooks:
                listEbook.append(ebook)
        elif type == API_KEYWORD_TYPE_FAVORITE:
            Ebooks = database_query_utility.getEbooksByFavorite()
            for ebook in Ebooks:
                listEbook.append(ebook)
        elif type == API_KEYWORD_TYPE_SEARCH:
            if search_type == API_KEYWORD_SEARCH_TYPE_AUTHOR:
                Ebooks = database_query_utility.getEbooksByNameAuthor(key_word)
                for ebook in Ebooks:
                    listEbook.append(ebook)
            elif search_type == API_KEYWORD_SEARCH_TYPE_EBOOK:
                Ebooks = database_query_utility.getEbookByNameEbook(key_word)
                for ebook in Ebooks:
                    listEbook.append(ebook)
            else:
                data = {'error': 'Data not found'}
                data_json = json.dumps(data)
                return HttpResponse(data_json, content_type='application/json', status=404)
        else:
            data = {'error': 'Data not found'}
            data_json = json.dumps(data)
            return HttpResponse(data_json, content_type='application/json', status=404)
        response_data['ebooks'] = listEbook
        response = HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
        return  response
    else:
        data = {'error': 'Data not found'}
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json', status=404)



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


def listChapter(request):
    ebook_id = request.REQUEST.get('ebook_id')
    if request.method =='GET':
        id = int(ebook_id)
        chapters = database_query_utility.getAllChapterEbook(id)
        if len(chapters)>0:
                data = []
                for idx in range(len(chapters)):
                    data.append({'ebook_id': ebook_id, 'chapters':{'chapter_id': chapters[idx]['id'],'name': chapters[idx]['name']}})
                    data_json = json.dumps(data)
                return HttpResponse(data_json, content_type='application/json', status=200)
        else:
            data = {'error': 'Data not found'}
            data_json = json.dumps(data)
            return HttpResponse(data_json, content_type='application/json', status=404)
    else:
        pass


def get_image(request):
    try:
        mime_type = ""
        flag = True
        real_path = database_query_utility.get_image_path_by_id(request.REQUEST.get("image_id"))
        if real_path:
            mime_type = get_mime_type(real_path)
        else:
            flag = False
    except:
        flag = False

    if flag:
        return HttpResponse(open(real_path,'rb'), content_type=mime_type, status=200)
    else:
        data = {'error': 'Data not found'}
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json', status=404)


def get_mime_type(real_path):
    mime_type = ""
    if real_path.endswith(".jpg") | real_path.endswith(".jpeg"):
        mime_type = "image/jpeg"
    elif real_path.endswith(".png"):
        mime_type = "image/png"
    elif real_path.endswith(".bm") | real_path.endswith(".bmp"):
        mime_type = "image/bmp"
    elif real_path.endswith(".gif"):
        mime_type = "image/gif"
    elif real_path.endswith(".ico"):
        mime_type = "image/x-icon"
    else:
        mime_type = "application/force-download"
    return mime_type