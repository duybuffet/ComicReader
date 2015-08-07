from django.shortcuts import render
from django.http import HttpResponse
import json
from comicreader.models import *
from scripts import database_query_utility
from comicreader.constants import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    pass

def getebook(request):
    ebook_id = request.REQUEST.get('ebook_id')
    if request.method =='GET':
        ebook = database_query_utility.getEbookById(ebook_id)
        if len(ebook)>0:
            data = {'ebook_id': ebook[0]['id'], 'ebook':{'id': ebook[0]['id'], 'name': ebook[0]['name'], 'cover': database_query_utility.convertCover(ebook[0]['cover']), 'description': ebook[0]['description'],'author': ebook[0]['author'],'update': database_query_utility.convertDate(str(ebook[0]['update']))}}
            data_json = json.dumps(data)
            return HttpResponse(data_json, content_type='application/json', status=200)
        else:
            data = {'error': 'Data not found'}
            data_json = json.dumps(data)
            return HttpResponse(data_json, content_type='application/json', status=404)
    else:
        data = {'error': 'Data not found'}
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json', status=404)

def getCategory(request):
    if request.method =='GET':
        data = database_query_utility.getTotalEbookInCategory()
        if len(data)>0:
            data_json = json.dumps(data)
            return HttpResponse(data_json, content_type='application/json', status=200)
        else:
            data = {'error': 'Data not found'}
            data_json = json.dumps(data)
            return HttpResponse(data_json, content_type='application/json', status=404)
    else:
        data = {'error': 'Data not found'}
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json', status=404)


def listEbooks(request):
    type = request.REQUEST.get('type')
    search_type = request.REQUEST.get('search_type')
    key_word = request.REQUEST.get('key_word')

    if request.REQUEST.get('page'):
        page = int(request.REQUEST.get('page'))
    else:
        page = 1

    if request.method == 'GET':
        response_data = {}
        response_data['type'] = type
        response_data['search_type'] = search_type
        response_data['page'] = page
        response_data['max_page'] = 'False'
        ebooks = []
        if type == API_KEYWORD_TYPE_NEW:
            pages = Paginator(database_query_utility.getEbooksNew(),API_LIMIT_ELEMENT_PAGE)
            if page <= pages.num_pages and page>0:
                ebooks = pages.page(page).object_list
            else:
                response_data['max_page'] = 'True'
        elif type == API_KEYWORD_TYPE_CATEGORY:
            pages =  Paginator(database_query_utility.getEbooksByCategoy(key_word),API_LIMIT_ELEMENT_PAGE)
            if page <= pages.num_pages and page>0:
                ebooks = pages.page(page).object_list
            else:
                response_data['max_page'] = 'True'
        elif type == API_KEYWORD_TYPE_READ_MOST:
            pages = Paginator(database_query_utility.getEbooksByView(),API_LIMIT_ELEMENT_PAGE)
            if page <= pages.num_pages and page>0:
                ebooks = pages.page(page).object_list
            else:
                response_data['max_page'] = 'True'
        elif type == API_KEYWORD_TYPE_FAVORITE:
            pages = Paginator(database_query_utility.getEbooksByFavorite(),API_LIMIT_ELEMENT_PAGE)
            if page <= pages.num_pages and page>0:
                ebooks = pages.page(page).object_list
            else:
                response_data['max_page'] = 'True'
        elif type == API_KEYWORD_TYPE_HOT:
            pages = Paginator(database_query_utility.getEbooksHot(),API_LIMIT_ELEMENT_PAGE)
            if page <= pages.num_pages and page>0:
                ebooks = pages.page(page).object_list
            else:
                response_data['max_page'] = 'True'
        elif type == API_KEYWORD_TYPE_SEARCH:
            if search_type == API_KEYWORD_SEARCH_TYPE_AUTHOR:
                pages = Paginator(database_query_utility.getEbooksByNameAuthor(key_word),API_LIMIT_ELEMENT_PAGE)
                if page <= pages.num_pages and page>0:
                    ebooks = pages.page(page).object_list
                else:
                    response_data['max_page'] = 'True'
            elif search_type == API_KEYWORD_SEARCH_TYPE_EBOOK:
                pages = Paginator(database_query_utility.getEbooksByNameEbook(key_word),API_LIMIT_ELEMENT_PAGE)
                if page <= pages.num_pages and page>0:
                    ebooks = pages.page(page).object_list
                else:
                    response_data['max_page'] = 'True'
            else:
                data = {'error': 'Data not found'}
                data_json = json.dumps(data)
                return HttpResponse(data_json, content_type='application/json', status=404)
        elif type == API_KEYWORD_TYPE_NULL:
            ebooks = database_query_utility.getAllEbook()
        else:
            data = {'error': 'Data not found'}
            data_json = json.dumps(data)
            return HttpResponse(data_json, content_type='application/json', status=404)

        response_data['ebooks'] = ebooks
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
                    data.append({'chapter_id': chapters[idx]['id'], 'total': database_query_utility.getTotalImageInChapter(chapters[idx]['id']),'name': chapters[idx]['name'],'update': database_query_utility.convertDate(str(chapters[idx]['update']))})
                data_json = json.dumps({'ebook_id': ebook_id, 'chapters':data})
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

def get_ebooks_by_category(request):
    category_id = request.GET.get("category_id")
    if request.REQUEST.get('page'):
        page = int(request.REQUEST.get('page'))
    else:
        page = 1
    response_data = {}
    response_data['category_id'] = category_id
    response_data['max_page'] = 'False'
    ebooks=[]
    if request.method == 'GET':
        pages = Paginator(database_query_utility.get_ebooks_by_cat(category_id),API_LIMIT_ELEMENT_PAGE)
        if page <= pages.num_pages and page>0:
            ebooks = pages.page(page).object_list
        else:
            response_data['max_page'] = 'True'
        # print data
        response_data['ebooks'] = ebooks
        response = HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
        return response
    else:
        data = {'error': 'Data not found'}
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json', status=404)
