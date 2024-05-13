import random

print("HELLO, WELCOME!!!👋👋");

options = ["rock", "paper", "scissors"]


computer_wins =0
users_wins=0

while True:
    users_pick = input("What is your pick(rock/scissors/paper or 'q to quit')? ").lower()
    if users_pick not in options :
        break

    randomNo = random.randint(0,2)
    computer_pick = options[randomNo]
    #0=rock,1=scissors,2=paper

    if users_pick == "rock" and computer_pick == "scissors":
        print("You win!!🎊🎉")
        print("The computers pick was",computer_pick+ ".")
        users_wins +=1
    

    elif users_pick == "paper" and computer_pick == "rock":
        print("You win!!🎊🎉")
        print("The computers pick was",computer_pick+ ".")
        users_wins +=1


    elif users_pick == "scissors" and computer_pick == "paper":
        print("You win!!🎊🎉")
        print("The computers pick was",computer_pick+ ".")
        users_wins +=1

    
    else :
        print("Computer Wins")
        print("The computers pick was",computer_pick+ ".")
        computer_wins +=1


print("You have won",users_wins,"times.")
print("The computer has won",computer_wins,"times.")
print("THANK YOU FOR PLAYING 😊😊")

