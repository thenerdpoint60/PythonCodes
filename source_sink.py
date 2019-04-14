from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        a=self.graph[u]
        print("The garph is %d and added %d:"%(a,v))
    def printPaths(self,u,d,visited,path):
        visited[u]=True
        path.append(u)
        if u==d:
            print (path)
        else:
            for i in self.graph[u]:
                if visited[i]==False:
                    self.printPaths(i,d,visited,path)
        path.pop()
        visited[u]=False

    def findPaths(self,s,d):
        visited=[False]*(self.vertices)
        path=[]
        self.printPaths(s,d,visited,path)
