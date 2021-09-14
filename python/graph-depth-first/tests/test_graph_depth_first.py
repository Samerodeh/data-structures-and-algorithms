from graph_depth_first import __version__
from graph_depth_first.graph_depth_first import *
import pytest

def test_version():
    assert __version__ == '0.1.0'

#@pytest
def test_add_node(value, Vertex):
    node = Vertex(value)
    actual = value
    excepted = node
    assert actual == excepted

#@pytest
def test_add_edge(vertex1, vertex2, weight=1):
    edge = Edge(vertex2, weight)
    actual = weight(vertex1, vertex2)
    excepted = edge
    assert actual == excepted

#@pytest
def test_get_nodes(self):
    actual = self.graph.keys()
    excepted = actual
    assert actual == excepted

#@pytest
def test_get_neighbors():
    collection = []
    holder = {}
    actual = collection.append(holder)
    excepted = collection
    assert actual == excepted

#@pytest
def test_size(self):
    actual = len(self.graph) if len(self.graph) > 0 else None
    excepted = actual
    assert actual == excepted

#@pytest
def test_depth_first(graph, Node):
    result = []
    actual = graph, Node
    excepted = result
    assert actual == excepted