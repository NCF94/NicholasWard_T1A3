import csv

from colored import fg, bg, attr


def view_goals(file_name):
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        reader.__next__()
        for row in reader:
            if (row[1] == "True"):
                print(f"{fg('blue')}Goal:{attr('reset')} '{row[0]}' {fg('green')}is completed{attr('reset')}")
            else:
                print(f"{fg('blue')}Goal:{attr('reset')} '{row[0]}' {fg('red')}is not completed{attr('reset')}")


def mark_goals(file_name):
    view_goals(file_name)
    goal_name = input(f"Enter the goal name you want to mark as complete: ")
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
    goal_name = input(f"Enter your weekly goal name: ")
    with open(file_name, "a") as goal_file:
        writer = csv.writer(goal_file)
        writer.writerow([goal_name, "False"])


def remove_goals(file_name):
    view_goals(file_name)
    goal_name = input(f"Enter the name of the goal you wish to remove: ")
    goal_lists = []
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        for row in reader:
            if (goal_name != row[0]):
                goal_lists.append(row)
    print(goal_lists)
    with open(file_name, "w") as goal_file:
        writer = csv.writer(goal_file)
        writer.writerows(goal_lists)

def weekly_score(file_name):
    pass
# function for the score, each goal listed marked as complete will = 1 point.
# need to figure out how to make score out of number of items in the list


def add_body_weight(weight_file_name):
    view_weight(weight_file_name)
    body_weight = input(f"Enter the week number and your body weight (e.g Week 1 - 80kg): ")
    with open(weight_file_name, "a") as weight_file:
        writer = csv.writer(weight_file)
        writer.writerow([body_weight, "False"])


def mark_weight(weight_file_name):
    view_weight(weight_file_name)
    week_weight = input(f"Enter the week/weight you want to mark as lower than the previous week: ")
    weight_lists = []
    with open(weight_file_name, "r") as weight_file:
        reader = csv.reader(weight_file)
        for row in reader:
            if (week_weight == row[0]):
                weight_lists.append([week_weight, "True"])
            else:
                weight_lists.append(row)
    print(weight_lists)
    with open(weight_file_name, "w") as weight_file:
        writer = csv.writer(weight_file)
        writer.writerows(weight_lists)


def view_weight(weight_file_name):
    with open(weight_file_name, "r") as weight_file:
        reader = csv.reader(weight_file)
        reader.__next__()
        for row in reader:
            if (row[1] == "True"):
                print(
                    f"{fg('blue')}Bodyweight:{attr('reset')} '{row[0]}' {fg('green')}Congratulations, this weeks weight is less then last week! Keep going, you got this!{attr('reset')}")
            else:
                print(
                    f"{fg('blue')}Bodyweight:{attr('reset')} '{row[0]}' {fg('red')}This weeks weight is more then last weeks. Thats okay though, this is a long process{attr('reset')}")
