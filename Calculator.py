# print the welcome statement
print("Calculator for basic arithematic operations.\n")
# Initialize with default values
Number1 = 0
Number2 = 0
# Start a loop so program continues
while True:
   # prompt the user for two numbers
    User_input1 = input("Enter Your First Number:")
    User_input2 = input("Enter Your Second Number:")
    # check if the both numbers are float
    if '.' in User_input1 and '.' in User_input2:
        Number1 = float(User_input1)
        Number2 = float(User_input2)
    # check if both numbers are digits , if they are then convert them into integer
    elif User_input1.isdigit() and User_input2.isdigit():
        Number1 = int(User_input1)
        Number2 = int(User_input2)
    else:
        # if the input is other than digit print below statement
        print("invalid input, please put a valid number")
        continue    # Restart the loop to get valid input
    # Dsiplay the list of operations
    print("List of Operations:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponentiation\n7.Exit")
    # prompt user to enter their choice
    option = int(input("Enter your choice:"))
    # if the user chose option 1
    if option == 1:
        # add both inputs and store it in 'Sum' variable
        Sum = Number1 + Number2
        # print the value stored in "Sum variable" along with the inputs
        print(f"Addition of {Number1} and {Number2} is {Sum}")
    # if the user chose option 2
    elif option == 2:
        # subtract both the input numbers and store it "Sub" variable
        Sub = Number1 - Number2
        # print the value stored in "Sub" variable along with the inputs
        print(f"Subraction of {Number1} and {Number2} is {Sub}")
    #if the user chose option 3
    elif option == 3:
        #multiply both input numbers and store it "Mult" variable
        Mult = Number1 * Number2
        # print the value stored in "Mult" variable along with the inputs
        print(f"Multiplication of {Number1} and {Number2} is {Mult}")
    #if the user chose option 4
    elif option == 4:
        #Divide both input numbers and store it "Div" variable
        Div = Number1/Number2
        # print the value stored in "Div" variable along with the inputs
        print(f"Division of {Number1} and {Number2} is {Div}")
    #if the user chose option 5
    elif option == 5:
        #modulus both input numbers and store it "Mod" variable
        Mod = Number1 % Number2
        # print the value stored in "Mod" variable along with the inputs
        print(f"Modulus of {Number1} and {Number2} is {Mod}")
    #if the user chose option 6
    elif option == 6:
        #use power fucntion Number1 as base, Number2 as exponent and store it "Mod" variable
        Power_Of = pow(Number1, Number2)
        # print the value stored in "Power_Of" variable along with the inputs
        print(f"{Number1} as base and {Number2} as exponent result is {Power_Of}")
    #if the user chose option 7
    elif option == 7:
        #print the exit statement and exit the loop
        print("Exiting the program, Have a Great day")
        break
    #if the user chose option other than mentioned above print invalid option statement
    else:
        print("Invalid option. Please choose a valid option.")

print()#Empty statement for space between operations
