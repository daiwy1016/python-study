#!/usr/bin/env python
#-*- coding:utf-8 -*-
# db.py
import threading

class _Engine(object):
    """docstring for _Engine"""

    def __init__(self, connect):
        self.connect = connect

    def connect(self):
        return self._connect()

engine = None


class _DbCtx(threading.local):
    """docstring for _DbCtx"""
    def __init__(self):
        self.connection = None
        self.transactions = 0
    def is_init(self):
        return not self.connection is None#判断是否已经进行了初始化
    def init(self):
        self.connection = _LasyConnection()#打开一个数据库链接
        self.transactions = 0
    def cleanup(self):
        self.connection.cleanup()
        self.connection = None
    def cursor(self):
        return self.connection.cursor()

_db_ctx = _DbCtx()

class _ConnectionCtx(object):
	def __enter__(self):#在使用with语句时调用，会话管理器在代码块开始前调用，返回值与as后的参数绑定
		global _db_ctx
		self.should_cleanup=False
		if not _db_ctx.is_init():
			_db_ctx.init()
			self.should_cleanup=True
		return self
	def __exit__(self,exctype,excvalue,traceback):#会话管理器在代码块执行完成好后调用，在with语句完成时，对象销毁之前调用
		global _db_ctx
		if self.should_cleanup:
			_db_ctx.cleanup()
def connection():
	return _ConnectionCtx()

class _TransationCtx(object):
	def __enter__(self):
		global _db_ctx
		self.should_close_conn=False
		if not _db_ctx.is_init():
			_db_ctx.init()
			self.should_close_conn=True
		_db_ctx.transations=_db_ctx.transactions+1
		return self
	def __exit__(self,exctype,excvalue,traceback):
		global _db_ctx
		_db_ctx.transactions=_db_ctx.transations-1
		try:
			if _db_ctx.transactions==0:
				if exctype is None:
					self.commit()
				else:
					self.rollback()
		finally:
			if self.should_close_conn:
				_db_ctx.cleanup()
	def commit(self):
		global _db_ctx
		try:
			_db_ctx.connection.commit()

		except:
			_db_ctx.connection.rollback()
			raise
	def  rollback(self):
		global _db_ctx
		_db_ctx.connection.rollback()
