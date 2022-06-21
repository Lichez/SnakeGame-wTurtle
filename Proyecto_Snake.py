import turtle
import time
import random

# Declaración de la pantalla

screen = turtle.Screen()
screen.setup(650, 650)
screen.bgcolor('black')
screen.title('Project Snake')

border = turtle.Turtle()
border.hideturtle()
border.speed(10)
border.color('white')
border.penup()
border.goto(325, 325)
border.pensize(3)
border.pendown()

for i in range(4):
    border.right(90)
    border.forward(650)

border.right(90)
border.forward(50)
border.right(90)
border.forward(650)



# Declaración de la serpiente

snake = turtle.Turtle()
snake.speed(10)
snake.shape('square')
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'
snake.color('green')

# Declarción de la comida

food = turtle.Turtle()
food.hideturtle()
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)
food.showturtle()
food.speed(0)

# Declaracion cuerpo

body = []

# Marcador

score = 0
max_score = 0

text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0, 285)
text.write("Puntuación: 0\tPuntuación más alta: 0", align="center", font=("verdana", 20, "normal"))

# Movimiento de la serpiente

delay = 0.1


def up():
    snake.direction = 'up'


def down():
    snake.direction = 'down'


def right():
    snake.direction = 'right'


def left():
    snake.direction = 'left'


def movement():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)

    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)


screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# Actualización de la pantalla

while True:
    screen.update()

    # Colision pantalla

    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 258 or snake.ycor() < -300:
        time.sleep(2)
        for i in body:
            i.clear()
            i.hideturtle()
        snake.hideturtle()
        snake.home()
        snake.showturtle()
        snake.direction = 'stop'
        body.clear()
        food.hideturtle()
        food.goto(0, 100)
        food.showturtle()

        score = 0
        text.clear()
        text.write("Puntuación: {}\tPuntuación más alta: {}".format(score, max_score), align="center", font=("verdana", 20, "normal"))

    if snake.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        new_body = turtle.Turtle()
        new_body.shape('square')
        new_body.color('green')
        new_body.penup()
        new_body.goto(0, 0)
        new_body.speed(0)
        body.append(new_body)

        score += 10
        if score > max_score:
            max_score = score
            text.clear()
            text.write("Puntuación: {}\tPuntuación más alta: {}".format(score, max_score), align="center", font=("verdana", 20, "normal"))
        else:
            text.clear()
            text.write("Puntuación: {}\tPuntuación más alta: {}".format(score, max_score), align="center", font=("verdana", 20, "normal"))

    total = len(body)

    for i in range(total - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    if total > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    movement()

    # Colision con cuerpo

    for i in body:
        if i.distance(snake) < 20:
            time.sleep(2)
            for i in body:
                i.clear()
                i.hideturtle()
            snake.hideturtle()
            snake.home()
            snake.showturtle()
            body.clear()
            snake.direction = 'stop'
            food.hideturtle()
            food.goto(0, 100)
            food.showturtle()

            score = 0
            text.clear()
            text.write("Puntuación: {}\tPuntuación más alta: {}".format(score, max_score), align="center", font=("verdana", 20, "normal"))

    time.sleep(delay)


turtle.done()
