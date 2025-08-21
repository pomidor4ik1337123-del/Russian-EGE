#КЕГЭ 10921

from itertools import*
сс = 0
glas = 'АИ'
for i in product('ДЖАВАСКРИПТ',repeat=11):
    a = ''.join(i)
    c = 0
    for j in range(len(a)):
        if a[j] in glas:
            c += j+1
    if c == 11:
        сс += 1
        print(a)
print(сс)
