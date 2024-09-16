# Basic decision tree, which really is just a bunch of ID3 methods to create a tree
# Probably could put this logic in main but for now might be simpler to extract, though idk
class decision_tree:
    def __init__(self, root):
        # set the rootNode, which should not be None, but rather a Node class with all the training data
        self.root = root
    # We could make these generic and pass in a math function instead that calculates each of these but
    # optimize later, make changes if needed
    def createTreeInformationGain():
        return None
    def createTreeMajorityError():
        return None
    def createTreeGiniIndex():
        return None
        
        