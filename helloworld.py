#!/usr/bin/env python
# -*- coding: utf-8 -*-
#helloworld.py


print 'hello,world'

#name=raw_input()
#print 'hello,',name

#name=raw_input('please enter your name:')
#print 'hello,',name

# a=-1
# if a>0:
  # print a
# else:
  # print -a
# age=20
# if age >=18:
    # print 'adult'
# else:
    # print 'teenager'
	
a='abc'
b=a
a='XYZ'
print b #abc

ord('a')#65
chr(65)#A


print u'中文'
#中文
u'中'
#u'\u4e2d'

u'ABC'.encode('utf-8')
#'ABC'
u'中文'.encode('utf-8')
#'\xe4\xb8\xad\xe6\x96\x87'

print 'hi,%s,you have $%d'%('dai',1000)


age=20
if age>=6:
    print u'少年'
elif age >=18:
    print u'成年'
else:
    print 'kid'

names=['michael','bob','tracy']
for name in names:
    print name
	
print '========================='
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
    print sum
print u'结果为：%s'%sum
print '========================='
print range(5)
print '========================='
sum=0
for x in range(101):
    sum=sum+x
print u'结果为：%s'%sum
print '========================='
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n=n-2
print sum
print '========================='
# birth =int(raw_input('birth:'))
# if birth <2000:
    # print u'00前'
# else:
    # print u'00后'
print '========================='



def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print my_abs(10)
print '========================='
import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print x,y,math.pi
print '========================='

def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print power(5,2)
print '========================='

def add_end(l=[]):
    l.append('end')
    return l
print add_end()
print add_end()
print '========================='

def add_end2(l=None):
    if l is None:
        l=[]
    l.append('end')
    return l
print add_end2()
print add_end2()
print '========================='
#请计算a2 + b2 + c2 + ……
def calclist(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print calclist([1,3,5,7])
print calc(1,3,5,7)
print '========================='

def fact_bak(n):
    if n==1:
        return 1
    return n*fact(n-1)
#print fact(1000)

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return produc
    return fact_iter(num-1,num*product)
#print fact(1000)
print '========================='   
import os
print [d for d in os.listdir('.')]

print '========================='   

l=['Aa','bB',18,'c']
print [s.lower() for s in l if isinstance(s,str)]
print '========================='   

def add(x,y,f):
    return f(x)+f(y)
	
print add(-5,6,abs)
print '========================='   

def f(x):
    return x*x
print map(f,[1,2,3,4,5,6,7,8,9])
print '=========================' 
#import string
def wgwca(x):
    return x.capitalize()
def wgw(x):
    return [x[0].upper()+x[1:].lower()]
#print map(wgw,['ada','bdad','ccc'])
print map(wgwca,['ada','bdad','ccc'])
print map(lambda x:x.capitalize(),['adam','LISA','barT'])
print '=========================' 

def prod(x,y):
    return x*y
print reduce(prod,[1,2,3,4])
def prodd(L):
    return reduce(lambda x, y: x*y, L)
print(prodd([1, 2, 3, 4]))
print '=========================' 
def is_odd(n):
    return n%2==0
print filter(is_odd,[1,2,3,4,5,6,7,8,9])

def sushu(n):
    flag=0
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            flag=1
            break
    if flag==0:
        return n
    
print filter(sushu,range(1,15))

print '=========================' 
def cmp_case(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0
print sorted(['bob','about','Zoo','Credit'],cmp_case)
print '========================='


def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f=lazy_sum(1,3,5,7,9)
f2=lazy_sum(1,3,5,7,9)
print f()
print f2()
print f==f2
print '========================='

def build(x,y):
    return lambda:x*x+y*y
print build(5,5)()
print '========================='

def log(f):
    def wrapper(*args,**kw):
        print 'call %s()'%f.__name__
        return f(*args,**kw)
    return wrapper


def logtext(text):
    def decorator(f):
        def w(*a,**k):
            print '%s,%s():'%(text,f.__name__)
            return f(*a,**k)
        return w
    return decorator



def logwn(text):
    def decorator(f):
        def w(*a,**k):
            print 'begin call'
            print '%s,%s()'%(text,f.__name__)
            execute =f(*a,**k)
            print 'end call'
            return execute 
        return w
    if isinstance(text,str):
        return decorator
    f=text
    text='execute'
    return decorator(f)

@logwn('111')
def now():
    print '2013-12-15'
now()
print '========================='
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print ''

bartee=Student('ddd',60)
print bartee.name