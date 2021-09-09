class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, value):
        node = Vertex(value)
        self.graph[node] = []
        return node

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.graph:
            raise KeyError('Vertex1 is not in the graph')

        if vertex2 not in self.graph:
            raise KeyError('Vertex2 is not in the graph')


        edge = Edge(vertex2, weight)
        self.graph[vertex1].append(edge)

    def get_nodes(self):
        return self.graph.keys()

    def get_neighbors(self, vertex):
        collection = []
        connections =  self.graph.get(vertex, [])

        for neighbor in connections:
            holder = {}
            holder[neighbor] = neighbor.weight
            collection.append(holder)

        return collection

    def size(self):
        return len(self.graph) if len(self.graph) > 0 else None

if __name__ == "__main__":

    graph = Graph()
    vertex1 = graph.add_node('a')
    vertex2 = graph.add_node('b')
    vertex3 = graph.add_node('c')
    vertex4 = graph.add_node('d')
    graph.add_edge(vertex1, vertex2)
    graph.add_edge(vertex2, vertex1)
    graph.add_edge(vertex1, vertex3)
    graph.add_edge(vertex3, vertex1)
    graph.add_edge(vertex1, vertex4)
    graph.add_edge(vertex2, vertex3)
    print(graph.get_nodes())
    print('Size: ', graph.size())