# coding=utf-8
__author__ = 'tac_nakadai'

#coding: UTF-8

print "C:¥My Document¥node¥track¥test.txt"
print r"C:¥My Document¥node¥track¥test.txt"

print "11 & 14 = ", 11 & 14
print "10 | 12 = ", 10 | 12
print "10 ^ 12 = ", 10 ^ 12
print "~ 10 = ", ~ 10
print "~ 11 = ", ~ 11
print "~ 100 = ", ~ 100

#############
# Variable

print "#### Variable ####"

pref1 = u"東京"
pref2 = pref1

print pref1, pref2

pref1 = u"大阪"

print pref1, pref2

list1 = [1, 2]
list2 = list1

list1.append(3)

print list1
print list2