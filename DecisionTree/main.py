# Entry point for our application. 
import os
# Import our math helper library.
import math_helper

def read_file(file_path):
    with open(file_path, mode='r') as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    #Will change with args later no need to be bogged down by those details now though. 
    relative_path = os.path.join('DataSets', 'Car', 'car.data')
    read_file(relative_path)
    #Simple test
    print(math_helper.calcEntropy())