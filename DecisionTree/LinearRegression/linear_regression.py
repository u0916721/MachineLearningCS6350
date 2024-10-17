#Trying something new with numpy instead of vanilla python
import numpy as np

def readData(file_path):
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    return data

#Calculating y_i - wTX - b
#We can optimize this later
def calculateYiMinusWTXI(wT,xI,b=0):
    return xI[-1] - np.dot(wT,xI[:-1]) - b
#See lecture 8 slide 39
def calcOneElementDeltaJ(j,weightVector,data,bias=0):
    deltaJ = 0
    for s in data:
        #print(calculateYiMinusWTXI(weightVector,s))
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
    return weightVector - r * deltaJ

def batchGradientDescent(data,r = 0.01, b = 0):
    #Init the base weight
    weightVector = np.zeros(data.shape[1] - 1)
    wT = weightVector
    for i in range(0,10):
        deltaJ = calculateEnitireDeltaJ(weightVector,data)
        newWeight = updateWeight(weightVector,r,deltaJ)
        #to examine convergence, you can watch the norm of the weight vector difference, ‖wt −wt−1‖, at each step t. 
        # if ‖wt −wt−1‖ is less than a tolerance level, say, 10−6, you can conclude that it converges
        if np.linalg.norm(newWeight - weightVector) <= 10**-6:
            print("Converge!")
            break
    return newWeight

    

file_path = 'slump_test.data'
data = readData(file_path)
batchGradientDescent(data)
