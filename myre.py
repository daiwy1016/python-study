#/usr/bin/env python
#-*- coding:utf-8 -*-
import re
s='408366645@qq.com'
m=re.match(r'^[0-9a-zA-Z\.]+@(qq|gmail).com$',s)
print m.group(0)

from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print p.x

import base64
print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')


def b64decode_self(str):
    return base64.b64decode(str+'='*(4-len(str)%4))
    
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some &nbsp;<a href=\"#\">html</a> tutorial...<br>END</p></body></html>')