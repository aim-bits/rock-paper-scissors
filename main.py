import random

    
#Game Operations for Rock
def game():
    #create a list
    gameOptions = ["Rock", "Paper", "Scissors"]

    #user selection
    selection = input("Choose R for Rock, P for Paper, S for Scissors: ")
    
    while (not(selection.upper() == "R" or selection.upper() == "P" or selection.upper() =="S" )):
        print("Wrong Selection. try again")
        
        return game()
    
    def rock_selection():
            #display user and CPU selection
        player_move = "Rock" 
        print(f"Player({player_move})")
        cpu_move = random.choice(gameOptions)
        print(f"CPU({cpu_move})")
        if player_move == cpu_move:
            print("Tie!!... try again")
            return game()
        if cpu_move == "Paper":
            print("Computer Wins!!")
        elif cpu_move == "Scissors":
            print("You Win!!")
            
    def paper_selection():
        #display user and CPU selection
        player_move = "Paper" 
        print(f"Player({player_move})")
        cpu_move = random.choice(gameOptions)
        print(f"CPU({cpu_move})")
        if player_move == cpu_move:
            print("Tie!!... try again")
            return game()
        if cpu_move == "Scissors":
            print("Computer Wins!!")
        elif cpu_move == "Rock":
            print("You Win!!")
        
    def scissors_selection():
        #display user and CPU selection
        player_move = "Scissors" 
        print(f"Player({player_move})")
        cpu_move = random.choice(gameOptions)
        print(f"CPU({cpu_move})")
        if player_move == cpu_move:
            print("Tie!!... try again")
            return game()
        if cpu_move == "Rock":
            print("Computer Wins!!")
        elif cpu_move == "Paper":
            print("You Win!!")
            
        
    if selection.upper() == "R":
        return rock_selection()
    elif selection.upper() == "P":
        return paper_selection()
    elif selection.upper() == "S":
        return scissors_selection()
    
            
   
                


game()

        
        
    