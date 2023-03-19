def user_choice():
    
    choice ='WRONG'
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        
    
    
        choice = input("Please enter a number (0-10): ")
        
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
            
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
            else:
                within_range = False
        
    
    return int(choice)
#Simple User Interaction
#Finally let's combine all of these ideas to create a small game where a user can choose a "position" in an existing list and replace it with a value of their choice.
#Simple User Interaction
Finally let's combine all of these ideas to create a small game where a user can choose a "position" in an existing list and replace it with a value of their choice.