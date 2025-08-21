#КЕГЭ 5954 шаблонный шаблон
#разбор Роди - https://www.youtube.com/watch?v=R5w8IroAWos

from functools import*

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)


for n in range(2030):
    f(n)

print((f(2023) - f(2022))//f(2020))
