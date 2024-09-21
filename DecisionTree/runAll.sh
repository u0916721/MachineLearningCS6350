#!/bin/bash

# Wipe output.txt clean if it exists
> output.txt

# Run Python files with Python 3 and pipe output to both console and output.txt

echo "Car data decision tree being built and run against with test data" 
python3 car.py 

echo "Car data decision tree being built and run against with training data"
python3 car_test_on_self_train.py 

echo "Bank decision tree being built and run against with test data" 
python3 bank.py 

echo "Bank decision tree being built and run against with training data" 
python3 bank_test_on_self_train.py 