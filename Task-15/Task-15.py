import turtle

screen=turtle.Screen()
screen.bgcolor("white")
screen.title("Pong game")
screen.setup(1000,500)

left_score=0
right_score=0
score=turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0,220)
score.write("Left_player_score : {}    Right_player_score : {}".format(left_score,right_score),align="center",font=("Courier",10))

left_player=turtle.Turtle()
left_player.speed(0)
left_player.shape("square")
left_player.color("black")
left_player.shapesize(5,1)
left_player.penup()
left_player.goto(-400,0)

right_player=turtle.Turtle()
right_player.speed(0)
right_player.shape("square")
right_player.color("black")
right_player.shapesize(5,1)
right_player.penup()
right_player.goto(400,0)

ball = turtle.Turtle()
ball.speed(50)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

def left_up():
    up=left_player.ycor()
    up+=25
    left_player.sety(up)
def left_down():
    down=left_player.ycor()
    down-=25
    left_player.sety(down)
def right_up():
    up=right_player.ycor()
    up+=25
    right_player.sety(up)
def right_down():
    down=right_player.ycor()
    down-=25
    right_player.sety(down)

screen.listen()
screen.onkeypress(left_up,"w")
screen.onkeypress(left_down,"s")
screen.onkeypress(right_up,"Up")
screen.onkeypress(right_down,"Down")

while True:
    screen.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>200:
        ball.sety(200)
        ball.dy*=-1
    if ball.ycor()<-200:
        ball.sety(-200)
        ball.dy*=-1

    if ball.xcor()>500:
        ball.goto(0,0)
        ball.dy*=-1
        left_score+=1
        score.clear()
        score.write("Left_player_score : {}    Right_player_score : {}".format(left_score,right_score),align="center",font=("Courier",10))
    if ball.xcor()<-500:
        ball.goto(0,0)
        ball.dy*=-1
        right_score+=1
        score.clear()
        score.write("Left_player_score : {}    Right_player_score : {}".format(left_score,right_score),align="center",font=("Courier",10))

    if (ball.xcor()>360 and ball.xcor()<370) and (ball.ycor()<right_player.ycor()+45 and ball.ycor()>right_player.ycor()-45):
        ball.setx(360)
        ball.dx*=-1

    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<left_player.ycor()+45 and ball.ycor()>left_player.ycor()-45):
        ball.setx(-360)
        ball.dx*=-1


turtle.done()
