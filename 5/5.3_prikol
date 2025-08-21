№КЕГЭ 21243 больмень интересно

def f(n):
    s = ''
    while n:
        s += str(n % 5)
        n //= 5
    return s[::-1]


res = []
for n in range(1, 1000):
    n_5 = f(n)
    if sum(int(x) for x in n_5) % 5 == 0:
        n_5 = n_5.replace('0', '*')
        n_5 = n_5.replace('1', '0')
        n_5 = n_5.replace('*', '1')    #все один из способов замены 0 на 1 и 1 на 0
        n_5 = n_5 + '14'

    else:
        n_5 = n_5 + '33'
        n_5 = '44' + n_5[2:]
    r = int(n_5, 5)
    if r > 370:
        res.append([r, n])
print(min(res))
