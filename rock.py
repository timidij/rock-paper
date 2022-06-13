# Rock, Paper, Scissors Game Task

import random




# function for player option validation
def player_option():
    player_choice = input ("Choose from either Rock, Paper or Scissors: ")
    if player_choice in ["Rock", "rock", "r", "R"]:
        player_choice = "R"
    elif player_choice in ["Paper", "paper", "p", "P"]:
        player_choice = "P"
    elif player_choice in ["Scissors", "scissors", "s", "S"]:
        player_choice = "S"


    return player_choice

# function for CPU option validation
def computer_option():
    # list created
    picking_choice = ["R", "P", "S"]

    cpu_choice = random.choice(picking_choice)
    return cpu_choice


def verify():

    while True:
        # Initail player VS CPU scores
        player_wins = 0
        cpu_wins = 0
        # playing condition
        print("")  # creating space
        player_choice = player_option()
        cpu_choice = computer_option()
        print("")  # creating space


        # creating condition for "R" as "Rock"
        if player_choice == "R":
            if cpu_choice == "R":
                print("You and CPU chose 'Rock'. It's a Tie!")

            elif cpu_choice == "P":
                print("You chose 'Rock' while the CPU chose 'Paper'. You lose.")
                cpu_wins += 1

            elif cpu_choice == "S":
                print("You chose 'Rock' while the CPU chose 'Scissors'. You WIN!!!.")
                player_wins += 1


        # creating condition for "P" as "Paper"
        elif player_choice == "P":
            if cpu_choice == "R":
                print("You chose 'Paper' while the CPU chose 'Rock'. You WIN!!!.")
                player_wins += 1

            elif cpu_choice == "P":
                print("You chose 'Paper' while the CPU chose 'Paper'. You Tied.")

            elif cpu_choice == "S":
                print("You chose 'Paper' while the CPU chose 'Scissors'. You lose.")
                cpu_wins +=1

        # creating condition for "S" as "Scissors"
        elif player_choice == "S":
            if cpu_choice == "R":
                print("You chose 'Scissors' while the CPU chose 'Rock'. You lose.")
                cpu_wins+=1

            elif cpu_choice == "P":
                print("You chose 'Scissors' while the CPU chose 'Paper'. You WIN!!!.")
                player_wins +=1


            elif cpu_choice == "S":
                print("You chose 'Scissors' while the CPU chose 'Scissors'. You Tied.")

        else:
            print("ERROR!!!...Please check the options and try input again.")
        print("")
        print("player wins: " + str(player_wins))
        print("cpu wins: " + str(cpu_wins))
        print("")
        verify()
verify()