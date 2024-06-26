import numpy as np
import networkx as nx
import itertools as it

def positive_edges(prefs):
	edges=[]
	for e in it.combinations(prefs.keys(), 2):
		if np.all(np.isnan(prefs[e[0]]-prefs[e[1]])):
			weight=np.nan
		else:
			weight=np.nanmean(prefs[e[0]]-prefs[e[1]])

		n=np.sum(~np.isnan(prefs[e[0]]-prefs[e[1]]))
		if np.isnan(weight):
			continue
		elif weight>=0:
			edges.append((e[0], e[1], {'weight': weight, 'n': n}))
		else:
			edges.append((e[1], e[0], {'weight': -weight, 'n': n}))
	return edges

def prefgraph(prefs):
	g=nx.DiGraph()
	g.add_nodes_from(list(prefs.keys()))
	edges=positive_edges(prefs)
	g.add_edges_from(edges)

	return g

def decompose(g):
	f=np.array([g[e[0]][e[1]]['weight'] for e in g.edges])
	W=np.diag([g[e[0]][e[1]]['n'] for e in g.edges])

	idx=dict()
	nodes=list(g.nodes)
	for i in range(0, len(nodes)):
		idx[nodes[i]]=i

	origins=np.zeros((len(g.edges), len(g.nodes)))
	c=0
	for e in g.edges:
		sign=np.sign(g[e[0]][e[1]]['weight'])
		if np.isnan(sign):
			sign=0
		origins[c][idx[e[0]]]=sign*-1
		origins[c][idx[e[1]]]=sign
		c=c+1

	try:
		s=-np.linalg.pinv(origins.T@W@origins)@origins.T@W@f
	except LinAlgError:
		s=np.zeros(len(list(g.nodes)))

	values=dict()

	for option in idx.keys():
		values[option]=s[idx[option]]

	return values

def hodgerank(prefs):
	g=prefgraph(prefs)
	return decompose(g)
