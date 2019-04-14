class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insertNode(self,data):
        if self.data:
            if data<self.data:
                if self.left==None:
                    self.left=Node(data)
                else:
                    self.left.insertNode(data)
            elif data>self.data:
                if self.right==None:
                    self.right=Node(data)
                else:
                    self.right.insertNode(data)
        else:
            self.data=data
    def printTree(self):
        print(self.data)    
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()
    def minValue(node):
        current = node 
        while(current.left is not None): 
            current = current.left 
        return current.data
    def maxValue(node):
        current1 = node 
        while(current1.right is not None): 
            current1 = current1.right 
        return current1.data









   
         
       


