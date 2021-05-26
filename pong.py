import turtle

def updateScoreboard():
    pen.clear()
    pen.write("P1: {}   P2: {}".format(pointsPlayer1, pointsPlayer2), align="center", font=("Courier", 24, "bold"))

def createPlayer() :
    player = turtle.Turtle()
    player.shape("square")
    player.shapesize(stretch_wid = 9, stretch_len = 1)
    player.speed(20)
    player.penup()
    return player

def player1Up() :
    y = p1.ycor()
    y += 20
    p1.sety(y)

def player1Down() :
    y = p1.ycor()
    y -= 20
    p1.sety(y)

def player2Up() :
    y = p2.ycor()
    y += 20
    p2.sety(y)

def player2Down() :
    y = p2.ycor()
    y -= 20
    p2.sety(y)

window = turtle.Screen()
window.title("PONG     ~iudizm")
window.bgcolor("grey")
window.setup(width=800, height=600)
window.tracer(0)

pointsPlayer1 = 0
pointsPlayer2 = 0

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.ht()
pen.goto(0, 260)
updateScoreboard()

p1 = createPlayer()
p1.color("white")
p1.goto(-350, 0)

p2 = createPlayer()
p2.color("black")
p2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.15

window.listen()
window.onkeypress(player1Up, "w")
window.onkeypress(player1Down, "s")
window.onkeypress(player2Up, "Up")
window.onkeypress(player2Down, "Down")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pointsPlayer2 += 1
        updateScoreboard()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pointsPlayer1 += 1
        updateScoreboard()

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < p2.ycor() + 50 and ball.ycor() > p2.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1

    if p1.ycor() > 250:
        yplayer1 = p1.ycor()
        p1.sety(yplayer1)
