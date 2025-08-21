#КЕГЭ 
#типичный представитель fnmatch

from fnmatch import*

for n in range(37, 10**8, 37):
    if fnmatch(str(n), '2*1234?6'):
        print(n, n // 37)
