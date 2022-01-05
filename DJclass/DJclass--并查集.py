#!/usr/bin/env python
# coding: utf-8

# ### 并查集
# 根据相关题目要求，将属于同一类的集合合并，最终可以得到有多少个不一样的连通分量，连通分量即一个图
# 
# 并查集一般定义两个函数，一个变量--father 数组。 
# father 数组用于记录每个元素的父亲节点，即每个集合的代表元素。 
# 
# 两个函数：
# 
#     Union: 用于将两个属于同类的集合融合，融合的意义就是将两个集合的代表元素指向同一个，
#     即， 假设x,y,z 属于集合A， z为代表元素（father[x] = z, father[y] = z, father[z]=z), a, b,c 属于集合B， c 为代表元素（father[a]=c,father[b]=c,father[c]=c）如果要融合A,B 则将任意一个集合的代表元素设置为两个集合代表元素，eg: father[z] = c则，A 集合变为father[x] = z, father[y] = z, father[z]=c,当我们查询x元素的代表元素时，我们找到z， z还有代表元素，是c，那么x的代表元素就是c。这样我们就完成了两个集合的融合。 
# 
#     Find ： 该函数用于寻找目标元素的代表元素。 我们采用递归的方式实现。不断地寻找该元素的上一级子代表元素
#     比如father[x] = y, father[y]=z,father[z]=c, father[c]=c 递归直到father[i]=i（元素的代表元素是它本身）停止。 同时我们为了union和以后的find时更加高效，我们每次递归，都更新目标元素的代表元素。
#     比如， 当前father[x]=y, father[y]=z ，father[z]=c, father[c]=c 递归结束后我们将father[x] =c （c为返回元素）这样可以有效降低时间复杂度。 

# ### python

# In[2]:


class DJclass:
    def __init__(self,size):
        self.father = [i for i in range(size)]
        
    def find(self, idx):
        if self.father[idx] == idx:
            return idx 
        else:
            self.father[idx] = self.find(self.father[idx])
            return self.father[idx]
        
    def union(self,i,j):
        self.father[self.find(i)] = self.find(j)
        


# In[ ]:




