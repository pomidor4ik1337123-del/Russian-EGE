№КЕГЭ 8658

res = []
for n in range(1, 1000000):
    oct_n = oct(n)[2:]
    if n % 7 == 0:
        oct_n = oct_n + '67'
    if n % 7 != 0:

        oct_n = oct_n + oct((n % 7) * 7)[2:]
    r = int(oct_n, 8)
    if r < 3000:
        res.append(r)
print(res, len(res))
