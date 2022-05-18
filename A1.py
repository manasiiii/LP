from collections import defaultdict
import queue

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,s):
        visited=[False]*(max(self.graph)+1)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

    def dfsutil(self, v,visited):
        visited.add(v)
        print(v,end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfsutil(neighbour,visited)
    
    def dfs(self,v):
        visited=set()
        self.dfsutil(v, visited)


g=Graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)

print("Using DFS ")
g.dfs(0)
print("\n")
print("Using BFS\n")
g.bfs(0)
print("\n")