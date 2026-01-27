import pgzrun
import math 


TITLE = "Break Out Game !"
WIDTH,HEIGHT = 600,400

brick_list = []
score_name = "High_score: "
score = 0
game_end = "CONGRATULATION YOU SCORED"
game_over = False 
speed = False 
ball_dx = 3
ball_dy = -1
class Paddle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.x2 = 100
        self.y2 = 30
    def paddle_draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_rect(Rect((self.x,self.y),(self.x2,self.y2)),"green")
paddle = Paddle(250,300)
paddle_rect = Rect((paddle.x, paddle.y), (paddle.x2, paddle.y2))
class Brick:
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.x2 = 50
        self.y2 = 30
    def rect(self):
        return Rect((self.x,self.y),(self.x2,self.y2))
    def draw_brick(self):
        pos = (self.x,self.y)
        screen.draw.filled_rect(Rect((self.x,self.y),(self.x2,self.y2)),"brown")

class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = 10
    def draw_ball(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,("blue"))
ball = Ball(WIDTH/2,HEIGHT/2)
def create_bricks():
    for i in range(10):
        for j in range(4):
            brick = Brick(i,j)
            brick.x = 25 + i * 55
            brick.y = 10 + j * 40
            brick_list.append(brick)


def draw():
    if game_over:
        screen.blit("game_over2",(0,0))
        screen.draw.text(game_end,center =(300,280), color ="white")
        screen.draw.text(str(score), center = (300,300), color = "white")
        return
    screen.blit("field_background",(0,0))
    paddle.paddle_draw()
    ball.draw_ball()
    for brick in brick_list:
        brick.draw_brick()
    screen.draw.text(score_name,center = (50,10),color = "black")
    screen.draw.text(str(score),center = (110,10),color = "black")
    
def brick_collision():
    global score 
    for brick in brick_list[:]:
        if brick.rect.collidepoint(ball.x,ball.y):
            brick_list.remove(brick)
            score += 2

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def ball_position():
    global game_over,ball_dx,ball_dy
    ball.x += ball_dx
    ball.y += ball_dy 
    if ball.x <= 0 or ball.x > WIDTH:
        ball_dx *= -1
    if ball.y <= 0:
        ball_dy *= -1
    if ball.y > HEIGHT:
        game_over = True

create_bricks()
def update():
    global game_over
    global score 
    global ball_dx,ball_dy,speed
    if game_over:
        return 
    if keyboard.right:
        paddle.x += 5
    elif keyboard.left:
        paddle.x -= 5
    if paddle.x < 0 :
        paddle.x = 10
    elif paddle.x > 520 :
        paddle.x = 450
    for brick in brick_list:
        if distance(brick.x,brick.y,ball.x,ball.y) < 50:
            brick_list.remove(brick)
            ball_dy *=-1 
            ball_dx *= +1
            score += 2
    """if score == 6 and speed == False:
        ball_dy = -2
        speed = True"""
    if distance(paddle.x,paddle.y,ball.x,ball.y) < 50 and ball_dy > 0 :
        ball_dy = -ball_dy
        ball.y = paddle.y - ball.radius
    ball_position()
    if not brick_list:
        create_bricks()
    
   
     
pgzrun.go()
