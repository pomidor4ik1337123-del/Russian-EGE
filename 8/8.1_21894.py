#КЕГЭ 21894

from itertools import*

c = 0
chet = '02468'
nechet = '13579'
for i in permutations('0123456789', 4):
    a = ''.join(i)
    if a[0] != '0':
        if (a[0] in chet and a[1] in nechet and a[2] in chet and a[3] in nechet) or (a[0] in nechet and a[1] in chet and a[2] in nechet and a[3] in chet):
            print(a)
            c += 1
print(c)
