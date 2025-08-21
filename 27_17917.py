#КЕГЭ 17917
#не стоит бояться 27 номера - он супер простой и понятный, буквально неделя чилловой прорешки и он будет отлетать токо так епта
#есть два основных метода решения - условно старый и хайповый с помощью DBscan. Основная волна решщалась спокойно с помощью "старого" метода, учить ли дбскан или нет для запаса - решайте сами. СЕйчас перед вами будент как раз простой старый метод
#РАЗБОР РОДИ К ПРОСМОТРУ ОБЯЗАТЕЛЕН!!!!
from math import*

a = [[], [], [], []]
b =[[], [], [], [], []]

for i in open('27_A_17917.txt'):
    x, y = [float(k) for k in i.split()]
    if y < 4:
        a[0].append([x, y])
    elif x > 15:
        a[1].append([x, y])
    elif (10 < y < 14) and x < 10:
        a[2].append([x, y])
    elif y > 14:
        a[3].append([x, y])


for i in open('27_B_17917.txt'):
    x, y = [float(k) for k in i.split()]
    if y < 4 and x < 10:
        b[0].append([x, y])
    elif y > 10:
        b[1].append([x, y])
    elif x > 20 and y > 5:
        b[2].append([x, y])
    elif y < 5 and 24 < x < 28:
        b[3].append([x, y])
    elif x > 29:
        b[4].append([x, y])


def center(cluster):
    m = []
    for p in cluster:
        summa = sum(dist(p, p1) for p1 in cluster)
        m.append([summa, p])
    return min(m)[1]


center_a = [center(cluster) for cluster in a]
center_b = [center(cluster) for cluster in b]

pxa = int(sum(x for x, y in center_a) / 4 * 10_000)
pya = int(sum(y for x, y in center_a) / 4 * 10_000)
pxb = int(sum(x for x, y in center_b) / 5 * 10_000)
pyb = int(sum(y for x, y in center_b) / 5 * 10_000)

print(pxa, pya)
print(pxb, pyb)
