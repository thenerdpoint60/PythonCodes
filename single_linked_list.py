class Node:
    def __init__(self):
        self.data=None
        self.next=None
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next=next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None
    def insertAtTheBegining(self,data):
        newNode=Node()
        newNode.setData(data)
        if self.lenght==0:
            self.head=newNode
        else:
            newNode.setNode(self.head)
            self.head=newNode
        self.length+=1

    def insertAtEnd(self.data):
        newNode=Node()
        newNode.setData(data)
        current=self.head
        while current.getNext()!=None:
            current=current.getNext()
        current.setNext(newNode)
        self.lenght+=1


    













        
        
