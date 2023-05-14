import pytest
import csv
from wellness_functions import weekly_score

# This test check  the 'score' for the user's weekly goals.
# It does this by checking if score is equal to total.
# If I change all the values in the "test_score.csv" file to true, the test passes. because the score is = to the total (6/6)
# If I change a value to False, the test fails because score is not = to total.

def test_weekly_score():
    file_name = "tests/test_score.csv"
    
    score = 6
    total = 6
    with open(file_name, "r") as goal_file:
        reader = csv.reader(goal_file)
        reader.__next__()
        for row in reader:
            if (row[2] == "False"):
                score -= 1
            
    total_score = f"{score}/{total}"     
    assert weekly_score(file_name) == total_score
        
    # This is my second test
