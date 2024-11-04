#This is the code that contains perceptron code.
#This assumes d is a numpy data frame
import numpy as np

def perceptronTrain(D,Maxiter):
    #Init weight vector to be the size of the data
    weightVector = np.zeros(len(D.shape[0])-1,dtype = float) # more here, based on size of d
    bias = 0
    for i in range(0,Maxiter):
        #Should shuffle the array on each pass
        np.random.shuffle(D)
        for d in D:
            y = None # This is the true label of the sample d
            a = activationPerceptron(weightVector,d,bias)
            #ya should always be positive if is correct this is the online error driven aspect of perceptron
            ya = y * a
            #Did we make an error
            if ya <= 0:
                #Then we update the weight vector and bias
                weightVector = weightVector + y*d
                b = b + y
    #Here we return a tuple with the weight vector and its bias     
    return (weightVector,bias)
#returns the activations for this sample
def activationPerceptron(weightVector,sample,bias):
    return None
# Returns the label, given a testSample
def perceptronTest(weightVector,bias,testSample):
    a = activationPerceptron(weightVector,testSample,bias)
    if a >= 0:
        return 1
    else:
        return 0