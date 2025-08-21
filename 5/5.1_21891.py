#КЕГЭ 21891

for n in range(1, 1000):
    n_bin = bin(n)[2:]
    a = n_bin + str(n_bin.count('1') % 2)
    b = a + str(a.count('1') % 2)
    r = int(b, 2)
    if r > 253:
        print(n, r)
