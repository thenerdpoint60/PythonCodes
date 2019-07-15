#Author thenerdpoint60
#15/7
graph={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':['B'],'E':['B'],'F':['C'],'G':['C']}

def bfs(graph,start,goal):
    openlist=[start]
    closelist=[]
    #creates a list of node in the graph
    while openlist:
        node=openlist.pop(0)
        if node not in closelist:
            closelist.append(node)
            currentnode=graph[node]
            for nextnode in currentnode:
                openlist.append(nextnode)
            if goal==node:
                break
    #return closelist
    #checks if the goalis present in the graph
    for i in closelist:
        if(goal == i):
            present=True
        else:
            present=False
    if(present):
        print(closelist)
    else:
        print("Goal Doesn't exists")
bfs(graph,'A','B')

