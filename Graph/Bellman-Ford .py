#!/usr/bin/env python
# coding: utf-8

# ### 动态规划实现，适用于当有负权值边， 或者限制经过边数的数量。
# 
#     伪代码：
#         procedure BellmanFord(list vertices, list edges, vertex source)
#            // 讀入邊和節點的列表並對distance和predecessor寫入最短路徑
# 
#            // 初始化圖
#            for each vertex v in vertices:
#                if v is source then distance[v] := 0
#                else distance[v] := infinity
#                predecessor[v] := null
# 
#            // 對每一條邊重複操作
#            for i from 1 to size(vertices)-1: (当有限制条件：只能最多经过k条边时，遍历次数为 for i from 1 to k)
#                for each edge (u, v) with weight w in edges:
#                    if distance[u] + w < distance[v]: //遍历路径数组 k 遍，k为限制边数的限制条件，这里可以全部遍历的意义就是数组中存储所有的路径信息，
#         每次遍历只会对应到指定的起始点终止点，一遍遍历完成后，就相当于得到多经过一个点的最短路径长度。
#                        distance[v] := distance[u] + w
#                        predecessor[v] := u
# 
#            // 檢查是否有負權重的回路
#            for each edge (u, v) with weight w in edges:
#                if distance[u] + w < distance[v]:
#                    error "圖包含負權重的回路"

# #### DP method 

# In[32]:


class Bellman_Ford:
    def __init__(self, graph, n, src, k):
        self.graph = graph
        self.n = n 
        self.src = src 
        self.k = k 
    def Print(self, dp):
        for i in range(len(dp)):
            print("from ", self.src, " to ", i ," passes at most ", self.k, " node, the minimun distance is: ", min(dp[i]))
    def shortest_dist(self):
        dp = [[float('inf') for i in range(self.k+1)] for j in range(self.n)]
        
        dp[self.src][0] = 0 
        for i in range(1, self.k+1):
            for fr in range(self.n):
                for to in range(self.n):
                    if graph[fr][to]!= -1:
                        dp[to][i] = min(dp[fr][i-1]+graph[fr][to], dp[to][i])
        self.Print(dp)
            


# In[33]:


graph = [[-1, 4, -1, -1, -1, -1, -1, 8, -1 ],
        [4, -1, 8, -1, -1, -1, -1, 11, -1 ],
        [-1, 8, -1, 7, -1, 4, -1, -1, 2],
        [-1, -1, 7, -1, 9, 14, -1, -1, -1 ],
        [-1, -1, -1, 9, -1, 10, -1, -1, -1],
        [-1, -1, 4, -1, 10, -1, 2, -1, -1],
        [-1, -1, -1, 14, -1, 2, -1, 1, 6],
        [8, 11, -1, -1, -1, -1, 1, -1, 7],
        [-1, -1, 2, -1, -1, -1, 6, 7, -1]]
Bellman = Bellman_Ford(graph,len(graph),6,8)
Bellman.shortest_dist()


# In[ ]:




