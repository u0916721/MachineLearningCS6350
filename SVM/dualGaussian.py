
from scipy.optimize import minimize
from scipy.spatial import distance
import numpy as np

def dualFunctionOptimizedGuassian(alphaList, xList,gamma):
    leftTerm = np.sum(alphaList)
    y = xList[:, -1]
    x = xList[:, :-1]
    yy = np.outer(y, y) 
    aa = np.outer(alphaList, alphaList) 
    kernel = guassianKernal(x,gamma)
    total = np.sum(aa * yy * kernel) 
    return (1/2) * total - leftTerm

def getWeightVecotr(alphaList,xList):
    y = xList[:, -1]
    x = xList[:, :-1]
    w = 0
    for i in range(0,len(xList)):
        w += alphaList[i] * y[i] * x[i]
    return w
    
    
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

def getAlphasGuassian(C,xList,gamma):
    alphaList = np.zeros(len(xList))
    #lets curry x in with a lambda
    #where x is a 1-D array with shape (n,), from the minimize function
    alphas = minimize(fun=lambda x: dualFunctionOptimizedGuassian(x, xList,gamma),x0=alphaList,bounds=bounds(C,alphaList),constraints={'type': 'eq', 'fun': lambda x: equality(x, xList)}, method='SLSQP')
    return alphas.x
    
    
def readData(file_path):
    #Don’t forget to convert the labels to be in {1, −1}
    data = np.genfromtxt(file_path, delimiter=',')
    for d in data:
        if d[-1] == 0:
            d[-1] = -1
    return data

def guassianKernal(xList,gamma):
    #Based on the reading https://mccormickml.com/2013/08/15/the-gaussian-kernel/
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html
    x = distance.cdist(xList, xList, metric='sqeuclidean')
    x = -1 * (x/gamma)
    return np.exp(x)


def getBias(w,xList,alphaList,c):
    #From the lecture slides
    #Let us find some j 0 < a* < C , what can we get?
    for i in range(0,len(xList)):
        alpha = alphaList[i]
        if 0 < alpha < c:
            y_j = xList[i][-1]
            x_j = xList[i][:-1]
            break
    return y_j - np.dot(x_j, w)

def guassianKernalPerdict(x_i,x,gamma):
    #Based on the reading https://mccormickml.com/2013/08/15/the-gaussian-kernel/
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html
    x = distance.sqeuclidean(x_i, x)
    x = -1 * (x/gamma)
    return np.exp(x)
#From lect 13 slides 68
def gperdict(alphas,xList,sample,gamma,bias=0):
    y = xList[:, -1]
    x = xList[:, :-1]
    sum = 0
    for i in range(0,len(xList)):
        sum += alphas[i]*y[i]*guassianKernalPerdict(x[i],sample,gamma)
    return np.sign(sum+bias)

def countSupportVectors(alphas,c):
    total = 0
    aList = []
    for a in alphas:
        if a > 0 and a < c:
            total +=1
            aList.append(a)
    return (total,aList)
    
    

        
def traindualDual():
    C = [100/873,500/873,700/873]
    #C = [100/873]
    #C = [500/873]
    #C = [700/873]
    Gammas = [0.1,0.5,1,5,100]
    #Gammas = [0.1]
    #Gammas = [0.5]
    #Gammas = [1]
    #Gammas = [5]
    #Gammas = [100]
    trainingData = readData('data/bank-note/train.csv')
    testData = readData('data/bank-note/test.csv')
    # number = 0
    for g in Gammas:
        print(f"For gamma value {g} ")
        for c in C:
            alphas = getAlphasGuassian(c ,trainingData,g)
            w = getWeightVecotr(alphas,trainingData)
            # print(f"The weight vector is {w}")
            bias = getBias(w,trainingData,alphas,c)
            # print(f"The bias is {bias}")
            right = 0
            for t in testData:
                tY = t[-1]
                if np.sign(tY) == gperdict(alphas,trainingData,t[:-1],g):
                    right += 1
            print(f"Total right for C = {c} and Gamma = {g} on testdata is {(right/len(testData)) * 100}")
            rightTraining = 0
            for t in trainingData:
                tY = t[-1]
                if np.sign(tY) == gperdict(alphas,trainingData,t[:-1],g):
                    rightTraining += 1
            print(f"Total right for C = {c} and Gamma = {g} on trainingData is {(rightTraining/len(trainingData)) * 100}")
            # res = countSupportVectors(alphas,c)
            # with open(str(number) + '.txt', 'w') as f:
            #     f.write(f"{res[0]}\n")
            #     for item in res[1]:
            #         f.write(f"{item}\n")
            # number += 1
# traindual()
traindualDual()