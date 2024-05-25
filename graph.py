import networkx as nx
from constants import Messages, NodeAttributes, EdgeAttributes, GraphAttributes


class Graph:
    def __init__(self, messages):
        self.graph = nx.MultiDiGraph()
        self.messages = messages

    def create_node(self, message):
        self.graph.add_node(
            message[Messages.UID],
            id=message[Messages.UID],
            name=message[Messages.NAME],
            sentiment=0,
            sentimentSum=0,
            sentimentCount=0,
            size=13,
            color="#e8e8e8",
        )

    def updateNodeSentiment(self, message):
        node = self.graph.nodes[message[Messages.UID]]
        node[NodeAttributes.SENTIMENT_COUNT] += 1
        node[NodeAttributes.SENTIMENT_SUM] += message[Messages.SENTIMENT_SCORE]
        node[NodeAttributes.SENTIMENT] = (
            node[NodeAttributes.SENTIMENT_SUM] / node[NodeAttributes.SENTIMENT_COUNT]
        )

    def create_edge(self, fromId, toId):
        self.graph.add_edge(fromId, toId, totalSentiment=0, sentiment=0, messages=[])

    def updateEdgeAttributes(self, edge, message):
        edge[EdgeAttributes.MESSAGES].append(message)
        edge[EdgeAttributes.TOTAL_SENTIMENT] += message[Messages.SENTIMENT_SCORE]
        edge[EdgeAttributes.SENTIMENT] = edge[EdgeAttributes.TOTAL_SENTIMENT] / len(
            edge[EdgeAttributes.MESSAGES]
        )

        edge_type = "natural"
        if message[EdgeAttributes.SENTIMENT] >= 0.3:
            edge_type = "positive"
        elif message[EdgeAttributes.SENTIMENT] <= -0.3:
            edge_type = "negative"

        edge[EdgeAttributes.TYPE] = edge_type

    def create_graph(self):
        if (
            self.messages[0][Messages.UID] == "RPLkPefjRdQ3WL3prDMQLTtwjZ02"
        ):  # ChitChat id
            self.messages.pop(0)

        for message, i in zip(self.messages, range(len(self.messages))):
            if message[Messages.UID] not in self.graph:
                self.create_node(message)
            self.updateNodeSentiment(message)

            if i == 0:  # handle edge cases
                continue

            if not self.graph.has_edge(
                self.messages[i - 1][Messages.UID], self.messages[i][Messages.UID]
            ):
                self.create_edge(
                    self.messages[i - 1][Messages.UID], self.messages[i][Messages.UID]
                )

            self.updateEdgeAttributes(self.messages[i - 1])

        degrees = nx.degree(self.graph)
        eccentricity = nx.eccentricity(self.graph)
        betweenness_centrality = nx.betweenness_centrality(self.graph)
        closeness_centrality = nx.closeness_centrality(self.graph)
        eigen_centrality = nx.eigenvector_centrality(self.graph)
        page_rank = nx.pagerank(self.graph)
        for node in self.graph.nodes:
            self.graph.nodes[node][NodeAttributes.DEGREE] = degrees[node]
            self.graph.nodes[node][NodeAttributes.ECCENTRICITY] = eccentricity[node]
            self.graph.nodes[node][NodeAttributes.BETWEENNESS_CENTRALITY] = (
                betweenness_centrality[node]
            )
            self.graph.nodes[node][NodeAttributes.CLOSENESS_CENTRALITY] = (
                closeness_centrality[node]
            )
            self.graph.nodes[node][NodeAttributes.EIGENCENTRALITY] = eigen_centrality[
                node
            ]
            self.graph.nodes[node][NodeAttributes.PAGERANK] = page_rank[node]

        # out_degrees = list(self.graph.out_degree())
        # for out_degree in out_degrees:
        #     self.graph.nodes[out_degree[0]][NodeAttributes.OUT_DEGREE] = out_degree[1]
        self.graph.graph[GraphAttributes.DIAMETER] = nx.diameter(self.graph)
        self.graph.graph[GraphAttributes.RADIUS] = nx.radius(self.graph)
        self.graph.graph[GraphAttributes.DENSITY] = nx.density(self.graph)
        self.graph.graph[GraphAttributes.RECIPROCITY] = nx.reciprocity(self.graph)
        self.graph.graph[GraphAttributes.TRANSITIVITY] = nx.transitivity(self.graph)
        self.graph.graph[GraphAttributes.AVERAGE_CLUSTERING] = nx.average_clustering(
            self.graph
        )
        nx.average_degree_connectivity(self.graph)
        nx.path_graph(self.graph)

        self.graph.graph[GraphAttributes.POSITIVE_EDGES] = len(
            [
                edge
                for edge in self.graph.edges(data=True)
                if edge[2][EdgeAttributes.TYPE] == "positive"
            ]
        ) / len(self.graph.edges)
        self.graph.graph[GraphAttributes.NEGATIVE_EDGES] = len(
            [
                edge
                for edge in self.graph.edges(data=True)
                if edge[2][EdgeAttributes.TYPE] == "negative"
            ]
        ) / len(self.graph.edges)
        self.graph.graph[GraphAttributes.NATURAL_EDGES] = len(
            [
                edge
                for edge in self.graph.edges(data=True)
                if edge[2][EdgeAttributes.TYPE] == "natural"
            ]
        ) / len(self.graph.edges)

        return nx.readwrite.json_graph.node_link_data(self.graph)
