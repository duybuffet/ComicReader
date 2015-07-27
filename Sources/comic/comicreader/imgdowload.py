from struct import pack
import urllib

__author__ = 'sang'
import os

PATH_DATA_IMAGE='/home/sang/Projects/ComicReader/Downloads/images/'
urls = [
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjo6h37YI/AAAAAAAAE9w/eawu2sxl5aI/Naruto%20chap%201-NARUTO01_-001.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjrjYcKZI/AAAAAAAAE-A/fNoh2eISyIo/Naruto%20chap%201-NARUTO01_-002.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjscWodPI/AAAAAAAAE-M/gAVGVYLNDt0/Naruto%20chap%201-NARUTO01_0003.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjvmn_GnI/AAAAAAAAE-k/8xXIl2BL17o/Naruto%20chap%201-NARUTO01_0004-0005.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjwBccEWI/AAAAAAAAE-w/Sv7ImkU-O1M/Naruto%20chap%201-NARUTO01_0008.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjxL0l8tI/AAAAAAAAE-4/15oVoSB673A/Naruto%20chap%201-NARUTO01_0009.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjxx-odyI/AAAAAAAAE_A/CIUcjSdp8hs/Naruto%20chap%201-NARUTO01_0010.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjyblhixI/AAAAAAAAE_Q/XZB-MjGN3do/Naruto%20chap%201-NARUTO01_0011.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjzFSfUrI/AAAAAAAAE_Y/f9Wpdt1dpRc/Naruto%20chap%201-NARUTO01_0012.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQjz__EhYI/AAAAAAAAE_g/ABX3C4H9vHo/Naruto%20chap%201-NARUTO01_0013.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj0rHC59I/AAAAAAAAE_s/ubhP2iJAQmE/Naruto%20chap%201-NARUTO01_0014.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj1E1MItI/AAAAAAAAE_0/OUUEvNxMUv4/Naruto%20chap%201-NARUTO01_0015.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj1_0GAQI/AAAAAAAAE_4/i9cQNIvoIok/Naruto%20chap%201-NARUTO01_0016.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj2vqsRrI/AAAAAAAAFAA/IIYPRV9lHJM/Naruto%20chap%201-NARUTO01_0017.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj36ebRoI/AAAAAAAAFAI/4lRs7Nb_HGI/Naruto%20chap%201-NARUTO01_0018.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj4swM8hI/AAAAAAAAFAM/ezWYzu3Uryw/Naruto%20chap%201-NARUTO01_0019.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj5l5wD5I/AAAAAAAAFAQ/j6U44C5dI2k/Naruto%20chap%201-NARUTO01_0020.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj6Uu8jUI/AAAAAAAAFAc/Hm3jvI5S1C4/Naruto%20chap%201-NARUTO01_0021.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj7I1mjeI/AAAAAAAAFAg/474gikRZpJ0/Naruto%20chap%201-NARUTO01_0022.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj73nzoMI/AAAAAAAAFAk/Mw1qgvRBoCg/Naruto%20chap%201-NARUTO01_0023.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj8cE2XXI/AAAAAAAAFAs/tLagHv4NPFw/Naruto%20chap%201-NARUTO01_0024.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj9NP5ChI/AAAAAAAAFA0/SQ0BROjf7T4/Naruto%20chap%201-NARUTO01_0025.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj9yTG3TI/AAAAAAAAFA8/53NlMkvrDJ8/Naruto%20chap%201-NARUTO01_0026.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj-kM992I/AAAAAAAAFBg/I-fV4roitHg/Naruto%20chap%201-NARUTO01_0027.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQj_lZJ1jI/AAAAAAAAFBw/w3qTCp5lQdA/Naruto%20chap%201-NARUTO01_0028.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkAs0kohI/AAAAAAAAFB0/Buargz54ml4/Naruto%20chap%201-NARUTO01_0029.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkBLEVN4I/AAAAAAAAFB8/8Nq5SHFA0b0/Naruto%20chap%201-NARUTO01_0030.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkDtPnPyI/AAAAAAAAFCE/n2Iw6LYV9oQ/Naruto%20chap%201-NARUTO01_0031.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkEQQ1EWI/AAAAAAAAFCM/0X_p0r-bI9E/Naruto%20chap%201-NARUTO01_0032.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkEwfvlrI/AAAAAAAAFCQ/gBXcUKqmGDE/Naruto%20chap%201-NARUTO01_0033.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkFhJIsfI/AAAAAAAAFCY/bA37s0wJacA/Naruto%20chap%201-NARUTO01_0034.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkGKaD9KI/AAAAAAAAFCg/oq1QGv9mCKo/Naruto%20chap%201-NARUTO01_0035.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkG8GiTrI/AAAAAAAAFCo/fboitiKPcqM/Naruto%20chap%201-NARUTO01_0036.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkHmF-8UI/AAAAAAAAFCs/MzbLUIGdJmo/Naruto%20chap%201-NARUTO01_0037.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkIJQ5hII/AAAAAAAAFC0/mj3vQMrSzRg/Naruto%20chap%201-NARUTO01_0038.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkIx5YP7I/AAAAAAAAFC4/dzIUhVNY4Is/Naruto%20chap%201-NARUTO01_0039.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkJf8-n7I/AAAAAAAAFDA/sReiPfR51io/Naruto%20chap%201-NARUTO01_0040.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkJyA52jI/AAAAAAAAFDE/B_0LZJWBeJo/Naruto%20chap%201-NARUTO01_0041.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkKpCWqkI/AAAAAAAAFDM/GZK9Ja0sC2Q/Naruto%20chap%201-NARUTO01_0042.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkLY9QPiI/AAAAAAAAFDU/IfIA4tWWrJA/Naruto%20chap%201-NARUTO01_0043.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkMDYsuxI/AAAAAAAAFDY/0TIFWlcPI6Y/Naruto%20chap%201-NARUTO01_0044.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkNHE2QzI/AAAAAAAAFDg/wweplqx9EeY/Naruto%20chap%201-NARUTO01_0045.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkNw2rM1I/AAAAAAAAFDw/R10ownc8U6Y/Naruto%20chap%201-NARUTO01_0046.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkORDe37I/AAAAAAAAFD4/t1vRRcSvFVw/Naruto%20chap%201-NARUTO01_0047.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkO21-kCI/AAAAAAAAFEA/FFrQCDeopMg/Naruto%20chap%201-NARUTO01_0048.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkPxrEAeI/AAAAAAAAFEM/VC4aM5TAE4Q/Naruto%20chap%201-NARUTO01_0049.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkQieXrxI/AAAAAAAAFEU/nfoMONef3GY/Naruto%20chap%201-NARUTO01_0050.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkRVzNTYI/AAAAAAAAFEc/zrAgPLc4AZk/Naruto%20chap%201-NARUTO01_0051.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkSHJ_54I/AAAAAAAAFEk/W1tle9Dq0jo/Naruto%20chap%201-NARUTO01_0052.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkS4BCIHI/AAAAAAAAFEw/sYr_fbG0dWw/Naruto%20chap%201-NARUTO01_0053.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkT6BBYYI/AAAAAAAAFE8/gCqVvylhSyE/Naruto%20chap%201-NARUTO01_0054-0055.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkUpsf9tI/AAAAAAAAFFE/N_8Id1gpFuk/Naruto%20chap%201-NARUTO01_0056.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkVXMzFKI/AAAAAAAAFFU/c1geBjTB3Zw/Naruto%20chap%201-NARUTO01_0057.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkV9WlKyI/AAAAAAAAFFY/tgtTd14-IfU/Naruto%20chap%201-NARUTO01_0058.jpg?imgmax=3000',
    'http://2.bp.blogspot.com/_93k9xmLQtxc/TdQkWkGjmXI/AAAAAAAAFFg/UEbDykpiiUU/Naruto%20chap%201-NARUTO01_0059.jpg?imgmax=3000',
]
imagename = [
    'NARUTO01_-0001.jpg',
    'NARUTO01_-0002.jpg',
    'NARUTO01_-0003.jpg',
    'NARUTO01_-0004-005.jpg',
    'NARUTO01_-0006.jpg',
    'NARUTO01_-0007.jpg',
    'NARUTO01_-0008.jpg',
    'NARUTO01_-0009.jpg',
    'NARUTO01_-0010.jpg',
    'NARUTO01_-0011.jpg',
    'NARUTO01_-0012.jpg',
    'NARUTO01_-0013.jpg',
    'NARUTO01_-0014.jpg',
    'NARUTO01_-0015.jpg',
    'NARUTO01_-0016.jpg',
    'NARUTO01_-0017.jpg',
    'NARUTO01_-0018.jpg',
    'NARUTO01_-0019.jpg',
    'NARUTO01_-0020.jpg',
    'NARUTO01_-0021.jpg',
    'NARUTO01_-0022.jpg',
    'NARUTO01_-0023.jpg',
    'NARUTO01_-0024.jpg',
    'NARUTO01_-0025.jpg',
    'NARUTO01_-0026.jpg',
    'NARUTO01_-0027.jpg',
    'NARUTO01_-0028.jpg',
    'NARUTO01_-0029.jpg',
    'NARUTO01_-0030.jpg',
    'NARUTO01_-0031.jpg',
    'NARUTO01_-0032.jpg',
    'NARUTO01_-0033.jpg',
    'NARUTO01_-0034.jpg',
    'NARUTO01_-0035.jpg',
    'NARUTO01_-0036.jpg',
    'NARUTO01_-0037.jpg',
    'NARUTO01_-0038.jpg',
    'NARUTO01_-0039.jpg',
    'NARUTO01_-0040.jpg',
    'NARUTO01_-0041.jpg',
    'NARUTO01_-0042.jpg',
    'NARUTO01_-0043.jpg',
    'NARUTO01_-0044.jpg',
    'NARUTO01_-0045.jpg',
    'NARUTO01_-0046.jpg',
    'NARUTO01_-0047.jpg',
    'NARUTO01_-0048.jpg',
    'NARUTO01_-0049.jpg',
    'NARUTO01_-0050.jpg',
    'NARUTO01_-0051.jpg',
    'NARUTO01_-0052.jpg',
    'NARUTO01_-0053.jpg',
    'NARUTO01_-0054-0055.jpg',
    'NARUTO01_-0056.jpg',
    'NARUTO01_-0057.jpg',
]
input ={'ebookname' : 'Naruto', 'chaptername': 'Naruto Chap 002_test', 'urlimg': urls, 'nameimg': imagename }


def dirNameEbook(ebookname):

    path = os.path.join(PATH_DATA_IMAGE, ebookname)
    if not os.path.exists(path):
        os.mkdir(os.path.join(path),0755)
    else:
        print 'Folder %s exits' %ebookname
    return  path

def dirNameChapter(chaptername):

    path =  os.path.join(dirNameEbook(input['ebookname']),chaptername)
    if not os.path.exists(path):
        os.mkdir(path,0755)
    else:
        print 'Folder %s exits' %chaptername
    return  path
def dowloadImage(input):
    pass

def download_photo(path, img_url, filename):

    file_path = "%s/%s" % (path, filename)
    downloaded_image = file(file_path, "wb")
    image_on_web = urllib.urlopen(img_url)
    while True:
        buf = image_on_web.read(65536)
        if len(buf) == 0:
            break
        downloaded_image.write(buf)
    downloaded_image.close()
    image_on_web.close()
    return file_path

if __name__ == '__main__':
    path = dirNameChapter(input['chaptername'])
    print path
    url = input['urlimg']
    image= input['nameimg']
    print len(url)
    print len(image)
    for i in xrange(len(url)):
      print download_photo(path, url[i], image[i] )