#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-16 10:50:07
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
#from transwarp.orm import Model,StringField,IntergerField
#import Model

class Model(dict):
	"""docstring for Model"""
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
	def __setattr__(self,key,value):
		self[key]=value



