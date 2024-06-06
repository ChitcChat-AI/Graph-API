import networkx as nx
from constants import NodeAttributes


def add_nodes_attributes(graph):
    degrees = nx.degree(graph)
    eccentricity = nx.eccentricity(graph)
    betweenness_centrality = nx.betweenness_centrality(graph)
    closeness_centrality = nx.closeness_centrality(graph)
    eigen_centrality = nx.eigenvector_centrality(graph)
    page_rank = nx.pagerank(graph)
    for node in graph.nodes:
        graph.nodes[node][NodeAttributes.DEGREE] = degrees[node]
        graph.nodes[node][NodeAttributes.ECCENTRICITY] = eccentricity[node]
        graph.nodes[node][NodeAttributes.BETWEENNESS_CENTRALITY] = round(
            betweenness_centrality[node], 2
        )
        graph.nodes[node][NodeAttributes.CLOSENESS_CENTRALITY] = round(
            closeness_centrality[node], 2
        )
        graph.nodes[node][NodeAttributes.EIGENCENTRALITY] = round(
            eigen_centrality[node], 2
        )
        graph.nodes[node][NodeAttributes.PAGERANK] = round(page_rank[node], 2)

    out_degrees = list(graph.out_degree())
    for out_degree in out_degrees:
        graph.nodes[out_degree[0]][NodeAttributes.OUT_DEGREE] = out_degree[1]
