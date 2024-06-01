import networkx as nx
from constants import Messages, NodeAttributes, EdgeAttributes, GraphAttributes


class Graph:
    def __init__(self, messages):
        self.graph = nx.DiGraph()
        self.messages = messages

    def create_node(self, message):
        self.graph.add_node(
            message[Messages.UID],
            id=message[Messages.UID],
            label=message[Messages.NAME],
            sentiment=0,
            sentimentSum=0,
            sentimentCount=0,
            size=13,
            color="#e8e8e8",
        )

    def updateNode(self, message):
        node = self.graph.nodes[message[Messages.UID]]
        node[NodeAttributes.SENTIMENT_COUNT] += 1
        node[NodeAttributes.SIZE] += 1
        node[NodeAttributes.SENTIMENT_SUM] += round(
            message[Messages.SENTIMENT_SCORE], 2
        )
        node[NodeAttributes.SENTIMENT] = round(
            node[NodeAttributes.SENTIMENT_SUM] / node[NodeAttributes.SENTIMENT_COUNT], 2
        )
        if node[NodeAttributes.SENTIMENT] >= 0.3:
            node[NodeAttributes.COLOR] = "#77bf38"
        elif node[NodeAttributes.SENTIMENT] <= -0.3:
            node[NodeAttributes.COLOR] = "#fb8281"
        else:
            node[NodeAttributes.COLOR] = "#e8e8e8"

    def create_edge(self, fromId, toId):
        self.graph.add_edge(
            fromId,
            toId,
            totalSentiment=0,
            sentiment=0,
            messages=[],
        )

    def updateEdgeAttributes(self, edge, newEdge):
        edge[EdgeAttributes.MESSAGES].append(newEdge[Messages.TEXT])
        edge[EdgeAttributes.TOTAL_SENTIMENT] += newEdge[Messages.SENTIMENT_SCORE]
        edge[EdgeAttributes.SENTIMENT] = edge[EdgeAttributes.TOTAL_SENTIMENT] / len(
            edge[EdgeAttributes.MESSAGES]
        )

        if edge[EdgeAttributes.SENTIMENT] >= 0.3:
            edge[EdgeAttributes.TYPE] = "positive"
        elif edge[EdgeAttributes.SENTIMENT] <= -0.3:
            edge[EdgeAttributes.TYPE] = "negative"
        else:
            edge[EdgeAttributes.TYPE] = "natural"

    def create_graph(self):
        if (
            self.messages[0][Messages.UID]
            == "RPLkPefjRdQ3WL3prDMQLTtwjZ02"  # ChitChat id
        ):
            self.messages.pop(0)

        for message, i in zip(self.messages, range(len(self.messages))):
            if message[Messages.UID] not in self.graph:
                self.create_node(message)
            self.updateNode(message)

            if i == 0:  # handle edge cases
                continue

            if not self.graph.has_edge(
                self.messages[i - 1][Messages.UID], self.messages[i][Messages.UID]
            ):
                self.create_edge(
                    self.messages[i - 1][Messages.UID], self.messages[i][Messages.UID]
                )

            self.updateEdgeAttributes(
                self.graph.edges[
                    self.messages[i - 1][Messages.UID], self.messages[i][Messages.UID]
                ],
                self.messages[i - 1],
            )

        degrees = nx.degree(self.graph)
        eccentricity = nx.eccentricity(self.graph)
        betweenness_centrality = nx.betweenness_centrality(self.graph)
        closeness_centrality = nx.closeness_centrality(self.graph)
        eigen_centrality = nx.eigenvector_centrality(self.graph)
        page_rank = nx.pagerank(self.graph)
        for node in self.graph.nodes:
            self.graph.nodes[node][NodeAttributes.DEGREE] = degrees[node]
            self.graph.nodes[node][NodeAttributes.ECCENTRICITY] = eccentricity[node]
            self.graph.nodes[node][NodeAttributes.BETWEENNESS_CENTRALITY] = round(
                betweenness_centrality[node], 2
            )
            self.graph.nodes[node][NodeAttributes.CLOSENESS_CENTRALITY] = round(
                closeness_centrality[node], 2
            )
            self.graph.nodes[node][NodeAttributes.EIGENCENTRALITY] = round(
                eigen_centrality[node], 2
            )
            self.graph.nodes[node][NodeAttributes.PAGERANK] = round(page_rank[node], 2)

        out_degrees = list(self.graph.out_degree())
        for out_degree in out_degrees:
            self.graph.nodes[out_degree[0]][NodeAttributes.OUT_DEGREE] = out_degree[1]
        self.graph.graph[GraphAttributes.DIAMETER] = nx.diameter(self.graph)
        self.graph.graph[GraphAttributes.RADIUS] = nx.radius(self.graph)
        self.graph.graph[GraphAttributes.DENSITY] = round(nx.density(self.graph), 2)
        self.graph.graph[GraphAttributes.RECIPROCITY] = round(
            nx.reciprocity(self.graph), 2
        )
        self.graph.graph[GraphAttributes.TRANSITIVITY] = round(
            nx.transitivity(self.graph), 2
        )
        self.graph.graph[GraphAttributes.PATH_LENGTH] = len(nx.path_graph(self.graph))
        self.graph.graph[GraphAttributes.AVERAGE_CLUSTERING] = round(
            nx.average_clustering(self.graph), 2
        )

        self.graph.graph[GraphAttributes.POSITIVE_EDGES] = round(
            len(
                [
                    edge
                    for edge in self.graph.edges(data=True)
                    if edge[2][EdgeAttributes.TYPE] == "positive"
                ]
            )
            / len(self.graph.edges),
            2,
        )
        self.graph.graph[GraphAttributes.NEGATIVE_EDGES] = round(
            len(
                [
                    edge
                    for edge in self.graph.edges(data=True)
                    if edge[2][EdgeAttributes.TYPE] == "negative"
                ]
            )
            / len(self.graph.edges),
            2,
        )
        self.graph.graph[GraphAttributes.NATURAL_EDGES] = round(
            len(
                [
                    edge
                    for edge in self.graph.edges(data=True)
                    if edge[2][EdgeAttributes.TYPE] == "natural"
                ]
            )
            / len(self.graph.edges),
            2,
        )

        return nx.readwrite.json_graph.node_link_data(self.graph)
