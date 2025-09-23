import turtle
import time

#Functions 
def up():
   x= pen.xcor()
   y= pen.ycor()+24
   if valid_move(x,y):
        pen.goto(x,y)
def down():
    x= pen.xcor()
    y= pen.ycor()-24
    if valid_move(x,y):
        pen.goto(x,y)
def right():
    x= pen.xcor()+24
    y= pen.ycor()
    if valid_move(x,y):
        pen.goto(x,y)
def left():
    x= pen.xcor()-24
    y= pen.ycor()
    if valid_move(x,y):
        pen.goto(x,y)
def valid_move(x,y):
    for tiles in obstacle:
        if x == tiles.xcor() and  y == tiles.ycor():
            return False
    return True   


  
#pen and screen
screen=turtle.Screen()
screen.bgcolor("black")
pen=turtle.Turtle()
pen.color("red")
pen.up()
pen.shape("turtle")
turtle.colormode(255)

#the Maze 
finish=turtle.Turtle()
finish.color("Green")
finish.shape("circle")
finish.up()
maze=["XXXXXXXXXXXX",
      "X   X      X",
      "X   X   X  X",
      "X XXX  X   X",
      "X      X   X",
      "XXX   XXXXXX",
      "X  XX      X",
      "X   XXXX   X",
      "X          X",
      "X  XXXXXXXXX",
      "X          X",
      "XXXXXXXXXXFX "]
obstacle=[]
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x]== 'X':
            tiles = turtle.Turtle()
            tiles.shape("square")
            tiles.speed(100)
            tiles.penup()
            tiles.color("white")
            tile_y= 288-(y*24)
            tile_x=-288 +(x*24)
            tiles.goto(tile_x,tile_y)
            obstacle.append(tiles)
        elif maze[y][x]== "F":
            f_x= -288+(x*24)
            f_y= 288-(y*24)
            finish.goto(f_x,f_y)

clock= turtle.Turtle()
clock.goto(150,150) 
clock.color("white")     
pen.goto(-264,264)
screen.listen()
screen.onkey(right,"d")
screen.onkey(down,"s")
screen.onkey(up,"w")
screen.onkey(left,"a")
timer=30

while True:
    clock.write(timer)
    time.sleep(1)
    clock.clear()
    timer= timer-1
    if timer == 0:
        pen.write("GAME OVER",font=("arial",20))

        screen.onkey(None,"d")
        screen.onkey(None,"a")
        screen.onkey(None,"w")
        screen.onkey(None,"s")
        break

    if pen.distance(finish)< 10:
        pen.write("YOU WON",font=("arial",20))

        screen.onkey(None,"d")
        screen.onkey(None,"a")
        screen.onkey(None,"w")
        screen.onkey(None,"s")
        break


turtle.exitonclick()
 
