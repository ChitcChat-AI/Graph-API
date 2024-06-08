class Messages:
    UID = "uid"
    NAME = "name"
    TEXT = "text"
    SENTIMENT_SCORE = "sentimentScore"
    CREATED_AT = "createdAt"


class NodeAttributes:
    ID = "id"
    NAME = "name"
    UID = "uid"
    SENTIMENT = "sentiment"
    SENTIMENT_SUM = "sentimentSum"
    SENTIMENT_COUNT = "sentimentCount"
    DEGREE = "degree"
    OUT_DEGREE = "outDegree"
    SIZE = "size"
    COLOR = "color"
    ECCENTRICITY = "eccentricity"
    OPINION_BEFORE = "opinionBefore"
    OPINION_AFTER = "opinionAfter"
    BETWEENNESS_CENTRALITY = "betweennessCentrality"
    CLOSENESS_CENTRALITY = "closenessCentrality"
    EIGENCENTRALITY = "EigenCentrality"
    PAGERANK = "PageRank"


class GraphAttributes:
    RADIUS = "Radius"
    DIAMETER = "Diameter"
    GRAPH_VIEW = "graphView"
    DENSITY = "density"
    POSITIVE_EDGES = "positiveEdges"
    NEGATIVE_EDGES = "negativeEdges"
    NATURAL_EDGES = "naturalEdges"
    RECIPROCITY = "reciprocity"
    TRANSITIVITY = "transitivity"
    AVERAGE_CLUSTERING = "averageClustering"
    AVERAGE_DEGREE_CONNECTIVITY = "averageDegreeConnectivity"
    PATH_LENGTH = "pathLength"


class EdgeAttributes:
    SENTIMENT = "sentiment"
    TYPE = "type"
    TOTAL_SENTIMENT = "totalSentiment"
    MESSAGES = "messages"
