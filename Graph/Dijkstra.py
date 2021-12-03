#!/usr/bin/env python
# coding: utf-8

# ## 单源最短路径算法Dijkstra: 
# 
#     核心思想greedy：
#     将所有节点分为两类：
#     1. 已确定从起点到当前点的最短路径长度的节点， 2. 以及未确定从七点到当前节点的最短路筋长度：
#     分别记为：[已确定点]，[未确定点]
# 
#     S：{已确定点集合}
#     U：{未确定点集合}
#     算法步骤：
#         a. 初始，S只有源点，即S = {v}, v为原点且v的距离为0. U 包含除v以外的其他顶点， 
#     若v和U中顶点u有边，则<u,v> 正常有权值，若u不是v的出边邻接点，则<u,v>权值为无穷
# 
#         b. 从U 中选取一个距离v最小的顶点k，把k，加入S中（该选定的距离是v到k的最短路径距离）
#         c. 以k为新考虑的中间点，修改U中各顶点的距离，若从源点v到顶点u的距离（经过k）比原来
#     距离（不经过k） 短，则修改顶点u的距离值，修改后的距离值为距离顶点k的距离加上k的权值
# 
#         d. 重复步骤b和c直到所有顶点都包含在S中。 
# 

# ## Method 1: Enumeration method 

# In[21]:


# graph: the graph in the format of list. the element of the list is the distance between each vertex.
# shorted_distance: the list of shortest distance between vertex and initial point
# initial_point: the source of the graph 
class Dijkstra:
    def __init__(self, graph: list[list], size, initial_point: int):
        self.graph = graph
        self.n = size 
        self.initial = initial_point 
        
    def get_min_dis_point(self, shortest_distance, visited, size):
        index = -1 
        minn = float('inf')
        for i in range(size):
            if visited[i] == False and shortest_distance[i] < minn:
                minn = shortest_distance[i]
                index = i 
        return index 
    def Print(self, shortest_distance):
        for i in range(self.n):
            print("The shortest distance between vertex ", i, 
                  " and inital vertex ", self.initial, " is ", 
                  shortest_distance[i])
        
    def shortestpath(self):
        shortest_distance = [float('inf')] * self.n
        
        for i in range(self.n):
            #print(self.initial)
            #print(self.graph)
            if self.graph[self.initial][i] != -1:
                shortest_distance[i] = self.graph[self.initial][i]
                
        visited = [False] * self.n
        shortest_distance[self.initial] = 0 # set initial point distance be 0 (to itself)
        visited[self.initial] = True # set initial point be visited
        
        # we do not need to go through the initial point
        for i in range(self.n-1):
            index = self.get_min_dis_point(shortest_distance, visited,self.n)
            visited[index] = True 
            for j in range(self.n):
                if visited[j] == False and self.graph[index][j] != -1 and shortest_distance[index] != float('inf') and shortest_distance[index] + self.graph[index][j] < shortest_distance[j]:
                    # update the shortest_distance, if the path through the index vertex, we update the shortest_distance
                    shortest_distance[j] = shortest_distance[index] + self.graph[index][j]
                    
        self.Print(shortest_distance)
            
        


# In[20]:


graph = [[-1, 4, -1, -1, -1, -1, -1, 8, -1 ],
        [4, -1, 8, -1, -1, -1, -1, 11, -1 ],
        [-1, 8, -1, 7, -1, 4, -1, -1, 2],
        [-1, -1, 7, -1, 9, 14, -1, -1, -1 ],
        [-1, -1, -1, 9, -1, 10, -1, -1, -1],
        [-1, -1, 4, -1, 10, -1, 2, -1, -1],
        [-1, -1, -1, 14, -1, 2, -1, 1, 6],
        [8, 11, -1, -1, -1, -1, 1, -1, 7],
        [-1, -1, 2, -1, -1, -1, 6, 7, -1]]
dijkstra = Dijkstra(graph, len(graph), 6)
dijkstra.shortestpath()


# #### Time Complexibility: O(n^2)
# #### Space Complexibility: O(n^2)

# ## Method 2: Priority queue(heap)

# In[41]:


import heapq
class Dijkstra:
    def __init__(self, graph: list[list], size, initial_point: int):
        self.graph = graph
        self.n = size 
        self.initial = initial_point 
    def Print(self, shortest_distance):
        for i in range(self.n):
            print("The shortest distance between vertex ", i, 
                  " and inital vertex ", self.initial, " is ", 
                  shortest_distance[i])
    def shortestpath(self):
        shortest_distance = [float('inf')] * self.n
        
       
        prior_queue = [(0, self.initial)]
        shortest_distance[self.initial] = 0 
        visited = [False] * self.n 
        while prior_queue:
            shortest = heapq.heappop(prior_queue)
            distance = shortest[0]
            vertex = shortest[1]
            for i in range(0, self.n):
                if self.graph[vertex][i] != -1 :
                    dist = shortest_distance[vertex] + self.graph[vertex][i]
                    if dist < shortest_distance[i]:
                        shortest_distance[i] = dist 
                        heapq.heappush(prior_queue ,(dist, i))
                        
        self.Print(shortest_distance)
        


# In[42]:


graph = [[-1, 4, -1, -1, -1, -1, -1, 8, -1 ],
        [4, -1, 8, -1, -1, -1, -1, 11, -1 ],
        [-1, 8, -1, 7, -1, 4, -1, -1, 2],
        [-1, -1, 7, -1, 9, 14, -1, -1, -1 ],
        [-1, -1, -1, 9, -1, 10, -1, -1, -1],
        [-1, -1, 4, -1, 10, -1, 2, -1, -1],
        [-1, -1, -1, 14, -1, 2, -1, 1, 6],
        [8, 11, -1, -1, -1, -1, 1, -1, 7],
        [-1, -1, 2, -1, -1, -1, 6, 7, -1]]
dijkstra = Dijkstra(graph, len(graph), 6)
dijkstra.shortestpath()


# #### Time Complexibility: O(m*logm)      m: length(graph)
# #### Space Complexibility: O(n^2)

# In[ ]:




