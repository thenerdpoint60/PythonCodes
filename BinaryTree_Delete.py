#BinaryTree
class nodes:
    def __init__(self,data):#creatin a nodes
        self.l=None
        self.r=None
        self.d=data
    def addLeafs(self,data):#adding leafs
        if(self.d):#checking if there's a root node
            if(data<self.d):#checks if the leaf value is smaller than the root
                if(self.l==None):#if there's no left leaf
                    self.l=nodes(data)
                else:
                    self.l.insert(data)
            elif(data>self.d):
                if(self.r is None):
                    self.r=nodes(data)
                else:
                    self.r.insert(data)
        else:
            self.d=data
    def printTheTree(self):
        if(self.l):
            self.l.printTheTree()
        print(self.d)
        if(self.r):
            self.r.printTheTree()
