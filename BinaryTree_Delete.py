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

    def delete(self,data):
        if(self is None):
            return None
        if(data<self.d):
            self.l=self.l.delete(data)
        elif(data>self.d):
            self.r=self.r.delete(data)
        else:
            if(self.l is None):
                temp=self.r
                self=None
                return temp
            elif(self.r is None):
                temp=self.l
                self=None
                return temp
        temp=self.minValueNode(self.r)
        self.d=temp.d
        self.r=self.r.delete(temp.d)
        return self
    def minValueNode(slef,node):
        current=node
        while(current.l is not None):
            current=current.l
        return current













                
