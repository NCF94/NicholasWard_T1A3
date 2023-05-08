import csv

from colored import fg, bg, attr

from datetime import datetime

def add_body_weight(weight_file_name):
    date = datetime.today().strftime('%d/%m/%Y')
    
    view_weight(weight_file_name)
    body_weight = input(f"Enter the week number and your body weight (e.g 80kg): ")
    with open(weight_file_name, "a") as weight_file:
        writer = csv.writer(weight_file)
        writer.writerow([(date, body_weight), "False"])


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
    print(*weight_lists)
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
                    f"{fg('blue')}Bodyweight:{attr('reset')} {row[0]} {fg('green')}Congratulations, this weeks weight is less then last week! Keep going, you got this!{attr('reset')}")
            else:
                print(
                    f"{fg('blue')}Bodyweight:{attr('reset')} {row[0]} {fg('red')}This weeks weight is more then last weeks. Thats okay though, this is a long process{attr('reset')}")


def remove_weight(weight_file_name):
    view_weight(weight_file_name)
    week_weight = input(f"Enter the weight you wish to remove e.g ('08/05/2023', '70kg'): ")
    weight_lists = []
    with open(weight_file_name, "r") as weight_file:
        reader = csv.reader(weight_file)
        for row in reader:
            if (week_weight != row[0]):
                weight_lists.append(row)
    print(*weight_lists)
    with open(weight_file_name, "w") as weight_file:
        writer = csv.writer(weight_file)
        writer.writerows(weight_lists)