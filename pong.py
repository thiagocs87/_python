# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddleL_pos = HEIGHT / 2
paddleR_pos = HEIGHT / 2
velocity = [0, 0]
move_p1 = 0
move_p2 = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
direction = "RIGHT"
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos
    global velocity
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    velocity[0] = random.randrange(5,10)
    velocity[1] = random.randrange(3, 10)
    if direction == "LEFT":
        velocity[0] *= -1
        velocity[1] *= -1
        
# define event handlers
def new_game():
    global paddleR_pos, paddleL_pos, paddleR_vel, paddleL_vel
    global score1, score2
    global direction
    paddleR_pos = HEIGHT / 2
    paddleL_pos = HEIGHT / 2
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddleR_pos, paddleL_pos, ball_pos, ball_vel, move_p1, move_p2
    global direction    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += velocity[0]
    ball_pos[1] += velocity[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddleL_pos = paddleL_pos + move_p1
    paddleR_pos = paddleR_pos + move_p2  
    
    if paddleL_pos == HALF_PAD_HEIGHT or  paddleL_pos == HEIGHT - HALF_PAD_HEIGHT:
        move_p1 = 0

    if paddleR_pos == HALF_PAD_HEIGHT or  paddleR_pos == HEIGHT - HALF_PAD_HEIGHT:
        move_p2 = 0   
    
    # draw paddles
    canvas.draw_polygon([(0,paddleL_pos-HALF_PAD_HEIGHT),(PAD_WIDTH,paddleL_pos-HALF_PAD_HEIGHT),(PAD_WIDTH,paddleL_pos+HALF_PAD_HEIGHT),(0,paddleL_pos+HALF_PAD_HEIGHT)], 5, "White", "Green")
    canvas.draw_polygon([(WIDTH,paddleR_pos-HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH,paddleR_pos-HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH,paddleR_pos+HALF_PAD_HEIGHT),(WIDTH,paddleR_pos+HALF_PAD_HEIGHT)], 5, "White", "Green")    
    
    # determine whether paddle and ball collide    
    if velocity[0] > 0:
        if int(ball_pos[0]) >= int(WIDTH)- BALL_RADIUS:
            if ball_pos[1]>=paddleR_pos - HALF_PAD_HEIGHT and ball_pos[1]<=paddleR_pos + HALF_PAD_HEIGHT:
                velocity[0] = -velocity[0] - (velocity[0] * 0.1) 
                velocity[1] = velocity[1] + (velocity[0] * 0.1) 
            else:
                score1 += 1
                direction = "RIGHT"
                new_game()                 
    
    if velocity[0] < 0:
        if int(ball_pos[0] - BALL_RADIUS) <= 0:
            if ball_pos[1]>=paddleL_pos - HALF_PAD_HEIGHT and ball_pos[1]<=paddleL_pos + HALF_PAD_HEIGHT:
                velocity[0] = -velocity[0] - (velocity[0] * 0.1) 
                velocity[1] = velocity[1] + (velocity[0] * 0.1) 
            else:
                direction = "LEFT"
                score2 += 1
                new_game()
    
    if velocity[1] > 0:
        if int(ball_pos[1]) >= int(HEIGHT)- BALL_RADIUS:
            velocity[0] = velocity[0]
            velocity[1] = -velocity[1]
            
    if velocity[1] < 0:
        if int(ball_pos[1] - BALL_RADIUS) <= 0:
            velocity[0] = velocity[0]
            velocity[1] = -velocity[1]            

    # draw scores
    canvas.draw_text('Player 1: ' + str(score1), (20, 20), 20, 'Red')
    canvas.draw_text('Player 2: ' + str(score2), (500, 20), 20, 'Red')
        
def keydown(key):
    global move_p1
    global move_p2
    
    if key == simplegui.KEY_MAP["up"]:
        move_p1 = -5
    if key == simplegui.KEY_MAP["down"]:
        move_p1 = 5

    if key == simplegui.KEY_MAP["w"]:
        move_p2 = -5
    if key == simplegui.KEY_MAP["s"]:
        move_p2 = 5  
        
def keyup(key):
    global move_p1
    global move_p2
    
    if key == simplegui.KEY_MAP["up"]:
        move_p1 = 0
    if key == simplegui.KEY_MAP["down"]:
        move_p1 = 0

    if key == simplegui.KEY_MAP["s"]:
        move_p2 = 0
    if key == simplegui.KEY_MAP["w"]:
        move_p2 = 0   

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()