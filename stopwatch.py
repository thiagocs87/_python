#"Stopwatch: The Game"

import simplegui

# define global variables
watch = 0
minute = "0" 
second = "0"
milisecond = "0"
score = 0
tries = 0
score_parameter = 5

def format_score():
    return str(score) + "/" + str(tries)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    global minute
    global second
    global milisecond
    
    if t < 10:
        minute = "0"
        second = "0"
        milisecond = str(t)
    else:
        if t//10 >= 60:
            minute = str((t//600))
            second = str((t//10) % 60)
            milisecond = str(t - (int(minute) * 600) - (int(second) * 10))
        else:
            minute = "0"
            second = str((t//10) % 60)
            milisecond = str(t - (int(second) * 10))

    if len(minute) == 1:
        minute = "0" + minute
    
    if len(second) == 1:
        second = "0" + second
    
    return minute + ":" + second + "." + milisecond
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global tries
    global score
    
    if timer.is_running():
        if int(minute) > 0:
            if int(second) == 0 and int(milisecond) == 0:
                score += 1
            if int(second) % 1 == 0 and int(milisecond) == 0:
                score += 1
        if int(minute) == 0:
            if int(second) % 1 == 0 and int(milisecond) == 0:
                score += 1

        tries += 1
        timer.stop()

def reset():
    global watch
    global score
    global tries
    watch = 0
    tries = 0
    score = 0
    timer.start()

# define event handler for timer with 0.1 sec interval
def tick():
    global watch
    watch += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(watch),[130,180], 60, 'Red')
    canvas.draw_text(format_score(),[315,45], 40, 'White')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 400,300)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100,tick)
button1 = frame.add_button("Start", start)
button2 = frame.add_button("Stop", stop)
button3 = frame.add_button("Reset", reset)


# start frame
frame.start()