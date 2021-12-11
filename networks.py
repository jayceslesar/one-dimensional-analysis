import networkx as nx
from networkx.algorithms.centrality import eigenvector
import numpy as np
import random
from collections import OrderedDict
import matplotlib.pyplot as plt
import plotly.graph_objects as px
import plotly.graph_objs as go
import itertools


def make_graph(prob, num_nodes):
  G = nx.DiGraph()
  p = prob
  for node in range(num_nodes):
    G.add_node(node)
    for neighbor in range(G.number_of_nodes()-1):
      if random.uniform(0, 1) < p: #create an edge
        if np.random.binomial(1,0.5) == 0:
          G.add_edge(*(node,neighbor))
        else:
          G.add_edge(*(neighbor, node))
  return G


def draw(graph):
  nx.draw(graph, with_labels=True, node_size=200, pos=nx.fruchterman_reingold_layout(graph))


def metrics(graph):
  degree_centrality = nx.degree_centrality(graph)
  in_degree_centrality = nx.in_degree_centrality(graph)
  out_degree_centrality = nx.out_degree_centrality(graph)

  closeness_centrality = nx.closeness_centrality(graph)
  between_centrality = nx.betweenness_centrality(graph)
  eigenvector_centrality = nx.eigenvector_centrality(graph)

  print(dict_mean(eigenvector_centrality))
  return degree_centrality, in_degree_centrality, out_degree_centrality, closeness_centrality, between_centrality, eigenvector_centrality


def erdos_renyi(num_nodes, p, directed: bool):
  return nx.fast_gnp_random_graph(num_nodes, p, directed=directed)

def watts_strogatz(num_nodes, k, prob):
   G = nx.watts_strogatz_graph(num_nodes, k, prob)
   return G.to_directed()

def rw(graph, walk_length, starting_node):
  # getting the adjecency matrix
  A = nx.adjacency_matrix(graph)
  A = A.todense()
  A = np.array(A, dtype = np.float64)

  # degree matrix
  D = np.diag(np.sum(A, axis=0))

  # transition matrix T
  T = A / A.sum(axis=1, keepdims=True)

  # random walk length
  walkLength = walk_length

  # defining starting node
  p = np.zeros((graph.number_of_nodes(), 1)).reshape(-1,1)
  p[starting_node] = 1

  visited = list()
  for k in range(walkLength):
      p = np.dot(T,p)
      visited.append(np.argmax(p))
  return visited


def sub_graph(graph, visited):
  H = nx.subgraph(graph, visited)
  return H


def dict_mean(dicts):
  return sum(dicts.values()) / len(dicts)


def comparison_graph(G, H, num_walkers):
  Gdc, Gidc, Godc, Gcc, Gbc, Gevc  = metrics(G)
  Hdc, Hidc, Hodc, Hcc, Hbc, Hevc = metrics(H)

  # creating random data through randomint
  # function of numpy.random
  np.random.seed(42)

  x = ['Degree Centrality', 'In-Degree Centrality', 'Out-degree Centrality', 'Closeness Centrality', 'Betweenness Centrality', 'Eigenvector Centrality']

  plot = px.Figure(data=[go.Bar(
      name = 'Entire Graph',
      x = x,
      y = [dict_mean(Gdc), dict_mean(Gidc), dict_mean(Godc), dict_mean(Gcc), dict_mean(Gbc), dict_mean(Gevc)],
      text = [round(dict_mean(Gdc), 3), round(dict_mean(Gidc), 3), round(dict_mean(Godc), 3),
             round(dict_mean(Gcc), 3), round(dict_mean(Gbc), 3), round(dict_mean(Gevc), 3)],
      textposition='auto'
    ),
                        go.Bar(
      name = 'Sub-Graph',
      x = x,
      y = [dict_mean(Hdc), dict_mean(Hidc), dict_mean(Hodc), dict_mean(Hcc), dict_mean(Hbc), dict_mean(Hevc)],
      text = [round(dict_mean(Hdc), 3), round(dict_mean(Hidc), 3), round(dict_mean(Hodc), 3),
             round(dict_mean(Hcc), 3), round(dict_mean(Hbc), 3), round(dict_mean(Hevc), 3)],
      textposition='auto'
    )
  ])
  
  plot.update_layout(title=f'Metric Comparison of Graph with {G.number_of_nodes()} nodes vs. Sub-Graph with {H.number_of_nodes()} nodes with {num_walkers} walkers', font_size=20)
  plot.show()

def run_multiple_runners(graph, num_times, walk_length):
  l = {}
  for _ in range(num_times):
    rand_node = random.randrange(0, graph.number_of_nodes())
    visited = rw(graph, walk_length, rand_node)
    l[rand_node] = visited
  return set(itertools.chain(*list(l.values())))
