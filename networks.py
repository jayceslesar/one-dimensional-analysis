import networkx as nx
import numpy as np
import random
from collections import OrderedDict

def make_graph(prob, num_nodes):
  G = nx.DiGraph()
  p = prob
  for node in range(num_nodes):
    G.add_node(node)
    for neighbor in range(G.number_of_nodes()-1):
      if random.uniform(0, 1) < p: #create an edge
        G.add_edge(node,neighbor)
      if random.uniform(0, 1) < p: #create an edge
        G.add_edge(neighbor,node)

  from itertools import count
  groups = set(nx.get_node_attributes(G,'state').values())
  mapping = dict(zip(sorted(groups),count()))  
  return G

def draw(graph):
  nx.draw(graph, with_labels=True, node_size=200, pos=nx.fruchterman_reingold_layout(graph))

def metrics(graph):
  degree_centrality = nx.degree_centrality(graph)
  in_degree_centrality = nx.in_degree_centrality(graph)
  out_degree_centrality = nx.out_degree_centrality(graph)

  # degDictG = {n: d for n, d in graph.degree()}
  # orderedDegs = OrderedDict(sorted(degDictG.items(), key=lambda x: x[1], reverse=True))
  # print('Degree: \n', orderedDegs)

  # print('')

  # # Explain betweenness on board
  # betDict = nx.betweenness_centrality(graph, normalized=False)
  # orderedBets = OrderedDict(sorted(betDict.items(), key=lambda x: x[1], reverse=True))
  # print("Betweenness:\n", orderedBets)

  print(degree_centrality, in_degree_centrality, out_degree_centrality)

def erdos_renyi(num_nodes, p, directed):
  F = nx.fast_gnp_random_graph(num_nodes, p, directed=directed)
  return F

def rw(graph, walk_length, starting_node):
  A = nx.adjacency_matrix(graph)
  A = A.todense()
  A = np.array(A, dtype = np.float64)

  # degree matrix
  D = np.diag(np.sum(A, axis=0))

  # transition matrix T
  #T = np.dot(np.linalg.inv(D), A)
  T = A / A.sum(axis=1, keepdims=True)

  # random walk length
  walkLength = walk_length

  # defining starting node
  p = np.zeros((graph.number_of_nodes(), 1)).reshape(-1,1)
  p[starting_node] = 1

  visited = list()
  for k in range(walkLength):
      # evaluate the next state vector
      p = np.dot(T,p)
      # choose the node with higher probability as the visited node
      visited.append(np.argmax(p))
  return visited

def sub_graph(graph, visited):
  H = nx.subgraph(graph, visited)
  return H
