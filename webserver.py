#!/usr/bin/env python
#-*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
from helloweb import application
httpd=make_server('',8000,application)
print 'servering http on port 8000...'
httpd.serve_forever()