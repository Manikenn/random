import turtle

# Создаем экран для рисования
screen = turtle.Screen()
screen.bgcolor("#ffeeff")

# Создаем черепашку для рисования
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Рисуем круги разных цветов
colors = ["#ff0000", "#ff9900", "#ffff00", "#00ff00", "#00ffff", "#0000ff", "#9900ff"]
for i in range(7):
    pen.color(colors[i])
    pen.circle(50 + i * 10)

# Рисуем звезды
pen.color("#ffffff")
pen.penup()
pen.goto(-150, 0)
pen.pendown()
for i in range(5):
    pen.forward(300)
    pen.right(144)

# Заканчиваем рисование
turtle.done()