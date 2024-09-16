# Entry point for our application. 
import os
# Import our math helper library.
import math_helper
from node import node

#Our training data
trainingData = []


def read_file(file_path):
    with open(file_path, mode='r') as file:
        for line in file:
            # Creates a 2d array where entry is a sample
            trainingData.append(line.strip().split(','))
            #Note: Do I need to extract all the possible feature values or can that be handled implicitly?

if __name__ == "__main__":
    #Will change with args later no need to be bogged down by those details now though. 
    relative_path = os.path.join('DataSets', 'Car', 'car.data')
    read_file(relative_path)
    n = node(None,None,trainingData)
    n.calcLabel()
    print(n.label)

