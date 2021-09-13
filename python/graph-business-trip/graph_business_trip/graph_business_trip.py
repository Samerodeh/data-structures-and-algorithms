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

def business_trip(graph, city_names):

    global cost
    global can1
    global can2

    status = True
    cost = 0
    can1 = 0
    can2 = 1

    def trip(graph, start, end):

        path = graph.graph[start]

        for city in path:
            if end == city.vertex:
                global cost
                cost += city.weight

                if end.value == city_names[-1].value:
                    break
                else:
                    global can1
                    can1 += 1
                    global can2
                    can2 += 1
                    trip(graph, city_names[can1], city_names[can2])

    trip(graph, city_names[can1], city_names[can2])

    if cost == 0:
        status = False

    cost = f"${str(cost)}"
    return (status, cost,)

if __name__ == '__main__':

    graph = Graph()

    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    narina = graph.add_node('narina')
    naboo = graph.add_node('naboo')
    manstropolis = graph.add_node('manstropolis')

    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(pandora,metroville,82)
    graph.add_edge(arendelle,pandora,150)
    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(arendelle,manstropolis,42)
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(metroville,manstropolis,105)
    graph.add_edge(metroville,naboo,26)
    graph.add_edge(metroville,narina,37)
    graph.add_edge(narina,metroville,37)
    graph.add_edge(narina,naboo,250)
    graph.add_edge(naboo,narina,250)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(naboo,manstropolis,73)
    graph.add_edge(manstropolis,naboo,73)
    graph.add_edge(manstropolis,arendelle,42)
    graph.add_edge(manstropolis,metroville,105)
    
    print()
    print(business_trip(graph,[pandora,arendelle]))
    print()