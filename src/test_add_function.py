import pytest
import csv
from wellness_functions import add_goals







# This is my first test.
# The purpose of this test is to test that the add_goals function correctly adds a new line (new goal) to the goals.csv file.
# For the purpose of testing, this test uses a test file called "test_add.csv"

def test_add_goals(monkeypatch):
    length = 0
    test_add_file = "tests/test_add.csv"
    
    with open(test_add_file) as f:
        reader = csv.reader(f)
        length = sum(1 for row in reader)
        
    inputs = iter(["Gym", "False"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    add_goals(test_add_file)
    with open(test_add_file) as f:
        reader = csv.reader(f)
        length_new = sum(1 for row in reader)
    print(length)
    print(length_new)
    assert length_new == length + 1
    

    



