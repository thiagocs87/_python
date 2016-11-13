import random

def name_to_number(name):
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error"

def number_to_name(number):

    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error"
    
def rpsls(player_choice): 
    
    player_number = name_to_number(player_choice)
    
    computer_number = random.randrange(0, 5)
    
    computer_choice = number_to_name(computer_number)
    
    print("Player choose " + player_choice)
    
    print("Computer choose " + computer_choice)
    
    difference = player_number - computer_number
    
    if difference == 0:
        print("Player and Computer tie")
    else:
        module = difference % 5
        if module in(1,2):
            print("Player wins")
        else:
            print("Computer wins")
    
    print("")
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")