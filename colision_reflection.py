import simplegui

# initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
velocity = [0, 0]

ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers

def keydown(key):
    acc = 1
    print velocity[0]
    print velocity[1]
    
    if velocity[0] == 0 and velocity[1] == 0:
        if key == simplegui.KEY_MAP["left"]:
                velocity[0] = velocity[0] - acc
        if key == simplegui.KEY_MAP["right"]:
                velocity[0] = velocity[0] + acc
        if key == simplegui.KEY_MAP["up"]:
                velocity[1] = velocity[1] - acc
        if key == simplegui.KEY_MAP["down"]:
                velocity[1] = velocity[1] + acc                
    else:
        if key == simplegui.KEY_MAP["left"]:
            velocity[0] = velocity[0] - acc
        if key == simplegui.KEY_MAP["right"]:
            velocity[0] = velocity[0] + acc
        if key == simplegui.KEY_MAP["up"]:
            velocity[1] = velocity[1] - acc
        if key == simplegui.KEY_MAP["down"]:
            velocity[1] = velocity[1] + acc
        
def draw(canvas):

    ball_pos[0] += velocity[0]
    ball_pos[1] += velocity[1]

    if velocity[0] > 0:
        print(ball_pos[0])
        if int(ball_pos[0]) >= int(WIDTH)- BALL_RADIUS:
            velocity[0] = -velocity[0]
            velocity[1] = velocity[1]
    
    if velocity[0] < 0:
        if int(ball_pos[0] - BALL_RADIUS) <= 0:
            velocity[0] = -velocity[0]
            velocity[1] = velocity[1]

    if velocity[1] > 0:
        if int(ball_pos[1]) >= int(HEIGHT)- BALL_RADIUS:
            velocity[0] = velocity[0]
            velocity[1] = -velocity[1]
            
    if velocity[1] < 0:
        if int(ball_pos[1] - BALL_RADIUS) <= 0:
            velocity[0] = velocity[0]
            velocity[1] = -velocity[1]            
            
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
f = simplegui.create_frame("Motion", WIDTH, HEIGHT)

#register event handler
f.set_draw_handler(draw)
f.set_keydown_handler(keydown)

# start frame
f.start()