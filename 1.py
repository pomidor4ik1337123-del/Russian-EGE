from itertools import*

a = '234 136 12 157 467 25 45'.split()
s = 'CE CG EG EA GF AD DF FB BD'.split()
print('1 2 3 4 5 6 7')
for p in permutations('ABCDEFG'):
    if all(str(p.index(x)+1) in a[p.index(y)] for x, y in s):
        print(*p)
