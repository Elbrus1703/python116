# -*- coding: utf-8 -*-

from random import random
n = round(random() * 100)
i = 0
print u("Компьютер загадал число. Отгадайте его. У вас 5 попыток")
while i <= 6:
 u = int(input(str(i) + '-я попытка: '))
if u > n:
        print u('не верно')
    elif u < n :
        print u('не верно')
    else:
        print u('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print u('Вы исчерпали 5 попыток. Было загадано', n)
