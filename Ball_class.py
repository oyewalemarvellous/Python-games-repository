import pgzrun

WIDTH,HEIGHT= 600,300
class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0 
        self.radius = 36
    
    def draw_ball(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos,self.radius,"blue")

ball = Ball(50,150)
def draw():
    screen.clear()
    ball.draw_ball()
speed = -5

def on_key_down(key):
    if key == keys.SPACE:
        ball.y  -= 25
    
    

def update():
    global speed
    #Bouncing ball
    """ball.y = ball.y + speed
    if ball.y == 10:
        speed = 5
    elif ball.y == 550:
        speed = -5"""
    if  ball.y <= 280:
        ball.y += 1


pgzrun.go()