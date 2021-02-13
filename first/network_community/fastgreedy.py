#!/usr/bin/python3
# coding: utf-8

# import required models
import igraph
from igraph import plot
import pandas as pd

# read influence_data data set
data = pd.read_csv('../data/influence_data.csv')

# generate the edges of graph as a list of tuples, and each tuple reprsent an edge
edges = []
for i in list(map(tuple, data[['inf_id', 'flw_id']].values)):
    tp = (i[0], i[1])
    if tp in edges or tp[::-1] in edges:
        continue
    else:
        edges.append(tp)

# create object Graph by edges
g = igraph.Graph(edges)
# community fastgreedy algorithm
g_ifmp = g.community_fastgreedy()
print(g_ifmp.optimal_count)
g2 = g_ifmp.as_clustering(n=16)


# beautify figure style and store image
visual_style = {}
visual_style["vertex_size"] = 10
visual_style["layout"] = g.layout("drl")
visual_style["margin"] = 80
out = plot(g2, **visual_style)
out.save('res.eps')

# acquire parameter
print(g2.q)
f = open('membership1.csv', 'a+')
mbs = g2.membership
for i in range(len(mbs)):
    print(i)
    f.write("%d,%d\n" % (i, mbs[i]))
f.close()