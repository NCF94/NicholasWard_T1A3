from wellness_functions import add_goals, remove_goals, view_goals, mark_goals, weekly_score

print("Welcome to the Wellness App")

file_name = "goals.csv"

def menu():
    print("1. Enter 1 to view this weeks welness goals")
    print("2. Enter 2 to mark a goal as complete")
    print("3. Enter 3 to add your own weekly goal")
    print("4. Enter 4 to remove a weekly goal")
    print("5. Enter 5 to see your weekly score")
    print("6. Enter 6 to exit")
    choice = input("Enter your choice: ")
    return choice

user_choice = ""

while user_choice != "6":
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
        
    elif(user_choice = "6"):
        continue
    
    input("Press enter to continue.")
    
        
print("Thanks for using the Wellness App, have a nice day")