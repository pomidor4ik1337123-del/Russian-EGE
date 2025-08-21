#КЕГЭ 21717

a = open('24_21717 (1).txt').readline()
m = 10000
for l in range(len(a)):
    for r in range(l + m, l, -1):
        c = a[l:r+1]
        if c.count('RSQ') < 130:
            break
        elif c.count('RSQ') == 130 and c[-1] != 'Q':
            m = min(m, len(c))
print(m)
