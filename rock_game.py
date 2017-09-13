#simulation.py

from random import random, randrange        #import random
print("Hello, welcome to this game of Rock, Paper, Scissors!")       #greet users
print("We'l be generous and let you go fist.") #Inform users that they'l go first

def main(): #set up main function

    dvalue = ""
        
    play = input("Please choose Rock Paper or Scissors...")  #ask user to make a move
    comp = (randrange(1,4,1))             #get computer to make a randome move

    if comp == 1:
        dvalue = "Rock"
        print("Computer chose Rock")
    if comp == 2:
        dvalue = "Paper"
        print("Computer chose Paper")
    if comp == 3:
        dvalue = "Scissors"
        print("Cimouter chose Scissors")
    
    
    
    if play == dvalue:
        print ("It's a tie")
    
    elif play == "Rock" and dvalue == "Paper":
        print ("Computer Wins")

    elif play == "Rock" and dvalue == "Scissors":
        print ("You wins!")

    elif play == "Scissors" and dvalue == "Rock":
        print ("Computer Wins")

    elif play == "Scissors" and dvalue == "Paper":
        print ("Computer Wins")

    elif play == "Paper" and dvalue == "Rock":
        print ("You Win!")
    elif play == "Paper" and dvalue == "Scissors":
        print ("Computer Wins")

    return 0

main()
