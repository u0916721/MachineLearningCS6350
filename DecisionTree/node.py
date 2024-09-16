# This is a node class for our tree
# Keeping it simple for now, but may need to add additional complexity, such as if its a leaf
class node:
    def __init__(self, splitAttribute, splitValue,trainingDataSet):
        #The attribute that we split on such as "Outlook"
        self.splitAttribute =  splitAttribute    
        # The value of the attribute that we split on, example "Rainy"
        self.splitValue = splitValue  
        # All of the children, or further splits
        self.children = None  
        self.trainingDataSet = trainingDataSet
        # The label of the trainingDataSet, iff we reach a depth limit
        # example [+,-,+,+] -> because + is the majorirty that is our label. 
        # This is only calculated if the node is a root
        self.label = None
    def calcLabel(self):
        #Gets and sets the majority label
        #Naive dictionary implementation
        d = {}
        for sample in self.trainingDataSet:
            labelValue = sample[len(sample)-1]
            if labelValue in d:
                d[labelValue] = d[labelValue] + 1
            else:
                d[labelValue] = 1
        # itterate over keys
        # find the biggest value
        bestLabelVal = " "
        bestValue = float('-inf')
        for k in d:
            if d[k] > bestValue:
                bestLabelVal = k
                bestValue = d[k]
        self.label = bestLabelVal
            
            
            
    
