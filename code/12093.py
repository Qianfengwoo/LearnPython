#!/usr/bin/env python
#coding:utf-8

string = 'I love  code.'
print string


str_lst = string.split(' ')
print str_lst

#words = [s.strip() for s in str_lst]  #这个方法不成功，为什么？
words = [s for s in str_lst if s!='']
print words

new_string = ' '.join(words)
print new_string
