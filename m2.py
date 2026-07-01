import turtle
import random

# Настройка черепахи и экрана
t = turtle.Turtle()
t.speed(0)                # максимальная скорость
t.hideturtle()            # скрываем указатель
turtle.colormode(255)     # RGB-режим для удобства
turtle.bgcolor("azure")   # светло-голубой фон

# --------------------- Жёлтая «крышка» (верхняя часть хлопушки) ---------------------
t.penup()
t.goto(0, -15)            # нижняя точка будущего круга (центр в (0,20), радиус 35)
t.pendown()
t.color("gold", "yellow")
t.begin_fill()
t.circle(35)              # круг станет видимой верхней частью
t.end_fill()

# --------------------- Красный конус ---------------------
t.penup()
t.goto(-35, 20)           # левый верх
t.pendown()
t.color("red", "red")
t.begin_fill()
t.goto(35, 20)            # правый верх
t.goto(0, -40)            # нижняя точка конуса
t.goto(-35, 20)
t.end_fill()

# обводка конуса для чёткости
t.penup()
t.goto(-35, 20)
t.pendown()
t.pensize(2)
t.color("darkred")
t.goto(35, 20)
t.goto(0, -40)
t.goto(-35, 20)

# --------------------- Палочка ---------------------
t.penup()
t.goto(0, -40)
t.setheading(-90)         # направление вниз
t.pendown()
t.pensize(8)
t.color("brown")
t.forward(100)

# --------------------- Конфетти и серпантин ---------------------
confetti_colors = ["#FF1493", "#00FFFF", "#FFD700", "#00FF00", "#FF4500", "#8A2BE2"]
t.pensize(3)

# Веер линий из самой верхней точки крышки (0, 55)
for angle in range(-70, 71, 15):
    t.penup()
    t.goto(0, 55)
    t.setheading(angle)
    t.pendown()
    t.color(random.choice(confetti_colors))
    length = random.randint(40, 90)
    t.forward(length)
    t.dot(6, random.choice(confetti_colors))   # шарик на конце

# Дополнительные линии из боковых точек крышки
offsets = [(-20, 50), (20, 50), (-10, 53), (10, 53)]
for offset in offsets:
    for _ in range(2):
        t.penup()
        t.goto(offset)
        t.setheading(random.randint(-80, 80))
        t.pendown()
        t.color(random.choice(confetti_colors))
        t.forward(random.randint(30, 70))
        t.dot(5, random.choice(confetti_colors))

# Ленты, свисающие из конуса
t.pensize(3)
t.penup()
t.goto(-15, -15)
t.pendown()
t.color("magenta")
t.setheading(-120)
t.circle(40, 90)          # левая лента

t.penup()
t.goto(15, -15)
t.pendown()
t.color("cyan")
t.setheading(-60)
t.circle(-40, 90)         # правая лента

# Ленты на конце палочки
t.penup()
t.goto(0, -140)
t.pendown()
t.color("orange")
t.setheading(-45)
t.circle(30, 90)

t.penup()
t.goto(0, -140)
t.pendown()
t.setheading(-135)
t.circle(-30, 90)

# --------------------- Завершение ---------------------
turtle.done()