#|----------------------------------------------------------------------------------------------------------------------------------|
#| Luka Beg (c) 7-12-2023 (MM-DD-YYYY)                                                                                              |
#| Program napravljen za vrijeme Ljetne Škole Informatie u Zajednici Tehničke Kulture (ZTK) kao završni rad Python radionice.       |
#| Mentor: Josip Cindrić                                                                                                            |
#|----------------------------------------------------------------------------------------------------------------------------------|
from turtle import *

def ploca():
    x = -400
    ispuna = True
    pencolor("green")
    fillcolor("green")
    pensize(1)
    speed(0)
    for i in range(1, 9):
        y = -400
        for j in range(1, 9):
            point1 = (x, y)
            point2 = (x, y + 100)
            point3 = (x + 100, y + 100)
            point4 = (x + 100, y)
            pu()
            goto(point1)
            if ispuna:
                begin_fill()
            pd()
            goto(point2)
            goto(point3)
            goto(point4)
            if ispuna:
                end_fill()
            ispuna = not ispuna
            y = y + 100
        x = x + 100
        ispuna = not ispuna
    return

def polje(a, b):
    x = -500
    y = -500
    if (not (((a % 2) == 0) ^ ((b % 2) == 0))):
        pencolor("green")
        fillcolor("green")
        pensize(1)
        speed(0)
    else:
        pencolor("green")
        fillcolor("white")
        pensize(1)
        speed(0)
    point1 = (x + (a * 100), y + (b * 100))
    point2 = (x + (a * 100), y + (b * 100) + 100)
    point3 = (x + (a * 100) + 100, y + (b * 100) + 100)
    point4 = (x + (a * 100) + 100, y(b * 100))
    pu()
    goto(point1)
    begin_fill()
    pd()
    goto(point2)
    goto(point3)
    goto(point4)
    goto(point1)
    end_fill()

def pijun(a, b, boja):
    pencolor(boja)
    fillcolor(boja)
    pensize(2)
    speed(0)
    x = -500
    y = -500
    pu()
    goto(x + (a * 100) + 30, y + (b * 100) + 20)
    pd()
    begin_fill()
    goto(x + (a * 100) + 70, y + (b * 100) + 20)
    goto(x + (a * 100) + 50, y + (b * 100) + 50)
    goto(x + (a * 100) + 30, y + (b * 100) + 20)
    pu()
    goto(x + (a * 100) + 50, y + (b * 100) + 40)
    pd()
    circle(10)
    end_fill()

def lovac(a, b, boja):
    pencolor(boja)
    fillcolor(boja)
    pensize(2)
    speed(0)
    x = -500
    y = -500
    pu()
    goto(x + (a * 100) + 80, y + (b * 100) + 20)
    pd()
    begin_fill()
    goto(x + (a * 100) + 80, y + (b * 100) + 20)
    goto(x + (a * 100) + 50, y + (b * 100) + 60)
    goto(x + (a * 100) + 20, y + (b * 100) + 20)
    pu()
    goto(x + (a * 100) + 50, y + (b * 100) + 60)
    pd()
    circle(10)
    end_fill()

def top(a, b, boja):
    pencolor(boja)
    fillcolor(boja)
    pensize(2)
    speed(0)
    x = -500
    y = -500
    pu()
    goto(x + (a * 100) + 20, y + (b * 100) + 20)
    pd()
    begin_fill()
    #Tijelo Topa
    fd(60)
    lt(90)
    fd(20)
    lt(90)
    fd(10)
    rt(90)
    fd(20)
    rt(90)
    fd(10)
    lt(90)
    fd(20)
    #Kruna Topa
    lt(90)
    fd(10)
    lt(90)
    fd(10)
    rt(90)
    fd(10)
    rt(90)
    fd(10)
    lt(90)
    fd(20)
    lt(90)
    fd(10)
    rt(90)
    fd(10)
    rt(90)
    fd(10)
    lt(90)
    fd(10)
    #Kraj Krune Topa
    lt(90)
    fd(20)
    lt(90)
    fd(10)
    rt(90)
    fd(20)
    rt(90)
    fd(10)
    lt(90)
    fd(20)
    lt(90)
    end_fill()

def skakac(a,b,boja):
    pencolor(boja)
    fillcolor(boja)
    pensize(2)
    speed(0)
    x=-500
    y=-500
    pu()
    goto(x+(a*100)+20, y+(b*100)+20)
    pendown()
    begin_fill()
    #Tijelo Skakaca/Konja
    fd(60)
    lt(90)
    fd(20)
    lt(90)
    fd(10)
    rt(90)
    fd(10)
    lt(90)
    fd(10)
    rt(90)
    fd(20)
    rt(90)
    fd(10)
    lt(90)
    fd(10)
    #Glava Skakaca/Konja
    lt(70)
    fd(50)
    lt(90)
    fd(30)
    lt(110)
    fd(10)
    #Kraj Glave Skakaca/Konja
    rt(90)
    fd(20)
    goto(x+(a*100)+20, y+(b*100)+40)
    goto(x+(a*100)+20, y+(b*100)+20)
    lt(90)
    end_fill()

def kraljica(a,b,boja):
    pencolor(boja)
    fillcolor(boja)
    pensize(2)
    speed(0)
    x=-500
    y=-500
    pu()
    goto(x+(a*100)+20, y+(b*100)+20)
    pd()
    begin_fill()
    #Tijelo Kraljice
    fd(60)
    lt(90)
    fd(20)
    lt(90)
    fd(20)
    rt(90)
    fd(30)
    rt(90)
    fd(10)
    lt(90)
    fd(10)
    #Glava Kraljice
    lt(90)
    fd(40)
    lt(90)
    fd(10)
    lt(90)
    fd(10)
    #Kraj Glave Kraljice
    rt(90)
    fd(30)
    rt(90)
    fd(20)
    lt(90)
    fd(20)
    lt(90)
    end_fill()

def kralj(a,b,boja):
    pencolor(boja)
    fillcolor(boja)
    pensize(2)
    speed(0)
    x=-500
    y=-500
    pu()
    goto(x+(a*100)+20, y+(b*100)+20)
    pd()
    begin_fill()
    #Tijelo Kralja
    fd(60)
    lt(90)
    fd(20)
    lt(90)
    fd(20)
    rt(90)
    fd(30)
    rt(90)
    fd(10)
    lt(90)
    fd(10)
    #Glava Kralja
