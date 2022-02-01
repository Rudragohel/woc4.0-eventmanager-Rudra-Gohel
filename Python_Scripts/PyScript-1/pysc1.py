#this code is implementation of Kruskal's Minimum Spanning Tree Algorithm using python libraries

import networkx as nx
import matplotlib.pyplot as plt
import os


class Graph:

	def __init__(self, vertices):
		self.V = vertices 
		self.graph = [] 
		# to store graph

	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# A utility function to find set of an element i
	# (uses path compression technique)
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	# A function that does union of two sets of x and y
	# (uses union by rank)
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		# Attach smaller rank tree under root of
		# high rank tree (Union by Rank)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		# If ranks are same, then make one as root
		# and increment its rank by one
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's
		# algorithm
	def KruskalMST(self):

		self.result = [] # This will store the resultant MST
		
		# An index variable, used for sorted edges
		i = 0
		
		# An index variable, used for result[]
		e = 0

		# Step 1: Sort all the edges in
		# non-decreasing order of their
		# weight. If we are not allowed to change the
		# given graph, we can create a copy of graph
		self.graph = sorted(self.graph,
							key=lambda item: item[2])

		parent = []
		rank = []

		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is equal to V-1
		while e < self.V - 1:

			# Step 2: Pick the smallest edge and increment
			# the index for next iteration
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			# If including this edge does't
			# cause cycle, include it in result
			# and increment the indexof result
			# for next edge
			if x != y:
				e = e + 1
				self.result.append([u, v, w])
				self.union(parent, rank, x, y)
			# Else discard the edge
        
    
	def get_result(self):
		return self.result

#Above code of Kruskal algorithm is taken from https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/


num_of_nodes = int(input("Enter number of nodes: "))

G = Graph(num_of_nodes)
Graph_for_plot = nx.Graph()
Graph_after_plot = nx.Graph()


node_names = []

node_edges=[]

for i in range(num_of_nodes):
    name=str(input("Enter name of node " +  str(i+1)+ " (max 2 characters):"))
    node_names.append(name)
    Graph_for_plot.add_node(name)
    Graph_after_plot.add_node(name)
    
num_of_edges = int(input("Enter number of edges: "))

for i in range(num_of_edges):
    print("Enter names of edges connected by nodes:")
    while True:
        name1=str(input("Name of 1st Node:"))
        if name1 in node_names:
            break
        else:
            print("Invalid name. No such node exists. Enter again.")
    while True:
       name2=str(input("Name of 2nd Node:"))
       if name2 in node_names:
           break
       else:
           print("Invalid name. No such location exists. Enter again.")
    cost=int(input("Enter edge weight: "))
    G.addEdge(node_names.index(name1),node_names.index(name2),cost)
    node_edges.append([name1,name2,cost])
    Graph_for_plot.add_edge(name1, name2, weight=cost)

plt.figure(1,figsize=(7,7)) 
   
nx.draw_kamada_kawai(Graph_for_plot,node_color="blue",with_labels = True,node_size=2000, font_size=18,font_color="yellow")
pos=nx.kamada_kawai_layout(Graph_for_plot)
edge_labels=dict([((u,v,),d['weight'])
for u,v,d in Graph_for_plot.edges(data=True)])
nx.draw_networkx_edge_labels(Graph_for_plot,pos,edge_labels=edge_labels)

plt.savefig("map.png")

# Function call
G.KruskalMST()
node_edges = G.get_result()

total_cost=0

for i in range(len(node_edges)):
    total_cost = total_cost + node_edges[i][2]
    Graph_after_plot.add_edge(node_names[node_edges[i][0]],node_names[node_edges[i][1]],weight=node_edges[i][2])

print("Total weight: ",total_cost)

plt.figure(2,figsize=(7,7)) 
   
nx.draw(Graph_after_plot,pos=pos,node_color="blue",with_labels = True,node_size=2000, font_size=18,font_color="yellow")
edge_labels=dict([((u,v,),d['weight'])
for u,v,d in Graph_after_plot.edges(data=True)])
nx.draw_networkx_edge_labels(Graph_after_plot,pos,edge_labels=edge_labels)

plt.savefig("map_after.png")

os.startfile("map.png")
os.startfile("map_after.png")