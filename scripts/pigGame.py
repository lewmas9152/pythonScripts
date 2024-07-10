import random

def roll() :
    min_players =1
    max_players = 6
    roll_value = random.randint(min_players,max_players)

    return roll_value



while True:
    players = input("Enter the number of players(2-4): ")

    if players.isdigit():

        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("You can have atleast 2 players and a max of 4 players")

    else:
        print("Please enter a valid option")

max_score = 50
players_score = [ 0 for _ in range(players)]

print(players_score)

while max(players_score) < max_score :
    for player in range(players):
        print("\nPlayer", player+1, "turn")
        print("Your current score is", players_score[player],"\n")
        current_score = 0

        while True:
            play_option = input("Do you want to roll (y/n): ").lower()

            if play_option != "y":
                break
            
            else :
                roll_result = roll()

            if roll_result == 1:
                print("You rolled a 1 ,you lose all your points")
                current_score = 0
                break

            else:
                current_score += roll_result
                print("You rolled a", roll_result)
            print("Your current score is", current_score)


    players_score[player] += current_score
    print("Your total score is", players_score[player])
    

    
max_score = max(players_score)
winning_player = players_score.index(max_score) + 1
print("Player", winning_player, "wins the game")



print("Game Over")