#Trying something new with numpy instead of vanilla python
import numpy as np

def readData(file_path):
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    return data

#Data in the form of a numpy array
#Returns a vector for perdiction
def batchGradientDescent(data):
    #Init the base weight
    weightVector = np.zeros(data.shape[1] - 1)
    wT = weightVector
    
    return None

#xi is the sample vector
#weightVector is our curent weightVector
# bias which is optional for now is zero
#xj is the xjth element of the the sample vector
def individualGradient(weightVector,xi,xj,bais=0):
    #Have this one take care of yi
    return None
#Calculating y_i - wTX - b
#We can optimize this later
def calculateYiMinusWTXI(wT,xI,b=0):
    return xI[-1] - np.dot(wT,xI[:-1]) - b
#See lecture 8 slide 39
def calcOneElementDeltaJ(j,weightVector,data,bias=0):
    deltaJ = 0
    for s in data:
        deltaJ -= (calculateYiMinusWTXI(weightVector,s)) * s[j]
    return deltaJ
#Calcuates an entire delta J
def calculateEnitireDeltaJ(weightVector,data,bias=0):
    deltaJ = []
    for i in range(0,len(weightVector)):
        tempJ = calcOneElementDeltaJ(i,weightVector,data,bias)
        deltaJ.append(tempJ)
    return np.array(deltaJ)
#Gives a new weight value
def updateWeight(weightVector,r,deltaJ):
    return weightVector - r * deltaJ * weightVector

def batchGradientDescent(data,r = 0.5, b = 0):
    #Init the base weight
    weightVector = np.zeros(data.shape[1] - 1)
    wT = weightVector
    while True:
        deltaJ = calculateEnitireDeltaJ(weightVector,data)
        newWeight = updateWeight(weightVector,r,deltaJ)
        if newWeight - weightVector == 0:
            break
    return newWeight

    

file_path = 'slump_test.data'
data = readData(file_path)

print(data)
