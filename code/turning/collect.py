import random
import networkx as nx

import turn

for i in range(0,5):
	graphs=turn.all_directed_graphs(i)
	for g in graphs:
		print('{0},{1},"{2}"'.format(i, len(turn.turn_all(g)), g.edges))

turn.collect_all_5()

lim=16
samples=65536

for i in range(6,lim):
	for j in range(0,samples):
		g=nx.generators.random_graphs.gnp_random_graph(i, 0.5, directed=True)
		for n in g.nodes:
			g.add_node(n, ind=n)
			if random.random()>=0.5:
				g.add_edge(n,n)
		print('{0},{1},"{2}"'.format(i, len(turn.turn_all(g)), g.edges))
