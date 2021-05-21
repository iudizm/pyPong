import turtle

wn = turtle.Screen()
wn.title("PONG     ~iudizm")
wn.bgcolor("grey")
wn.setup(width=800, height=600)
wn.tracer(0)  # Nao atualiza a janela

# Placar
pts_a = 0
pts_b = 0

# Taco A
taco_a = turtle.Turtle()
taco_a.speed(0)
taco_a.shape("square")
taco_a.shapesize(stretch_wid=8, stretch_len=1)
taco_a.color("red")
taco_a.penup()
taco_a.goto(-350, 0)

# Taco B
taco_b = turtle.Turtle()
taco_b.speed(0)
taco_b.shape("square")
taco_b.shapesize(stretch_wid=8, stretch_len=1)
taco_b.color("blue")
taco_b.penup()
taco_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("black")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.25
bola.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.ht()
pen.goto(0, 260)
pen.write("P1: 0   P2: 0", align="center", font=("Courier", 24, "normal"))

# Funcoes tacos
def taco_a_cima():
    y = taco_a.ycor()
    y += 20
    taco_a.sety(y)

def taco_a_baixo():
    y = taco_a.ycor()
    y -= 20
    taco_a.sety(y)

def taco_b_cima():
    y = taco_b.ycor()
    y += 20
    taco_b.sety(y)

def taco_b_baixo():
    y = taco_b.ycor()
    y -= 20
    taco_b.sety(y)

# Teclas
wn.listen()
wn.onkeypress(taco_a_cima, "w")
wn.onkeypress(taco_a_baixo, "s")
wn.onkeypress(taco_b_cima, "Up")
wn.onkeypress(taco_b_baixo, "Down")

# Loop principal do jogo
while True:
    wn.update()  # Atualiza a janela(todo começo de loop)

    # Mexer a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Bordas seladas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        pts_b += 1
        pen.clear()
        pen.write("P1: {}   P2: {}".format(pts_a, pts_b),
        align="center", font=("Courier", 24, "normal"))

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pts_a += 1
        pen.clear()
        pen.write("P1: {}   P2: {}".format(pts_a, pts_b),
                align="center", font=("Courier", 24, "normal"))

    # Colisões
    # Colisao Taco B
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < taco_b.ycor() + 50 and bola.ycor() > taco_b.ycor()-50):
        bola.setx(340)
        bola.dx *= -1
    # Colisao Taco A
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < taco_a.ycor() + 50 and bola.ycor() > taco_a.ycor()-50):
        bola.setx(-340)
        bola.dx *= -1

    if taco_a.ycor() > 250:
        ytacoa = taco_a.ycor()
        taco_a.sety(ytacoa)
