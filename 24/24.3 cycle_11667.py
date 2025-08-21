#КЕГЭ 11667
#дефолтное достаточно задание

a = open('24_11667.txt').readline()
m = 0
for l in range(len(a)):
    for r in range(l + m, len(a)):
        c = a[l:r+1]
        if c.count('INFINITY') > 1000:
            break
        elif c.count('INFINITY') == 1000:
            m = max(m, len(c))

print(m)
