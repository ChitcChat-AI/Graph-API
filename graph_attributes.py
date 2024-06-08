import networkx as nx
from constants import Messages, NodeAttributes, EdgeAttributes, GraphAttributes


def get_transitivity(graph):
    try:
        return round(nx.transitivity(graph), 2)
    except nx.NetworkXError:
        return 0


def get_path_length(graph):
    try:
        return len(nx.path_graph(graph))
    except nx.NetworkXError:
        return "Infinite"


def get_average_clustering(graph):
    try:
        return round(nx.average_clustering(graph), 2)
    except nx.NetworkXError:
        return 0


def get_reciprocity(graph):
    try:
        return round(nx.reciprocity(graph), 2)
    except nx.NetworkXError:
        return 0


def get_density(graph):
    try:
        return round(nx.density(graph), 2)
    except nx.NetworkXError:
        return 0


def get_radius(graph):
    try:
        return round(nx.radius(graph), 2)
    except nx.NetworkXError:
        return 0


def get_diameter(graph):
    try:
        return round(nx.diameter(graph), 2)
    except nx.NetworkXError:
        return 0


def get_positive_edges(graph):
    return round(
        len(
            [
                edge
                for edge in graph.edges(data=True)
                if edge[2][EdgeAttributes.TYPE] == "positive"
            ]
        )
        / len(graph.edges),
        2,
    )


def get_negative_edges(graph):
    return round(
        len(
            [
                edge
                for edge in graph.edges(data=True)
                if edge[2][EdgeAttributes.TYPE] == "negative"
            ]
        )
        / len(graph.edges),
        2,
    )


def get_natural_edges(graph):
    return round(
        len(
            [
                edge
                for edge in graph.edges(data=True)
                if edge[2][EdgeAttributes.TYPE] == "natural"
            ]
        )
        / len(graph.edges),
        2,
    )


def add_graph_attributes(graph):
    graph.graph[GraphAttributes.DIAMETER] = get_diameter(graph)
    graph.graph[GraphAttributes.RADIUS] = get_radius(graph)
    graph.graph[GraphAttributes.DENSITY] = get_density(graph)
    graph.graph[GraphAttributes.RECIPROCITY] = get_reciprocity(graph)
    graph.graph[GraphAttributes.TRANSITIVITY] = get_transitivity(graph)
    graph.graph[GraphAttributes.PATH_LENGTH] = get_path_length(graph)
    graph.graph[GraphAttributes.AVERAGE_CLUSTERING] = get_average_clustering(graph)

    if len(graph.edges) > 0:
        graph.graph[GraphAttributes.POSITIVE_EDGES] = get_positive_edges(graph)
        graph.graph[GraphAttributes.NEGATIVE_EDGES] = get_negative_edges(graph)
        graph.graph[GraphAttributes.NATURAL_EDGES] = get_natural_edges(graph)
    else:
        graph.graph[GraphAttributes.POSITIVE_EDGES] = 0
        graph.graph[GraphAttributes.NEGATIVE_EDGES] = 0
        graph.graph[GraphAttributes.NATURAL_EDGES] = 0
