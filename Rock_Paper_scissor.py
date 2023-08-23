import random
#print welcome statement
print("Welcome to Rock-Paper-Scissors Game!!")
print("Game on!!")
#initialize both score variables ton '0'
Userwins = 0
Computerwins = 0
#create a list of rock and scissor for computer to select from
things = ["rock", "paper", "scissor"]
#print list of choices user can make
print("You have three choices to make: Rock, Paper, Scissor")
#define a while loop so the program continues
while True:
    # User's input and validation
    User_answer = input("Enter your choice: ").lower()  # Convert to lowercase
    if User_answer not in things:
        print("Invalid option, choose a valid option")
        continue

    # Computer's choice
    Computer_answer = random.choice(things)
    print("Computer's choice:", Computer_answer)

    # Determine the winner
    if User_answer == Computer_answer:
        print("It's a tie")
    elif User_answer == things[0] and Computer_answer == things[1]:
        print("You lose!!")
        Computerwins += 1
    elif User_answer == things[0] and Computer_answer == things[2]:
        print("You win!!")
        Userwins += 1
    elif User_answer == things[1] and Computer_answer == things[2]:
        print("You lose!!")
        Computerwins += 1
    elif User_answer == things[1] and Computer_answer == things[0]:
        print("You win!!")
        Userwins += 1
    elif User_answer == things[2] and Computer_answer == things[1]:
        print("You lose!!")
        Computerwins += 1
    elif User_answer == things[2] and Computer_answer == things[0]:
        print("You win!!")
        Userwins += 1

    # Check if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

# Print the final scores and exit message
print(f"Your score is {Userwins} and Computer score is {Computerwins}")
print("Exiting the program, have a great day")

