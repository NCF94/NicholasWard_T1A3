import csv

from colored import fg, bg, attr

from datetime import datetime

def add_body_weight(weight_file_name):
    date = datetime.today().strftime('%d/%m/%Y')
    
    view_weight(weight_file_name)
    body_weight = input(f"Enter your body weight (e.g 80kgs): ")
    if len(body_weight.strip()) == 0:
        print("The bodyweight input is empty")
        
    else:
       with open(weight_file_name, "a") as weight_file:
            writer = csv.writer(weight_file)
            writer.writerow([date, body_weight, "False"])


def mark_weight(weight_file_name):
    date = datetime.today().strftime('%d/%m/%Y')
    
    view_weight(weight_file_name)
    week_weight = input(f"Enter the week/weight you want to mark as lower than the previous week eg ('10/05/2023', '70kgs'): ")
    weight_lists = []
    with open(weight_file_name, "r") as weight_file:
        reader = csv.reader(weight_file)
        for row in reader:
            if (week_weight == row[1]):
                weight_lists.append([date,week_weight, "True"])
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
            if (row[2] == "True"):
                print(
                    f"{fg('blue')}Bodyweight:{attr('reset')} {row[0]} - {row[1]} {fg('green')}This weeks weight is less then last week!{attr('reset')}")
            else:
                print(
                    f"{fg('blue')}Bodyweight:{attr('reset')} {row[0]} - {row[1]} {fg('red')}This weeks weight is more then last weeks!{attr('reset')}")


def remove_weight(weight_file_name):
    view_weight(weight_file_name)
    week_weight = input(f"Enter the weight you wish to remove e.g 80kgs: ")
    weight_lists = []
    with open(weight_file_name, "r") as weight_file:
        reader = csv.reader(weight_file)
        for row in reader:
            if (week_weight != row[1]):
                weight_lists.append(row)
    print(*weight_lists)
    with open(weight_file_name, "w") as weight_file:
        writer = csv.writer(weight_file)
        writer.writerows(weight_lists)