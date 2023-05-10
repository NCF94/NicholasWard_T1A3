#!/bin/bash

# chech if python is installed - DO IN ASSIGNMENT
python3 -m venv wellness-venv
source wellness-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py


#./run.sh to run script