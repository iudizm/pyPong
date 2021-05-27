import turtle, math

def updateScoreboard():
    pen.clear()
    pen.write("P1: {}   P2: {}".format(pointsPlayer1, pointsPlayer2), align="center", font=("Courier", 24, "bold"))

def createPlayer() :
    player = turtle.Turtle()
    player.shape("square")
    player.shapesize(stretch_len = 7)
    player.speed(20)
    player.penup()
    player.left(90)
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


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
window = turtle.Screen()
window.title("PONG     ~iudizm")
window.bgcolor("#7c8477")
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)

horizontalBoardLimit = (SCREEN_WIDTH / 2) - 10
verticalBoardLimit = (SCREEN_HEIGHT / 2) - 10
playerRectanglePosition = (SCREEN_WIDTH / 2) -60

pointsPlayer1 = 0
pointsPlayer2 = 0

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.ht()
pen.goto(0, 260)
updateScoreboard()

p1 = createPlayer()
p1.color("#d3e4d3")
p1.goto(-350, 0)

p2 = createPlayer()
p2.color("#181d1a")
p2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.29
ball.dy = 0.15

window.onkeypress(player1Up, "w")
window.onkeypress(player1Down, "s")
window.onkeypress(player2Up, "Up")
window.onkeypress(player2Down, "Down")
window.listen()

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > (verticalBoardLimit) :
        ball.sety(verticalBoardLimit)
        ball.dy *= -1

    if ball.ycor() < -verticalBoardLimit :
        ball.sety(-verticalBoardLimit)
        ball.dy *= -1

    if ball.xcor() < -horizontalBoardLimit :
        ball.goto(0, 0)
        ball.dx *= -1
        pointsPlayer2 += 1
        updateScoreboard()

    if ball.xcor() > horizontalBoardLimit :
        ball.goto(0, 0)
        ball.dx *= -1
        pointsPlayer1 += 1
        updateScoreboard()

    if ball.xcor() <= -playerRectanglePosition :
        paddle1 = p1.ycor()
        if paddle1 + 70 >= ball.ycor() >= paddle1 - 70:
            ball.setx(-playerRectanglePosition)
            ball.color("#d3e4d3")
            ball.dx *= -1

    if ball.xcor() >= playerRectanglePosition :
        paddle2 = p2.ycor()
        if  paddle2 + 70 >= ball.ycor() >= paddle2 - 70 :
            ball.setx(playerRectanglePosition)
            ball.color('#181d1a')
            ball.dx *= -1