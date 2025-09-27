import turtle
import random
import time
screen=turtle.Screen()
screen.bgcolor("white")
pen= turtle.Turtle()
pen.shape("triangle")
#score
score=0
scores= turtle.Turtle()
scores.color("black")
scores.shape("square")
scores .up()
scores.goto(-190,190)
scores.hideturtle()
scores.write("scores :")



   
def create_balloons():
    balloons=turtle.Turtle()
    balloons.shape("circle")
    balloons.up()
    balloons.color("red")
    x=random.randint(-200,200)
    y= random.randint(150,200)
    balloons.speed(100)
    balloons.goto(x,y)
    return balloons
    '''speed=1
    balloon.speed(speed)
    minus_y=-200
    balloons.goto(x,minus_y)
    balloons.hideturtle()
    '''

      
    
    
   
def move_left():
    x_position= pen.xcor()-25
    pen.goto(x_position,y)
def move_right():
    x_position= pen.xcor()+25
    pen.goto(x_position,y)


#needle
pen.penup()
pen.speed(100)
x= 0
y = -160
pen.goto(x,y)
pen.left(90)
screen.listen()
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")


balloon=create_balloons()
ball_y=-200
#balloon
while True:
    
    balloon.sety(balloon.ycor()-5)
    if balloon.distance(pen) < 20:
        score +=1
        scores.clear()
        scores.write(score,font=("arial",25))
    
        balloon.hideturtle()
        balloon=create_balloons()
    if balloon.ycor() <= ball_y:
        balloon.hideturtle()
        balloon=create_balloons()

turtle.exitonclick()

    