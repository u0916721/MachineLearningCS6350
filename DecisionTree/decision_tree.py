# Basic decision tree, which really is just a bunch of ID3 methods to create a tree
# Probably could put this logic in main but for now might be simpler to extract, though idk
from node import node
class decision_tree:
    def __init__(self, root,depth):
        # set the rootNode, which should not be None, but rather a Node class with all the training data
        self.root = root
        self.depth = depth
    # We could make these generic and pass in a math function instead that calculates each of these but
    # optimize later, make changes if needed
    def createTreeInformationGain(self,depth,root: node):
        # Basecase
        if depth == 0 or root.hasOnlyOneLabel():
            return
        #Next tasks find the attribute with the best information gain and split on this attribute
        #Then remove the split attribute from the data set, this is an expensive call, but optimize later
        # Might need to make a copy of this data and then assign it to the node(because we could be pointing to one array), again pretty expensive. 
        # then repeat the call
        
        return None
    def createTreeMajorityError():
        return None
    def createTreeGiniIndex():
        return None
        
        