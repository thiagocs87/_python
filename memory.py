# implementation of card game - Memory

import simplegui
import random

CARD_WIDTH = 50
CARD_HEIGHT = 100
state_1 = -1
state_2 = -1
turns = 0

# helper function to initialize globals
def new_game():
    global list_1, list_print, turns
    turns = 0
    state_1 = 0
    state_2 = 0
    list_print = [False for i in range(16)]
    list_1 = [i % 8 + 1 for i in range(16)]
    random.shuffle(list_1)
    print list_1
    
# define event handlers
def mouseclick(position):
    global list_1, state_1, state_2, turns
    count = 0
    pos_array = (position[0] - position[0] % CARD_WIDTH) / CARD_WIDTH

    if list_print[pos_array] == True:
        return
    
    if state_1 != -1 and state_2 != -1:
        if list_1[state_1] != list_1[state_2]:
            list_print[state_1] = False
            list_print[state_2] = False
            state_1 = -1
            state_2 = -1
            turns += 1
        else:     
            state_1 = -1
            state_2 = -1
            turns += 1
    
    for n in list_print:
        if pos_array == count and state_1 == -1:
            state_1 = pos_array
            list_print[count] = True
        elif pos_array == count and state_1 != -1:
            state_2 = pos_array
            list_print[count] = True		
        count += 1
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global label, turns
    count = 0
    pos = 0
    for num in list_1:
        if list_print[count] == True:
            canvas.draw_polygon([(pos,0),(pos+CARD_WIDTH,0),(pos+CARD_WIDTH,CARD_HEIGHT),(pos,CARD_HEIGHT)],1,"White", "Green")
            canvas.draw_text(str(num), (15+pos,66), 50, "White")
        else:     
            canvas.draw_polygon([(pos,0),(pos+CARD_WIDTH,0),(pos+CARD_WIDTH,CARD_HEIGHT),(pos,CARD_HEIGHT)],1,"White", "Black")
        pos += 50
        count += 1
        label.set_text("Turns = " + str(turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game, 150)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric