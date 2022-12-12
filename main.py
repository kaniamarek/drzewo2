import turtle as t


def kw(a, c):
    t.fillcolor(c)
    t.begin_fill()
    for _ in range(4):
        t.fd(a)
        t.lt(90)
    t.end_fill()


def tree(a, c, i):
    if i == 0:

        kw(a, c)
        t.fd(a)
        t.rt(90)
        kw(a, c)
        t.fd(a)
        t.rt(45)
        return
    kw(a, c)
    t.lt(90)
    t.fd(a)
    t.rt(45)
    r, g, b = c
    tree(a/2**0.5, (r, g+0.1, b), i-1)
    t.fd(a)
    kw(a, c)
    t.lt(90)
    t.fd(a)
    t.rt(45)
    r -=0.1
    if r < 0:
        r = 0
        b += 0.1
    tree(a/2**0.5, (r, g+0.1, b), i-1)
    t.fd(a)
    t.lt(45)

t.speed(0)
t.penup()
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(50)
t.rt(180)
t.pendown()

kw(100, (1, 0.1, 0))
t.lt(90)
t.fd(100)
t.rt(45)
tree(100/2**0.5, (1, 0.1, 0), 8)
t.done()