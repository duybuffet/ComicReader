__author__ = 'zero'

import urllib
from bs4 import BeautifulSoup

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
        listCategory.append(element.text)
        print element.text

    return listCategory