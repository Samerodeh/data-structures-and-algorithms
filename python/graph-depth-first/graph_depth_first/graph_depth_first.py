class Vertix:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Vertix > {self.value}'

class Edge:
    def __init__(self, vertix , weight = 1):
        self.vertix = vertix
        self.weight = weight

class Graph:
    
    def __init__(self):
        self.graph = {}
    
    def add_node(self, value):
        node = Vertix(value)
        self.graph[node] = []
        return node
    
    def add_edge(self, vertex1, vertex2, weight=0):
        if vertex1 not in self.graph:
            raise KeyError('Vertex1 is not in the graph')

        if vertex2 not in self.graph:
            raise KeyError('Vertex2 is not in the graph')
        
        edge = Edge(vertex2, weight)
        self.graph[vertex1].append(edge)
    
    def get_nodes(self):
      return self.graph.keys()
    
    def get_neighbors(self, node):
        
        array=[]

        if node in self.graph :

            for edge in self.graph[node]:
               array.append((edge.vertix, edge.weight))
            return array

        if len(array)==0:
            return None
 
    
    def size(self):
        return len(self.graph) if len(self.graph) > 0 else None
    
    def depth_first(self,Node):
        if Node not in self.graph.keys():
            return 'No node'
        result = []

        def rec (node):
            print(node.value)
            if not node in result:
                result.append(node)
            for node in self.get_neighbors(node):
                if not node[0] in result:
                    rec (node[0])

        rec (Node)

        return result

if __name__ == '__main__':

    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')
    
    graph.add_edge(a,b)
    graph.add_edge(a,d)
    graph.add_edge(b,a)
    graph.add_edge(b,c)
    graph.add_edge(b,d)
    graph.add_edge(c,b)
    graph.add_edge(c,g)
    graph.add_edge(g,c)
    graph.add_edge(d,a)
    graph.add_edge(d,b)
    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)
    graph.add_edge(e,d)
    graph.add_edge(f,d)
    graph.add_edge(f,h)
    graph.add_edge(h,d)
    graph.add_edge(h,f)

    print(graph.depth_first(e)[5])