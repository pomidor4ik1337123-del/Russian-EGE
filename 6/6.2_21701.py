#КЕГЭ 21701

from turtle import*

k = 20
tracer(0)

for i in range(2):
    forward(28*k)
    right(90)
    forward(18*k)
    right(90)
penup()
forward(14*k)
right(90)
forward(10*k)
left(90)
pendown()
for i in range(2):
    forward(30*k)
    right(90)
    forward(7*k)
    right(90)
up()
for x in range(-50*k, 50*k, k):
    for y in range(-50 * k, 50 * k, k):
        goto(x, y)
        dot(3, 'purple')
done()
