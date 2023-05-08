from colored import fg, bg, attr

from wellness_functions import add_goals, remove_goals, view_goals, mark_goals, weekly_score

from weight_functions import add_body_weight, view_weight, mark_weight, remove_weight

print(f"{fg('229')}Welcome to the Wellness App!{attr('reset')}")

file_name = "goals.csv"
weight_file_name = "weight.csv"

try: 
    goals_file = open(file_name, "r")
    goals_file.close()
except FileNotFoundError as e:
    goals_file = open(file_name, "w")
    goals_file.write("title,completed\n") 
    goals_file.close() 
    
try: 
    weight_file = open(weight_file_name, "r")
    weight_file.close()  
except FileNotFoundError as e:
    weight_file = open(weight_file_name, "w")
    weight_file.write("weight,pass/fail\n") 
    weight_file.close()

def menu():
    print(f"{fg('blue')}1. Enter 1 to VIEW this weeks wellness goals{attr('reset')}")
    print(f"{fg('blue')}2. Enter 2 to MARK a goal as complete{attr('reset')}")
    print(f"{fg('blue')}3. Enter 3 to ADD your own weekly goal{attr('reset')}")
    print(f"{fg('blue')}4. Enter 4 to REMOVE a weekly goal{attr('reset')}")
    print(f"{fg('blue')}5. Enter 5 to VIEW your weekly score{attr('reset')}")
    print(f"{fg('105')}6. Enter 6 to ADD this weeks bodyweight{attr('reset')}")
    print(f"{fg('105')}7. Enter 7 to VIEW previous weeks bodyweight{attr('reset')}")
    print(f"{fg('105')}8. Enter 8 to MARK last weeks weight if it was lower than the previous weeks.{attr('reset')}")
    print(f"{fg('105')}9. Enter 9 to REMOVE a bodyweight{attr('reset')}")
    print(f"{fg('red')}10. Enter 10 to EXIT{attr('reset')}")
    choice = input(f"Enter your choice: ")
    return choice

user_choice = ""

while user_choice != "10":
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
        remove_weight(weight_file_name)
        
    elif(user_choice == "10"):
        continue
    
    input(f"Press enter to continue.")
    
        
print(f"{fg('229')}Thanks for using the Wellness App, have a nice day!{attr('reset')}")