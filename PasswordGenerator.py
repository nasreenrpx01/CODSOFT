#This is after i learned fucntion and exception handling
#import random and string module
import random
import string
#print the welcome statement
print("This is a program to generate a strong password!")
#write a passwordgenerator function
def Pwdgen(Length):
    try:
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(Length))
        print("Password generated successfully!")
        return random_string
    except ValueError:
        print("Invalid number. Please enter a valid number.")
#Loop to continue the program
while True:
    try:
        Length = int(input("Enter the desired length of the password: "))
        if Length <= 0:
            print("Please enter a positive integer.")
        else:
            random_str = Pwdgen(Length)
            print("Password:", random_str)
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
