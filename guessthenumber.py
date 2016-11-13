import simplegui
import random

range = 100
number_guesses = 7
computer_number = 0

def new_game():
    global computer_number
    frame = simplegui.create_frame("Mini-project", 200,300)
    frame.add_button("Range 1 to 100", range100)
    frame.add_button("Range 1 to 1000", range1000)
    frame.add_input("Guess",input_guess,50)
    print("New Game - Range is from 0 to " + str(range))
    print("Number of remaining guesses is " + str(number_guesses))
    computer_number = random.randint(1,range)
    
def range100():
    global range
    global number_guesses
    range = 100
    number_guesses = 7
    new_game()

def range1000():
    global range
    global number_guesses
    range = 1000
    number_guesses = 10
    new_game()
    
def input_guess(guess):
    global number_guesses
    global computer_number
    guess = int(guess)
    print("")
    print("Guess was " + str(guess))
    
    if guess < computer_number:
        number_guesses -= 1
        print("Higher!")
    elif guess > computer_number:
        number_guesses -= 1
        print("Lower!")
    else:
        print("correct")
        print("")
        new_game()
        
    if(number_guesses == 0):
        print("You lose!!")
        print("")
        new_game()
    else:
        print("Number of remaning guesses " + str(number_guesses))
    
new_game()