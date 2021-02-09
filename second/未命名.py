#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[22]:


# data = pd.read_csv('../data/influence_data.csv')
# data
#
#
# # In[6]:
#
#
# n = max(max(data['inf_id'].values)+1,max(data['flw_id'].values)+1)
# A = np.zeros((n,n))
# for i in range(len(data)):
#     A[data['inf_id'][i],data['flw_id'][i]]=1
# A
#
#
# # ## 聚合系数
#
# # In[23]:
#
#
# clst=[]
# for i in range(len(A)):
#     k = sum(A[i,:]) + sum(A[:,i])
#     print(k)
#     e = 0
#     neighbor = []
#     for j in range(len(A)):
#         if A[i,j]==1 or A[j,i]==1:
#             neighbor.append(j)
#     neighbor=set(neighbor)
#     for j in neighbor:
#         for l in neighbor:
#             e += A[j,l]+A[l,j]
#     if k != 0 and k!=1:
#         clst.append(2/k/(k-1)*e)
#     else:
#         clst.append(0)
#
#
# # In[25]:
#
#
# sorted(clst,reverse=True)
#
#
# # In[26]:
#
#
# import matplotlib.pyplot as plt
# plt.hist(clst)
#
#
# # In[28]:
#
#
# sum(np.array(clst)==2)
#
#
# # In[29]:
#
#
# np.mean(clst)


# In[ ]:


# ## 特征路径

# In[2]:


A = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])
A = A.T
inf = 999999
AA = (np.ones(A.shape) - A - np.identity(len(A))) * inf + 1
AA = AA - np.identity(len(A))
print(AA)

# In[3]:


# dij 算法
for i in range(len(A)):
    st = [i]
    lastlen = -1
    nodes = {}
    for j in range(i, len(A)):
        nodes[j] = [i, False]
    while len(st) != lastlen:
        lastlen = len(st)
        for j in range(i + 1, len(A)):
            for k in st:
                if AA[j, k] + AA[k, i] < AA[j, i]:
                    AA[j, i] = AA[j, k] + AA[k, i]
                    nodes[j][0] = k
        # print(A)
        remain = list(set(range(i, len(A))).difference(set(st)))
        # print(remain)
        # print(min(AA[remain, i]))
        if len(remain) > 0 and min(AA[remain, i]) < inf:
            # x = list(AA[:, i]).index(min(AA[remain, i]))
            for x in remain:
                if AA[x, i] == min(AA[remain, i]):
                    break
            st.append(x)
            nodes[nodes[x][0]][1] = False
            nodes[x][1] = True
            print(st)
    ll = 0
    for j in nodes.keys():
        if nodes[j][1]:
            ll += AA[j, i]
    print(ll)
# In[4]:


# In[ ]:
