# Challenge Summary

* depth first
* Arguments: Node (Starting point of search)
* Return: A collection of nodes in their pre-order depth-first traversal order
* Display the collection


## Whiteboard Process

![Whiteboard Process](asset/graph-depth-first.png)

## Approach & Efficiency

### What approach did you take?

*Algorithm.*

### Why?

*Because : It is Graph.*

### What is the Big O space/time for this approach?

*Time : O(n) : Because : Based on the number of nodes inside the graph.*

*Space : O(1) : Because : No need for additional spaces.*

## Solution

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

| Subject     | links |
| ----------- | ----------- |
| graph_depth_first| [graph_depth_first/graph_depth_first.py](graph_depth_first/graph_depth_first.py) |
| test_graph_depth_first | [tests/test_graph_depth_first.py](tests/test_graph_depth_first.py) |