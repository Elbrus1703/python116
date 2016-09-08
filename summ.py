# -*- coding: utf-8 -*-
from random import randint
print "rand - ", randint(0,9)
n = 0 
summ = 0 
while n <= 100:
	ostatok = n % 2 
	if ostatok == 0:
		summ = summ + n 
		print "=====" + str(n)
		print summ
		n = n + 1
print "******************"
print summ 