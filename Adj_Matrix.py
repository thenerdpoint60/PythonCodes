class graph_adj(object):
    def __init__(self,present_vertices):
        self.adjMatrix=[]
        #self.adjMatrix=[[0]*present_vertices for _ in range(present_vertices)]
        for i in range(present_vertices):
            self.adjMatrix.append([0 for i in range(present_vertices)])
        self.vertices=present_vertices
    def addEdge(self,v1,v2):
        #if v1 in self.vertices and v2 in self.vertices:
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def printTheMatrix(self):
        #for i in len(self.adjMatrix):
            #print(i)
        print(self.adjMatrix)

    def removeEdge(self,v1,v2):
        if(self.adjMatrix[v1][v2]==0):
            print("No edge between %d and %d"%(v1,v2))
            return
        self.adjMatrix[v1}[v2]=0
        self.adjMatrix[v2][v1]=0
        
