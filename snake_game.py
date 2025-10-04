import turtle 
import random 
turtle.colormode(255)


screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(600,600)


#snake
snake=turtle.Turtle()
snake.color("green")
snake.shape("circle")
snake.up()
snake.speed(0)

segments = []

#snake food
food=turtle.Turtle()
food.shape("circle")
food.color("red")
food.speed(0)
food.up()
x=random.randint(-180,180)
y=random.randint(-180,180) 
food.goto(x,y)


direction= "right"
#snake direction
def right():
    global direction
    direction="right"
def left():
    global direction
    direction= "left"
def up():
    global direction
    direction= "up"
def down():
    global direction
    direction = "down"
def move():
    if direction == "right":
        snake.setx(snake.xcor()+5) 
    if direction ==  "left":
        snake.setx(snake.xcor()-5)
    if direction == "down":
        snake.sety(snake.ycor()-5)
    if direction == "up":
        snake.sety(snake.ycor()+5)
def square(size):
    for i in range(4):
        write.forward(size)
        write.right(90)
    
   
   
#Writer
write= turtle.Turtle()
write.up()

write.color(132,76,59)
write.goto(-300,300)
write.begin_fill()
square(600)
write.end_fill()

write.color(194, 178, 128)
write.goto(-270,270)
write.begin_fill()
square(540)
write.end_fill()





#keyboard keys
screen.listen()
screen.onkey(right,"d")
screen.onkey(left,"a")
screen.onkey(up,"w")
screen.onkey(down,"s")



#collision
while True:
    move()
    if snake.distance(food) < 20:
        x=random.randint(-180,180)
        y=random.randint(-180,180) 
        food.goto(x,y)

        new_segment= turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.up()
        new_segment.hideturtle()
        segments.append(new_segment)
        
        
   

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

 
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    if snake.ycor() >= 300 or snake.ycor() <= -300 or snake.xcor() >= 300 or snake.xcor() <= -300:
        screen.onkey(None,"d")
        screen.onkey(None,"a")
        screen.onkey(None,"w")
        screen.onkey(None,"s")
        write.goto(-200,0)
        write.write("GAME OVER ",font=("arial",50)) 

        break

    
turtle.exitonclick()

