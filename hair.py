#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Grandfa(object):
    def hair(self):
        print 'no hair'
class Father(object):
    pass
class Mon(object):
    def hair(self):
        print 'hair'
class Tom(Father,Mon):
    pass
me=Tom()
me.hair()
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
       return 'Student object (name:%s)'%self.name
    __repr__= __str__

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if(self.a>10):
            raise StopIteration();
        return self.a
for n in Fib():
    print n
    
    
class Chain(object):
    def __init__(self,path=''):
        self.path=path
    def __getattr__(self,path):
        return Chain('%s%s'%(self.path,path))
    def __str__(self):
        return self.path
print Chain().status