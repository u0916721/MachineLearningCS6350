
from scipy.optimize import minimize
import numpy as np

#This is the function we want to minimize to get an alpa
def dualFunction(alphaList,xList):
    leftTerm = sum(alphaList)
    total = 0
    for i in range(0,len(xList)):
        alpha_i = alphaList[i]
        y_i = xList[i][-1]
        x_i = xList[i][:-1]
        for j in range(0,len(xList)):
            alpha_j = alphaList[j]
            y_j = xList[j][-1]
            x_j = xList[j][:-1]
            total += y_i * y_j * alpha_i * alpha_j * np.dot(x_i,x_j) 
    return (1/2)* total - leftTerm
#the sum_i alpha_iy_i =0
def equality(alphaList,xList):
    total = 0
    for i in range(0,len(xList)):
        total+= alphaList[i]*xList[i][-1] 
    return total

#The bounds for each alpha
def bounds(C,alphaList):
    retArr = []
    for a in alphaList:
        retArr.append((0,C))
    return retArr    

def getAlphas(C,xList):
    alphaList = np.zeros(len(xList))
    #lets curry x in with a lambda
    #where x is a 1-D array with shape (n,), from the minimize function
    alphas = minimize(fun=lambda x: dualFunction(x, xList),x0=alphaList,bounds=bounds(C,alphaList),constraints={'type': 'eq', 'fun': lambda x: equality(x, xList)}, method='SLSQP')
    return alphas.x
    
def readData(file_path):
    #Don’t forget to convert the labels to be in {1, −1}
    data = np.genfromtxt(file_path, delimiter=',')
    for d in data:
        if d[-1] == 0:
            d[-1] = -1
    return data

def traindual():
    trainingData = readData('data/bank-note/train.csv')
    testData = readData('data/bank-note/test.csv')
    alphas = getAlphas(1,trainingData)
    print("here")
    print(alphas)
    return None

traindual()