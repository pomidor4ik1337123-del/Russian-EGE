#КЕГЭ 17680 

b = []
a = [int(x) for x in open('17_17680.txt')]
for i in a:
    if i > 0:
        if abs(i) % 41 == 0:
            b.append(i)

res = []
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        if abs(a[i] - a[i+1]) % min(b)  == 0:
            res.append(a[i] + a[i+1])
print(len(res), max(res))
