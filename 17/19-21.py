#КЕГЭ 22 полный шаблон, халявные три балла, настоятедльбно рекоменду посмотреть разбор Роди
#для наглядности тут код для сложного номера, который на егэ совсем совсмем вряд ли попадется 

def f(a, b, m):
    if a >= 40 or b >= 40:
        return m % 2 == 0
    if m == 0:
        return 0
    h = []
    if a != b:
        h += [f(max(a, b) + 1, min(a, b), m - 1), f(max(a, b) + 2, min(a, b), m - 1), f(max(a, b) + 3, min(a, b), m - 1), f(max(a, b), min(a, b) * 2, m - 1)]
    if a == b:
        h += [f(max(a, b) + 1, min(a, b), m - 1), f(max(a, b) + 2, min(a, b), m - 1), f(max(a, b) + 3, min(a, b), m - 1), f(max(a, b), min(a, b) + 1, m - 1), f(max(a, b), min(a, b) + 2, m - 1), f(max(a, b), min(a, b) + 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)


print([a + b for a in range(1, 100) for b in range(1, 100) if f(a, b, 1)])
print([b for b in range(1, 40) if not f(11, b, 1) and f(11, b, 3)])
print([b for b in range(1, 40) if not f(31, b, 2) and f(31, b, 4)])

