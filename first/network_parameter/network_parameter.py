#!/usr/bin/python3
# coding: utf-8

import pandas as pd
import numpy as np

# read influence_data data set
data = pd.read_csv('../data/influence_data.csv')

# generate adjacency matrix
n = max(max(data['inf_id'].values) + 1, max(data['flw_id'].values) + 1)
A = np.zeros((n, n))
for i in range(len(data)):
    A[data['flw_id'][i], data['inf_id'][i]] = 1

# ## clustering coefficient
# calculate the clustering coeffiient and store in list clst
clst = []
for i in range(len(A)):
    k = sum(A[i, :]) + sum(A[:, i])
    print(k)
    e = 0
    neighbor = []
    for j in range(len(A)):
        if A[i, j] == 1 or A[j, i] == 1:
            neighbor.append(j)
    # get non-reapting nodes using set
    neighbor = set(neighbor)
    for j in neighbor:
        for l in neighbor:
            e += A[j, l] + A[l, j]
    if k != 0 and k != 1:
        clst.append(2 / k / (k - 1) * e)
    else:
        clst.append(0)

# write out clustering coefficient
f = open('clst1.csv', 'a+')
for i in range(len(clst)):
    f.write("%d,%f\n" % (i, clst[i]))
f.close()

# ## characteristic path length
# store each infulencer 's followers in dict infulencers
infulencers = {}
for i in range(len(A)):
    infulencers[i] = np.where(A[:, i])


# using dfs algorithm to find leaf node
# reached_nodes数组避免形成环路
def dfs(node, ttl):
    global reached_nodes
    reached_nodes.append(node)
    if ttl == 0:
        return 0
    sum = 0
    if len(infulencers[node][0]) == 0:
        return 0
    for i in infulencers[node][0]:
        if i in reached_nodes:
            continue
        sum += dfs(i, ttl - 1) + 1
    return sum


length_sum = {}
for i in range(len(A)):
    reached_nodes = []
    length_sum[i] = dfs(i, 100)
    print(i)

# calculate characteristic path length
length_res = {}
for i in length_sum.keys():
    k = sum(A[:, i])
    if k == 0:
        length_res[i] = 0
    else:
        length_res[i] = length_sum[i] / k

# write out
f = open('length1.csv', 'a+')
for i in length_sum.keys():
    f.write("%d,%f\n" % (i, length_sum[i]))
f.close

# ## katz centrality
# calculate eigenvalues
lmds, _ = np.linalg.eig(A)
lmd = np.max(lmds)
print(lmd)
# get the maxium eigenvalues and estimate  decay factor a, a is 1/4
a = 1 / 4
Ik = np.zeros(A.shape)
pre_A = np.identity(len(A))
for i in range(100):
    pre_A = a * pre_A.dot(A)
    Ik += pre_A

# write out
f1 = open('influcing_katz1.csv', 'a+')
f2 = open('influced_katz1.csv', 'a+')
for i in range(len(A)):
    f1.write("%d, %f\n" % (i, sum(Ik[:, i])))
    f2.write("%d, %f\n" % (i, sum(Ik[i, :])))
f1.close()
f2.close()

