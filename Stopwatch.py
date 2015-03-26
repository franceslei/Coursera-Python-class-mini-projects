
import simplegui

# define global variables
def new_game():
    global t
    t=0
    
    global s
    s='0:00.0'
    
    global counter_stop
    counter_stop=0
    
    global counter_whole_second
    counter_whole_second=0   
    
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t0=t/10
    t3=int(t%10)
    t2=int(t0)%60
    t1=int(t0)/60
    s1=str(t1)
    if t2<10:
        s2='0'+str(t2)
    else:
        s2=str(t2)
    s3=str(t3)
    return s1+':'+s2+'.'+s3  
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    global counter_stop
    global counter_whole_second
    timer.stop()
    counter_stop+=1
    if t%10==0:
        counter_whole_second+=1
def reset():
    timer.stop()
    new_game()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t+=1
    
    global s
    s=format(t)

# define draw handler
def time(canvas):
    canvas.draw_text(s,[100,110],42,"Red")
    canvas.draw_text(str(counter_whole_second)+'/'+str(counter_stop),[235,30],30,"White")
    
# create frame
frame=simplegui.create_frame("Stopwatch: The Game",300,200)

# register event handlers
button1 = frame.add_button("Start",start,80)
button2 = frame.add_button("Stop",stop,80)
button3 = frame.add_button("Reset",reset,80)
frame.set_draw_handler(time)

timer = simplegui.create_timer(100,timer_handler)
# start frame
frame.start()
new_game()