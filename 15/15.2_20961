#КЕГЭ 20961 отрезки чистый шаблон

def f(x):
    p = 15 <= x <= 142
    q = 38 <= x <= 167
    a = a1 <= x <= a2
    return (not((q <= ((not a) and p)) <= (not q)))


r = []
d = [y for x in [15, 38, 142, 167] for y in [x, x + 0.1, x - 0.1]]
for a1 in d:
    for a2 in d:
        if a1 <= a2:
            if all(f(x) == 0 for x in d):
                r.append(a2 - a1)
print(round(min(r)))
