import turtle

def updateScoreboard():
    pen.clear()
    pen.write("{}                          {}".format(pointsPlayer1, pointsPlayer2), align="center", font=("Courier", 30, "bold"))

def createPlayer() :
    player = turtle.Turtle()
    player.shape("square")
    player.shapesize(stretch_len = 7, stretch_wid=0.5)
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

# SCREEN CREATION
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = "#7c8477"
L_PADDLE_COLOR = "#d3e4d3"
R_PADDLE_COLOR = "#181d1a"
INITIAL_BALL_COLOR = "red"
WRITING_COLOR = "#c9e0ba"

window = turtle.Screen()
window.title("PONG     ~iudizm")
window.bgcolor(BG_COLOR)
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)

# PHISICAL LIMITS
horizontalBoardLimit = (SCREEN_WIDTH / 2) - 10
verticalBoardLimit = (SCREEN_HEIGHT / 2) - 10
playerRectanglePosition = (SCREEN_WIDTH / 2) -60

# DRAW SCOREBOARD
pointsPlayer1 = 0
pointsPlayer2 = 0

pen = turtle.Turtle()
pen.speed(0)
pen.pu()
pen.ht()
pen.pencolor(WRITING_COLOR)
pen.goto(0, 245)
updateScoreboard()

# PADDLES
p1 = createPlayer()
p1.color(L_PADDLE_COLOR)
p1.goto(-350, 0)

p2 = createPlayer()
p2.color(R_PADDLE_COLOR)
p2.goto(350, 0)

# BALL STUFF
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color(INITIAL_BALL_COLOR)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.29
ball.dy = 0.15

# INPUT HANDLING
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

    if ball.xcor() < -playerRectanglePosition :
        paddle1 = p1.ycor()
        if paddle1 + 70 >= ball.ycor() >= paddle1 - 70:
            ball.setx(-playerRectanglePosition)
            ball.color(L_PADDLE_COLOR)
            ball.dx *= -1

    if ball.xcor() > playerRectanglePosition :
        paddle2 = p2.ycor()
        if  paddle2 + 70 >= ball.ycor() >= paddle2 - 70 :
            ball.setx(playerRectanglePosition)
            ball.color(R_PADDLE_COLOR)
            ball.dx *= -1