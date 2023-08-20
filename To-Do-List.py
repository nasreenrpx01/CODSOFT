# Create an empty list to store tasks
TO_DO_LIST = []

# Use a loop to make the program continuous
while True:
    print("Welcome to Your To-Do List")
    # Display the options
    print("1. Create a List\n2. Update the List.\n3. Track the List\n4. Exit")
    
    # Prompt the user to enter their choice
    option = int(input("Enter your choice:"))
    
    # If the user chose option 1
    if option == 1:
        # Store the user's entered task in 'entered_list_element' variable
        entered_list_element = input("Enter your task to add in the list:")
        TO_DO_LIST.append(entered_list_element)
        print(f"{entered_list_element} is added to the list")
    
    # If the user chose option 2
    elif option == 2:
        #prompt them to chose 'a'to insert or 'b' to remove 
        print("a. Insert\nb. Remove")
        #store the user's choice in 'entered_option' variable
        entered_option = input("Enter your choice:")
        
        # If the user chose option 'a'
        if entered_option == 'a':
            #prompt the user to enter task to add in the list and store it in the 'entered_list_element' variable
            entered_list_element = input("Enter your task to add in your list:")
            #add the stored value in 'entered_list_element' variable in 'TO_DO_LIST' list
            TO_DO_LIST.append(entered_list_element)
            #print that their task is added to the list
            print(f"{entered_list_element} is inserted to the list")

        
        # If the user chose option 'b'
        elif entered_option == 'b':
            #prompt the user to enter task to insert and store it in the 'entered_list_element' variable
            entered_list_element = input("Enter tasks that you want to remove from the list:")
            # Check if the entered task is in the list before removing it
            if entered_list_element in TO_DO_LIST:
                #if the entered task is in the list remove it 
                TO_DO_LIST.remove(entered_list_element)
                #print that the entered task has been removed
                print(f"{entered_list_element} is  removed from the list")
            else:
                #if the entered task is not in the list print "Task not found in the list"
                print("Task not found in the list.")
    
    # If the user chose option 3
    elif option == 3:
        #print the 'TO_DO_LIST' list
        print(TO_DO_LIST)
    
    # If the user chose option 4
    elif option == 4:
        #print farewell statement
        print("Exiting the program,Have a great day!")
        break  # Exit the loop
    else:
        #if the user chooses other than above option print below statement
        print("Invalid option. Please choose a valid option.")
    # Add a blank line for separation
    print("")


 
