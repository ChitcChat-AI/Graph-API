import networkx as nx
from constants import NodeAttributes


def get_degrees(graph):
    try:
        return nx.degree(graph)
    except Exception:
        return None


def get_eccentricity(graph):
    try:
        return nx.eccentricity(graph)
    except Exception:
        return None


def get_betweenness_centrality(graph):
    try:
        return nx.betweenness_centrality(graph)
    except Exception:
        return None


def get_closeness_centrality(graph):
    try:
        return nx.closeness_centrality(graph)
    except Exception:
        return None


def get_eigen_centrality(graph):
    try:
        return nx.eigenvector_centrality(graph)
    except Exception:
        return None


def get_page_rank(graph):
    try:
        return nx.pagerank(graph)
    except Exception:
        return None


def get_out_degree(graph):
    try:
        return list(graph.out_degree())
    except Exception:
        return None


def add_nodes_attributes(graph):
    degrees = get_degrees(graph)
    eccentricity = get_eccentricity(graph)
    betweenness_centrality = get_betweenness_centrality(graph)
    closeness_centrality = get_closeness_centrality(graph)
    eigen_centrality = get_eigen_centrality(graph)
    page_rank = get_page_rank(graph)
    for node in graph.nodes:
        if degrees:
            graph.nodes[node][NodeAttributes.DEGREE] = degrees[node]

        if eccentricity:
            graph.nodes[node][NodeAttributes.ECCENTRICITY] = eccentricity[node]

        if betweenness_centrality:
            graph.nodes[node][NodeAttributes.BETWEENNESS_CENTRALITY] = round(
                betweenness_centrality[node], 2
            )

        if closeness_centrality:
            graph.nodes[node][NodeAttributes.CLOSENESS_CENTRALITY] = round(
                closeness_centrality[node], 2
            )

        if eigen_centrality:
            graph.nodes[node][NodeAttributes.EIGENCENTRALITY] = round(
                eigen_centrality[node], 2
            )

        if page_rank:
            graph.nodes[node][NodeAttributes.PAGERANK] = round(page_rank[node], 2)

    out_degrees = get_out_degree(graph)
    for out_degree in out_degrees:
        graph.nodes[out_degree[0]][NodeAttributes.OUT_DEGREE] = out_degree[1]
