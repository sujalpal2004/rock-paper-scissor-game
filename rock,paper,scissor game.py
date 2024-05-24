import random
choices = ["rock" , "paper" , "scissor"]

computer = random.choice(choices)
player = input(" Enter your Choice ? 1.rock , 2.paper , 3.scissor :")

if player==computer:
    print("Computer Choice : ",computer)
    print("player Choice : ",player)
    print("Wow! That's a tie.")
elif player == "rock":
     if computer == "paper":
        print("Computer Choice : ",computer)
        print("player Choice : ",player)
        print("That's so sad ! You lost.try again")
     if computer == "scissor":
        print("Computer Choice : ",computer)
        print("player Choice : ",player)
        print("Congratulations! You won.") 

elif player == "scissor":
     if computer == "paper":
        print("Computer Choice : ",computer)
        print("player Choice : ",player)
        print("Congratulations! You won.")
     if computer == "rock":
        print("Computer Choice : ",computer)
        print("player Choice : ",player)
        print("That's so sad ! You lost.try again")         

elif player == "paper":
     if computer == "rock":
        print("Computer Choice : ",computer)
        print("player Choice : ",player)
        print("Congratulations! You won.")
     if computer == "scissor":
        print("Computer Choice : ",computer)
        print("player Choice : ",player)
        print("That's so sad ! You lost.try again")         



