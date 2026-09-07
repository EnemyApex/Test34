import networkx as nx
import numpy as np
import plotly.graph_objects as go
import pandas as pd

def generate_graph(graph_type, n_nodes=10):
    if graph_type == "Aléatoire":
        G = nx.erdos_renyi_graph(n_nodes, 0.3, directed=True, seed=42)
    elif graph_type == "Echelle-libre":
        G = nx.scale_free_graph(n_nodes, seed=42).to_directed()
    elif graph_type == "Petit Monde":
        G = nx.watts_strogatz_graph(n_nodes, 4, 0.3, seed=42).to_directed()
    else: # "Cycle"
        G = nx.cycle_graph(n_nodes, create_using=nx.DiGraph)
    return G

def get_adjacency_matrix(G):
    return nx.to_numpy_array(G)

def plot_graph_plotly(G, scores):
    pos = nx.spring_layout(G, seed=42)
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    node_x = [pos[node][0] for node in G.nodes()]
    node_y = [pos[node][1] for node in G.nodes()]
    node_size = [s * 3000 + 20 for s in scores]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=1, color='#888'), hoverinfo='none'))
    fig.add_trace(go.Scatter(x=node_x, y=node_y, mode='markers+text',
                             marker=dict(size=node_size, color=scores, colorscale='Viridis', showscale=True),
                             text=[f"{i}<br>Score: {s:.4f}" for i,s in enumerate(scores)], textposition="top center"))
    fig.update_layout(title="Visualisation du Graphe", showlegend=False, margin=dict(l=20, r=20), height=500)
    return fig
