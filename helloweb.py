#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def application(environ,start_respones):
    method=environ['REQUEST_METHOD']
    print method
    start_respones('200 OK',[('Content-Type','text/html;charset=utf-8')])
    utext=u'<h1>hello %s!</h>'%(environ['PATH_INFO'][1:] or 'web')
    return utext.encode('utf-8')