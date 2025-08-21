#КЕГЭ 506
#есть два типа - делители и fnmatch. есть немалая вероятность того, что на основной волне будет именно fnmatch
#перед вами функция prost, которая проверяет число на простоту - если оно простое - функция возвращает 1, если не простое - то 0. Можно вообще обойтись без этой функцией и испольщовать только функцию дя поиска делителей (d(n)). Простое число - число, которое имеет только два делителя, следовательно если длина списка, который возвращает функция d аоставляет 2, то число простое

def prost(n):
    if n <= 1:
        return 0
    for i in range(2, round(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1


def d(n):
    delit = {1}
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            delit.add(d)
            delit.add(n // d)
    return sorted(list(delit)[1:])


for n in range(25317, 51238):
    a = d(n)
    c = 0
    prost_delit = []
    for delit in a:
        if prost(delit):
            c += 1
            prost_delit.append(delit)
    if c >= 6:
        print(n, max(prost_delit))
