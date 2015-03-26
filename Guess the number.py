# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number=0
    
    global game
    game=0
    
    global count100
    count100=0
    
    global count1000
    count1000=0
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0,100)
    
    global game
    game=1
    
    global count100
    count100=7
   
    print
    print 'Guess a number in the range of [0,100)'
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game   
       
    global secret_number
    secret_number = random.randrange(0,1000)
    
    global game
    game=2
 
    global count1000
    count1000=10
    
    print
    print 'Guess a number in the range of [0,1000)'
    
def input_guess(guess):
    # main game logic goes here	
    global count100
    global count1000
    
    print 
    if game==1:
        if count100>0:            
            number=int(guess)
            print 'Guess was ', number
            if number>=100:
                print "The number should be lower than 100"
            elif secret_number>number:
                count100-=1
                print 'Higher'
                print "you have", count100, "guesses remaining"
            
            elif secret_number<number:
                count100-=1
                print 'Lower'
                print "you have", count100, "guesses remaining"
                
            else:
                print 'Correct' 
                range100()
        if count100==0:
            print
            range100()
    
    elif game==2:    
        if count1000>0:
            number=int(guess)
            print 'Guess was ', number
            if number>=1000:
                print "The number should be lower than 1000"
            elif secret_number>number:
                count1000-=1
                print 'Higher'
                print "you have", count1000, "guesses remaining"
            
            elif secret_number<number:
                count1000-=1
                print 'Lower'
                print "you have", count1000, "guesses remaining"
                
            else:
                print 'Correct' 
                range1000()
        if count1000==0:
            print
            range1000()
    
# create frame
frame=simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame

button1=frame.add_button("range(0,100)", range100, 100)
button2=frame.add_button("range(0,1000)", range1000, 100)
inp=frame.add_input("Input Guess", input_guess, 100)

frame.start()

# call new_game 

new_game()
