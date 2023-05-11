import csv

from colored import fg, bg, attr

from datetime import datetime


def view_goals(file_name):
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        reader.__next__()
        for row in reader:
            if (row[2] == "True"):
                print(f"{fg('blue')}Goal:{attr('reset')} {row[0]} - {row[1]} {fg('green')}is completed{attr('reset')}")
            else:
                print(f"{fg('blue')}Goal:{attr('reset')} {row[0]} - {row[1]} {fg('red')}is not completed{attr('reset')}")


def mark_goals(file_name):
    date = datetime.today().strftime('%d/%m/%Y')
    view_goals(file_name)
    goal_name = input(f"Enter the goal name you want to mark as complete: ")
    goal_lists = []
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        for row in reader:
            if (goal_name == row[1]):
                goal_lists.append([date, goal_name, "True"])
            else:
                goal_lists.append(row)
    print(goal_lists)
    with open(file_name, "w") as goal_file:
        writer = csv.writer(goal_file)
        writer.writerows(goal_lists)


def add_goals(file_name):
    date = datetime.today().strftime('%d/%m/%Y')
    goal_name = input(f"Enter your goal name: ")
    if len(goal_name.strip()) == 0:
        print("The goal name input is empty")
        
    else:
        with open(file_name, "a") as goal_file:
            writer = csv.writer(goal_file)
            writer.writerow([date, goal_name, "False"])


def remove_goals(file_name):
    view_goals(file_name)
    goal_name = input(f"Enter the name of the goal you wish to remove: ")
    goal_lists = []
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        for row in reader:
            if (goal_name != row[1]):
                goal_lists.append(row)
    print(*goal_lists)
    with open(file_name, "w") as goal_file:
        writer = csv.writer(goal_file)
        writer.writerows(goal_lists)

def weekly_score(file_name):
    
    score = 0
    total = 0
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        for row in reader:
            if (row[2] == "True"):
                score += 1
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        reader.__next__()
        for row in reader:
            total +=1            
    print(f"Your score this week is: {fg('green')}{score}/{total}{attr('reset')}")
                



