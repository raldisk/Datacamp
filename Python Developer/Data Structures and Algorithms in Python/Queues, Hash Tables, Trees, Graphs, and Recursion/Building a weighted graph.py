# Building a weighted graph
class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        # Set the data for the vertex
        self.vertices[vertex] = []

    def add_edge(self, source, target, weight):
        # Set the weight
        self.vertices[source].append([target, weight])
