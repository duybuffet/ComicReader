__author__ = 'zero'

import urllib
import urllib2
from bs4 import BeautifulSoup
import os
import sys
import datetime

parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, parentdir)

env = "comic.settings"

# setup_environ(settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from comicreader.models import *

def crawlCategory():
    """
    crawl only category of http://blogtruyen.com
    :return: list all category
    """
    print "----->  crawlCategory()"
    html = urllib.urlopen("http://blogtruyen.com/danhsach/tatca")
    soup = BeautifulSoup(html.read())
    ulCategory = soup.findAll('ul', {'class':'submenu category'})
    liCategory = ulCategory[0].findAll('li')
    listCategory = []
    for element in liCategory:
        cat = Category(name= element.text )
        listCategory.append(cat)
    return listCategory


def maxPage():
    """
    find max page
    :return: max page
    """
    URL = "http://blogtruyen.com/ListStory/GetListStory"
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
    data = urllib.urlencode({'Url' : 'tatca', 'OrderBy' : '1', 'PageIndex' : '1'})
    html = opener.open(URL, data=data)
    soup = BeautifulSoup(html.read())
    spanPage = soup.findAll('span', {'class':'page'})
    spanEndPage = spanPage[len(spanPage)-1]
    href = spanEndPage.findAll('a')[0]['href']
    maxPage = href[20:]
    maxPage = int(maxPage[:len(maxPage)-1])
    del opener, data, html, soup, spanPage, spanEndPage, href
    return maxPage

def crawlAllEbook():
    """
    crawl url and totalchap of all ebook
    :return: list Object Ebook
    """
    print "Run crawlAllEbook()"
    URL = "http://blogtruyen.com/ListStory/GetListStory"
    try:
        listEbook = []
        for i in range(maxPage()):
            if i!=0:
                opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
                data = urllib.urlencode({'Url' : 'tatca', 'OrderBy' : '1', 'PageIndex' : i})
                html = opener.open(URL, data=data)
                soup = BeautifulSoup(html.read())
                divlist = soup.findAll('div', {'class':'list'})
                pNulls = divlist[0].findAll('p',{'class':''})

                for pNull in pNulls:
                    spans = pNull.findAll('span')
                    url = "http://blogtruyen.com"+spans[0].findAll('a')[0]['href']
                    totalChap = int(spans[1].text)
                    ebook = Ebook()
                    ebook.url = url
                    ebook.totalchap = totalChap
                    listEbook.append(ebook)
                print "====> next  %d" % i
            else:
                pass
        print "End crawlAllEbook()"
        return listEbook
    except:
        print "error! disconnect with server (method: crawlAllEbook )"


def crawlInforEbook(ebook):
    """
    crawl all information of Ebook

    :param ebook:
    :return: result = {'ebook':ebook,'categories':categories}
    ebook: object Ebook()
    categories: list categories (text)
    """
    id = ebook.id
    url = ebook.url
    print "run crawlInforEbook()"
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html.read())

    h1 = soup.findAll('h1', {'class':'entry-title'})
    name = h1[0].text

    divcontent = soup.findAll('div',{'class':'content'})
    description = divcontent[0].text

    divthumbnail = soup.findAll('div', {'class':'thumbnail'})
    cover =  divthumbnail[0].findAll('img')[0]['src']

    divDecription = soup.findAll('div',{'class':'description'})
    pNulls = divDecription[0].findAll('p')
    author = ''
    update = ''
    complete = ''
    categories = []
    for pNull in pNulls:
        #print pNull.text
        try:
            if pNull.findAll('a')[0]['class'][0]=='color-green':
                author = str(pNull.findAll('a')[0].text)
        except:
            pass

        try:
            if pNull['class'][0]=='clear-fix':
                update = str(pNull.findAll('span')[0].text)
        except:
            pass

        try:
            if pNull.findAll('span')[1]['class'][0]=='color-red':
                complete = str(pNull.findAll('span')[1].text)
        except:
            pass

        try:
            if pNull.findAll('span')[0]['class'][0]=='category':
                spancategorys = pNull.findAll('span')
                for element in spancategorys:
                    categories.append(str(element.text))
                    #print categories

        except:
            pass
    ebook_out = Ebook()
    ebook_out.id = ebook.id
    ebook_out.url =ebook.url
    ebook_out.name = name
    ebook_out.author = author
    ebook_out.cover = cover
    ebook_out.description = description
    ebook_out.update = datetime.datetime.strptime(update,'%d/%m/%Y %H:%M')
    ebook_out.complete = 0
    #print complete
    result = {'ebook':ebook_out,'categories':categories}
    print categories
    print "end crawlInforEbook()"
    return  result


def crawlChaptersOfEbook(ebook):
    """
    crawl all chap of ebook
    :param ebook:
    :return: list Chapter
    """
    print "Run crawlChaptersOfEbook"
    listChapters = []
    id = ebook.id
    url = ebook.url
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html.read())
    divListchapters = soup.findAll('div',{'id':'list-chapters'})
    pNulls = divListchapters[0].findAll('p')
    for pNull in pNulls:
        spanTitle = pNull.findAll('span',{'class':'title'})
        name = spanTitle[0].text
        url = "http://blogtruyen.com"+spanTitle[0].findAll('a')[0]['href']

        spanPublishedDate = pNull.findAll('span',{'class':'publishedDate'})
        update = spanPublishedDate[0].text

        chapter = Chapter()
        chapter.name = name
        chapter.url = url
        chapter.update = datetime.datetime.strptime(update,'%d/%m/%Y %H:%M')
        listChapters.append(chapter)
    result = {"ebook_id" : id, "chapters" : listChapters}
    print "End crawlChaptersOfEbook"
    return result

def getName(url):
    """
    fix name image
    :param url: url of image
    :return:name of image
    """
    subUrl = url.split('/')
    max = len(subUrl)
    oldname = subUrl[max-1]
    newname = oldname.split("?")[0]
    return newname

def crawImagesOfChapter(chapter):
    """
    crawl all images of a chapter
    :return: list Image
    """
    print "run crawlImagesOfChapter"
    listImages = []
    id = chapter.id
    url = chapter.url
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html.read())
    articleContent = soup.findAll('article',{'id':'content'})
    imgs = articleContent[0].findAll('img')
    for img in imgs:
        src = img['src']
        subSrc = src.split("url=")
        url = ''
        if len(subSrc)>1:
            url = subSrc[1]
        else:
            url = src
        image = Image()
        image.url = url
        image.name = getName(url)
        listImages.append(image)
    result = {"chapter_id":id, "images":listImages}
    print "end crawlImagesOfChapter"
    return result