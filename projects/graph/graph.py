"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices.update({vertex_id: set()})
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if self.vertices[v1] and self.vertices[v2]:
            self.vertices[v1].add(v2)
        pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size():
            for _ in range(q.size()):
                vert = q.dequeue()
                if vert not in visited:
                    visited.add(vert)
                    print(vert)
                    for edge in self.vertices[vert]:
                        q.enqueue(edge)

        pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size():
            for _ in range(s.size()):
                vert = s.pop()
                if vert not in visited:
                    visited.add(vert)
                    print(vert)
                    for edge in self.vertices[vert]:
                        s.push(edge)
        pass  # TODO

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        def helper(vertex):
            if vertex in visited:
                return
            visited.add(vertex)
            print(vertex)
            for edge in self.vertices[starting_vertex]:
                helper(edge)
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        predecessors = {}
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size():
            for _ in range(q.size()):
                vert = q.dequeue()
                if destination_vertex == vert:
                    arr = []
                    while vert in predecessors:
                        arr.append(vert)
                        vert = predecessors[vert]
                    return arr
                visited.add(vert)
                for edge in self.vertices[vert]:
                    if edge not in visited:
                        q.enqueue(edge)
                        predecessors[edge] = vert
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        predecessors = {}
        while s.size():
            for _ in range(s.size()):
                vert = s.pop()
                if destination_vertex == vert:
                    arr = []
                    while vert in predecessors:
                        arr.append(vert)
                        vert = predecessors[vert]
                    return arr
                if vert not in visited:
                    visited.add(vert)
                    for edge in self.vertices[vert]:
                        if edge not in visited:
                            s.push(edge)
                            predecessors[edge] = vert



    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        def helper(vertex, current, target, ans=['inf', []]):
            if vertex in visited:
                return ans
            if vertex == target:
                current += [vertex]
                return current
            visited.add(vertex)
            print(vertex)
            for edges in self.vertices[starting_vertex]:
                helper(edges)

        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
