class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, input_from, input_to):
        connections = self.edges.get(input_from)

        if not connections:
            connections = set()
        connections.add(input_to)

        self.edges[input_from] = connections

    def add_both_edges(self, input_from, input_to):
        self.add_edge(input_from, input_to)
        self.add_edge(input_to, input_from)

    def elements_dfs(self):
        result_list = []
        visited = set()

        for element in self.edges.keys():
            self.add_dfs_elements(element, result_list, visited)

        return result_list

    def add_dfs_elements(self, from_element, result_list, visited):
        if from_element in visited:
            return

        result_list.append(from_element)
        visited.add(from_element)

        for e in self.edges[from_element]:
            self.add_dfs_elements(e, result_list, visited)

    def elements_bfs(self):
        visited = set()
        result_list = []

        for k in self.edges.keys():
            queue = [k]
            while len(queue) > 0:
                first_element = queue.pop(0)
                if first_element in visited:
                    continue
                result_list.append(first_element)
                visited.add(first_element)

                for vertex in self.edges[first_element]:
                    queue.append(vertex)
        return result_list

    def is_connected(self, from_element, to_element):
        return self._is_connected(from_element, to_element, set())

    def _is_connected(self, from_element, to_element, visited):
        if from_element in visited:
            return False

        if from_element == to_element:
            return True

        visited.add(from_element)

        for vertex in self.edges[from_element]:
            if self._is_connected(vertex, to_element, visited):
                return True

        return False


if __name__ == "__main__":
    graph = Graph()
    graph.add_both_edges("a", "b")
    graph.add_both_edges("b", "c")
    graph.add_both_edges("b", "d")
    graph.add_both_edges("c", "e")

    print graph.elements_dfs()
    print graph.elements_bfs()

    print graph.is_connected("a", "e")

    graph.add_both_edges("y", "z")

    graph.add_both_edges("e", "z")

    print graph.is_connected("a", "z")
