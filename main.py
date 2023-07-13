#|----------------------------------------------------------------------------------------------------------------------------------|
#| Luka Beg (c) 7-12-2023 (MM-DD-YYYY)                                                                                              |
#| Program napravljen za vrijeme Ljetne Škole Informatie u Zajednici Tehničke Kulture (ZTK) kao završni rad Python radionice.       |
#| Mentor: Josip Cindrić                                                                                                            |
#|----------------------------------------------------------------------------------------------------------------------------------|
from turtle import *

def ploca(): #Chessboard Creation
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

def polje(a, b): #Field
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
    point4 = (x + (a * 100) + 100, y + (b * 100))
    pu()
    goto(point1)
    begin_fill()
    pd()
    goto(point2)
    goto(point3)
    goto(point4)
    goto(point1)
    end_fill()

def pijun(a, b, bojaP): #Pawn
    pencolor(bojaP)
    fillcolor(bojaP)
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

def lovac(a, b, bojaL): #Bishop
    pencolor(bojaL)
    fillcolor(bojaL)
    pensize(2)
    speed(0)
    x = -500
    y = -500
    pu()
    goto(x + (a * 100) + 20, y + (b * 100) + 20)
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

def top(a, b, bojaT):
    pencolor(bojaT)
    fillcolor(bojaT)
    pensize(2)
    speed(0)
    x = -500
    y = -500
    pu()
    goto(x + (a * 100) + 20, y + (b * 100) + 20)
    pd()
    begin_fill()
    #Tijelo Topa / Rook's Body
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
    #Kruna Topa / Start of Rook's Crown
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
    #Kraj Krune Topa / End of Rook's Crown
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

def skakac(a,b,bojaS):
    pencolor(bojaS)
    fillcolor(bojaS)
    pensize(2)
    speed(0)
    x=-500
    y=-500
    pu()
    goto(x+(a*100)+20, y+(b*100)+20)
    pendown()
    begin_fill()
    #Tijelo Skakaca / Knight's body
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
    #Glava Skakaca / Start of Knight's head
    lt(70)
    fd(50)
    lt(90)
    fd(30)
    lt(110)
    fd(10)
    #Kraj Glave Skakaca / End of Knight's head
    rt(90)
    fd(20)
    goto(x+(a*100)+20, y+(b*100)+40)
    goto(x+(a*100)+20, y+(b*100)+20)
    lt(90)
    end_fill()

def kraljica(a,b,bojaK):
    pencolor(bojaK)
    fillcolor(bojaK)
    pensize(2)
    speed(0)
    x=-500
    y=-500
    pu()
    goto(x+(a*100)+20, y+(b*100)+20)
    pd()
    begin_fill()
    #Tijelo Kraljice / Queen's Body
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
    #Glava Kraljice / Queen's Head
    lt(90)
    fd(40)
    lt(90)
    fd(10)
    lt(90)
    fd(10)
    #Kraj Glave Kraljice / End of Queen's Head
    rt(90)
    fd(30)
    rt(90)
    fd(20)
    lt(90)
    fd(20)
    lt(90)
    end_fill()

def kralj(a,b,bojaKc):
    pencolor(bojaKc)
    fillcolor(bojaKc)
    pensize(2)
    speed(0)
    x=-500
    y=-500
    pu()
    goto(x+(a*100)+20, y+(b*100)+20)
    pd()
    begin_fill()
    #Tijelo Kralja / Body of King
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
    #Glava Kralja / Start of King's head
    lt(90)
    fd(15)
    lt(90)
    fd(10)
    rt(90)
    fd(10)
    rt(90)
    fd(10)
    lt(90)
    fd(15)
    lt(90)
    fd(10)
    lt(90)
    fd(10)
    #Kraj Glave Kralja / End of King's head
    rt(90)
    fd(30)
    rt(90)
    fd(20)
    lt(90)
    fd(20)
    lt(90)
    end_fill()

def start(boja1, boja2):
    ploca()
    for i in range(1,9):
        pijun(i,2,boja1)
        pijun(i,7,boja2)
    #TOP/Rook
    top(1,1,boja1)
    top(8,1,boja1)
    top(1,8,boja2)
    top(8,8,boja2)
    #LOVAC/Bishop
    lovac(3,1,boja1)
    lovac(6,1,boja1)
    lovac(3,8,boja2)
    lovac(6,8,boja2)
    #SKAKAC/Knight
    skakac(2,1,boja1)
    skakac(7,1,boja1)
    skakac(2,8,boja2)
    skakac(7,8,boja2)
    #KRALJICA/Queen
    kraljica(4,1,boja1)
    kraljica(4,8,boja2)
    #KRALJ/King
    kralj(5,1,boja1)
    kralj(5,8,boja2)
    #PIJUNI/Pawn
    polje(3,2)
    pijun(3,4,boja1)
    polje(4,7)
    pijun(4,5,boja2)
    polje(4,2)
    pijun(4,4,boja1)
    ht()
    exitonclick()

start("red", "blue")
