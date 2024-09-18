# Basic math helping class, takes in pure numerical values and returns values, no data is parsed here
# Majority Error 
# Gini Index
# Entropy 
# Information Gain
import math

#Calculates the entropy
def calcEntropy(val):
    if val == 0:
        return 0
    return -1 * val * math.log2(val)

#Calculates Gini Index
def calcGiniIndex(val):
    return val * val

#Calculates majorityError
def calcMajorityError(ratios):
    return 1 - max(ratios)


#Calculates InformationGain
def calcInformationGain():
    return 69