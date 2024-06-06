import networkx as nx
from constants import Messages, NodeAttributes, EdgeAttributes, GraphAttributes
from graph_attributes import (
    add_graph_attributes,
    get_average_clustering,
    get_density,
    get_diameter,
    get_natural_edges,
    get_negative_edges,
    get_path_length,
    get_positive_edges,
    get_radius,
    get_reciprocity,
    get_transitivity,
)
from nodes_attributes import add_nodes_attributes


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

        add_nodes_attributes(self.graph)
        add_graph_attributes(self.graph)

        return nx.readwrite.json_graph.node_link_data(self.graph)
