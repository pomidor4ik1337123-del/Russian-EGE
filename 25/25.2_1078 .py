#КЕГЭ 1078

def d(n):
    delit = {1, n}
    for d in range(1, round(n ** 0.5) + 1):
        if n % d == 0:
            delit.add(d)
            delit.add(n // d)
    return sorted(delit)[1:-1]


for n in range(1204300, 1204380):
    deli = d(n)
    if len(deli) > 1:
        s = sum(int(x) for x in deli if x % 2 == 0)
    else:
        s = 0
    if s != 0 and s % 10 == 0:
        print(n, s)
