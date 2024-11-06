#This is the code that contains perceptron code.
#This assumes d is a numpy data frame
import numpy as np

def perceptronTrain(D,Maxiter):
    #Init weight vector to be the size of the data
    weightVector = np.zeros(len(D[0])-1,dtype = float) # more here, based on size of ds
    bias = 0
    for i in range(0,Maxiter):
        #Should shuffle the array on each pass optional
        #np.random.shuffle(D)
        for d in D:
            y = d[-1] # This is the true label of the sample d
            a = activationPerceptron(weightVector,d,bias)
            #ya should always be positive if is correct this is the online error driven aspect of perceptron
            ya = y * a
            a = np.sign(a)
            #Did we make an error, this is the same as y_i != y
            # as -y * -y = +y and +y * +y = y
            if a != y:
                #Then we update the weight vector and bias
                weightVector = weightVector + y*d[:-1]
                bias = 0

    #Here we return a tuple with the weight vector and its bias    
    print(bias)
    return (weightVector,0)
#returns the activations for this sample
def activationPerceptron(weightVector,sample,bias):
    s = sample[:-1]
    return np.dot(weightVector,s) + bias
# Returns the label, given a testSample
def perceptronGuess(weightVector,bias,testSample):
    a = activationPerceptron(weightVector,testSample,bias)
    if a >= 0:
        return 1
    else:
        return 0
def readData(file_path):
    data = np.genfromtxt(file_path, delimiter=',')
    return data
def perceptronTest():
    #Read in the data in numpy 2d arrays
    trainingData = readData('data/bank-note/train.csv')
    testData = readData('data/bank-note/test.csv')
    result = perceptronTrain(trainingData,100)
    weightVector = result[0]
    bias = result[1]
    print(weightVector)
    print(bias)
    totalRight = 0
    totalWrong = 0
    for td in testData:
        res = perceptronGuess(weightVector,bias,td)
        label = td[-1]
        passed = res == label
        if passed:
            totalRight += 1
        else:
            totalWrong += 1
    num1 = 0
    num0 = 0
    for td in testData:
        r = td[-1]
        if r == 1:
            num1+= 1
        else:
            num0 += 1
    print(f"For the test data of {len(testData)} elements the number of 1s is {num1} and the number of zeros is {num0}, ratio is {(num1/(num0+num1)) * 100} ")
        
    print(f"Error rate on the test data is {(totalWrong/(totalWrong+totalRight)) * 100}")
    print(f"Total perdectied right on the test data is {(totalRight/(totalWrong+totalRight)) * 100}")
perceptronTest()