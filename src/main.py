from wellness_functions import add_goals, remove_goals, view_goals, mark_goals, weekly_score, add_body_weight, view_weight, mark_weight

print("Welcome to the Wellness App!")

file_name = "goals.csv"
weight_file_name = "weight.csv"

def menu():
    print("1. Enter 1 to view this weeks welness goals")
    print("2. Enter 2 to mark a goal as complete")
    print("3. Enter 3 to add your own weekly goal")
    print("4. Enter 4 to remove a weekly goal")
    print("5. Enter 5 to see your weekly score")
    print("6. Enter 6 to input this weeks bodyweight")
    print("7. Enter 7 to view previous weeks bodyweight")
    print("8. Enter 8 to mark last weeks weight if it was lower than the previous weeks.")
    print("9. Enter 9 to exit")
    choice = input("Enter your choice: ")
    return choice

user_choice = ""

while user_choice != "9":
    user_choice = menu()
    
    if(user_choice == "1"):
        view_goals(file_name)
        
    elif(user_choice == "2"):
        mark_goals(file_name)
        
    elif(user_choice == "3"):
        add_goals(file_name)
        
    elif(user_choice == "4"):
        remove_goals(file_name)
        
    elif(user_choice == "5"):
        weekly_score(file_name)
        
    elif(user_choice == "6"):
        add_body_weight(weight_file_name)
        
    elif(user_choice == "7"):
        view_weight(weight_file_name)
        
    elif(user_choice == "8"):
        mark_weight(weight_file_name)
        
    elif(user_choice == "9"):
        continue
    
    input("Press enter to continue.")
    
        
print("Thanks for using the Wellness App, have a nice day!")