import numpy as np
import networkx as nx
import random

PORT_NODE_THRESHOLD = 80000

class Graph():
	def __init__(self, nx_G, is_directed, p, q):
		self.G = nx_G
		self.is_directed = is_directed
		self.p = p
		self.q = q

	def node2vec_walk(self, walk_length, start_node):
		'''
		Simulate a random walk starting from start node.
		'''
		G = self.G

		walk = [start_node]

		while len(walk) < walk_length * 2 - 1:
			cur = walk[-1]
			out_edges = G.out_edges(cur, keys=True)
			random.shuffle(out_edges)
			if len(out_edges) > 0:
				walk += [out_edges[0][1], out_edges[0][2]]
			else:
				break

		return walk

	def simulate_walks(self, num_walks, walk_length):
		'''
		Repeatedly simulate random walks from each node.
		'''
		G = self.G
		walks = []
		nodes = [x for x in list(G.nodes()) if x < PORT_NODE_THRESHOLD]
		print 'Walk iteration:'
		for walk_iter in range(num_walks):
			print str(walk_iter+1), '/', str(num_walks)
			random.shuffle(nodes)
			for node in nodes:
				walks.append(self.node2vec_walk(walk_length=walk_length, start_node=node))

		return walks