#Author thenerdpoint60
#15/7
def dfs(graph, node, visited):#Function Call
    if node not in visited:#checking if the node is shown for the first time or is repeated
        visited.append(node)  #If once used then it will notbe repeated again
        for n in graph[node]:#Recursive call of the code
            dfs(graph,n, visited)
    return visited #output


graph = {
    'B' : ['B','S'],
    'S' : ['A'],
    'C' : ['D','E','F','S'],
    'E' : ['C'],
    'D' : ['C','H'],
    'F' : ['C','G'],
    'G' :  ['E','G'],
    'H' :['F','S'],
    'A' : ['A','C','G']
}

dfs(graph,'A',[])
