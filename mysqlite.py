#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
#create table if not exists user (id varchar(20) primary key, name varchar(20))
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

#cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
#print cursor.rowcount

cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print values
cursor.close()
conn.commit()
conn.close()