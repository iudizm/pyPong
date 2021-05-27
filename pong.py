import turtle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_H = 140
PADDLE_W = 8

BG_COLOR = "#7c8477"
L_PADDLE_COLOR = "#d3e4d3"
R_PADDLE_COLOR = "#181d1a"
INITIAL_BALL_COLOR = "red"
WRITING_COLOR = "#c9e0ba"

PADDLE_LINE = (SCREEN_WIDTH / 2) - 60
VERTICAL_BOARD_LIMIT = (SCREEN_HEIGHT / 2) - 10
HORIZONTAL_BOARD_LIMIT = (SCREEN_WIDTH / 2) - 10

def updateScoreboard():
    scoreboard.clear()
    scoreboard.write("{}                         {}".format(pointsPlayer1, pointsPlayer2), align="center", font=("Courier", 30, "bold"))

def createPlayer() :
    player = turtle.Turtle()
    player.shape("square")
    player.shapesize(stretch_len = PADDLE_H / 20, stretch_wid= PADDLE_W / 20)
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
window = turtle.Screen()
window.title("PONG     ~iudizm")
window.bgcolor(BG_COLOR)
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)

# SCOREBOARD
pointsPlayer1 = 0
pointsPlayer2 = 0

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.pu()
scoreboard.ht()
scoreboard.pencolor(WRITING_COLOR)
scoreboard.goto(0, 245)
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

    # ball top bot
    if ball.ycor() > (VERTICAL_BOARD_LIMIT) :
        ball.sety(VERTICAL_BOARD_LIMIT)
        ball.dy *= -1

    if ball.ycor() < -VERTICAL_BOARD_LIMIT :
        ball.sety(-VERTICAL_BOARD_LIMIT)
        ball.dy *= -1

    # paddle up down
    if p1.ycor() + 70 >= VERTICAL_BOARD_LIMIT :
        p1.sety(VERTICAL_BOARD_LIMIT - 70)

    if p1.ycor() - 70 <= -VERTICAL_BOARD_LIMIT :
        p1.sety(-VERTICAL_BOARD_LIMIT + 70)

    # paddle 2 up down
    if p2.ycor() + 70 >= VERTICAL_BOARD_LIMIT :
        p2.sety(VERTICAL_BOARD_LIMIT - 70)

    if p2.ycor() - 70 <= -VERTICAL_BOARD_LIMIT :
        p2.sety(-VERTICAL_BOARD_LIMIT + 70)

    # ball left right (score)
    if ball.xcor() < -HORIZONTAL_BOARD_LIMIT :
        ball.goto(0, 0)
        ball.dx *= -1
        pointsPlayer2 += 1
        updateScoreboard()

    if ball.xcor() > HORIZONTAL_BOARD_LIMIT :
        ball.goto(0, 0)
        ball.dx *= -1
        pointsPlayer1 += 1
        updateScoreboard()

    # ball hitting paddles
    if ball.xcor() < -PADDLE_LINE :
        paddle1 = p1.ycor()
        if paddle1 + 70 >= ball.ycor() >= paddle1 - 70:
            ball.setx(-PADDLE_LINE)
            ball.color(L_PADDLE_COLOR)
            ball.dx *= -1

    if ball.xcor() > PADDLE_LINE :
        paddle2 = p2.ycor()
        if  paddle2 + 70 >= ball.ycor() >= paddle2 - 70 :
            ball.setx(PADDLE_LINE)
            ball.color(R_PADDLE_COLOR)
            ball.dx *= -1