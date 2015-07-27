__author__ = 'phuong'

import MySQLdb
import json

def getEbook():
    arr_book = []
    db = MySQLdb.connect(user='root',db='comicreader',passwd ='12345',host ='localhost')
    cursor = db.cursor()
    cursor.execute( 'SELECT id, url FROM ebook;')
    data = cursor.fetchall()
    for row in data :
        arr_book.append({row[0]:row[1]})
    print 'GET EBOOK', json.dumps(arr_book)
    db.close ()
    return arr_book

def getChapter():
    arr_chapter =[]
    db = MySQLdb.connect(user='root',db='comicreader',passwd ='12345',host ='localhost')
    cursor = db.cursor()
    cursor.execute( 'SELECT ebook_id, url FROM chapter;')
    data = cursor.fetchall()
    for row in data :
        arr_chapter.append({row[0]:row[1]})
    print 'GET CHAPTER', json.dumps(arr_chapter)
    db.close ()
    return  arr_chapter

def getDownload():
    arr_img = []
    db = MySQLdb.connect(user='root',db='comicreader',passwd ='12345',host ='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT a.name, b.name, c.url FROM ebook a, chapter b, image c WHERE a.id = b.ebook_id AND b.ebook_id = chapter_id;')
    data = cursor.fetchall()
    for row in data :
        arr_img.append({row[0]:[row[1],row[2]]})
    print 'GET IMG', json.dumps(arr_img)
    db.close ()
    return arr_img
if __name__ == "__main__":
    getEbook()
    getChapter()
    getDownload()

