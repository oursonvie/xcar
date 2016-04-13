# -*- coding: utf-8 -*-

# crawler module

from BeautifulSoup import BeautifulSoup
import urllib2
import codecs

def readlink(link):
    response = urllib2.urlopen(link)
    html = response.read()
    pagecontent = BeautifulSoup(html, fromEncoding='gb18030')
    return pagecontent