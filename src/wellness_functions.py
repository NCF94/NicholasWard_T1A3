import csv

def view_goals(file_name):
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        reader.__next__()
        for row in reader:
            if(row[1] == "True"):
                print(f"Goal {row[0]} is completed")
            else:
                print(f"Goal {row[0]} is not completed")
def mark_goals(file_name):
    view_goals(file_name)
    goal_name = input("Enter the goal name you want to mark as complete: ")
    goal_lists = []
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        for row in reader:
            if (goal_name == row[0]):
                goal_lists.append([goal_name, "True"])
            else:
                goal_lists.append(row)
    print(goal_lists)
    with open(file_name, "w") as goal_file:
        writer = csv.writer(goal_file)
        writer.writerows(goal_lists)
    
    
    
def add_goals(file_name):
    goal_name = input("Enter your weekly goal name: ")
    with open(file_name, "a") as goal_file:
        writer = csv.writer(goal_file)
        writer.writerow([goal_name, "False"])
    
def remove_goals(file_name):
    view_goals(file_name)
    goal_name = input("Enter the name of the goal you wish to remove: ")
    goal_lists = []
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        for row in reader:
            if(goal_name != row[0]):
                goal_lists.append(row)
    print(goal_lists)
    
def weekly_score(file_name):
# function for the score, each goal listed marked as complete will = 1 point.
# need to figure out how to make score out of number of items in the list.

