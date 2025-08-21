#КЕГЭ 8681

def tetie(n):
    if 1000 <= abs(n) <= 9999:
        return 1
    return 0

r = []
a = [int(x) for x in open('17_8681.txt')]
for i in range(len(a)-1):
    if (tetie(a[i]) or tetie(a[i+1])) and (a[i] * a[i+1]) % 1007 == 0:    #1007 - это минимальный четырехзначный элемент, оканчивающийся на 7, можно его найти программой, либо открыв эксель и отсортировав числа вручную 
        r.append(a[i] * a[i+1])
print(len(r), max(r))


#вот как написать поиск мин четырехзнач числа, оканчивающегося на 7
# b = []
# for i in range(len(a)-1):
#     if abs(i) % 10 == 7 and tetie(i):
#         b.append(i)
# print(min(b))
