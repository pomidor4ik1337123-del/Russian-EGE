#КЕГЭ 18942

from itertools import*

c = 0
for i in product('ДИОНСЙ', repeat=6):
    a = ''.join(i)
    if (a.count('Д') > 0 and a.count('Н') == 0) or (a.count('Н') > 0 and a.count('Д') == 0):
        if 'ДД' not in a and 'ИИ' not in a and 'ОО' not in a and 'НН' not in a and 'СС' not in a and 'ЙЙ' not in a:
            print(a)
            c += 1
print(c)
