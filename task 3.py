from collections import deque


class Graph:
    def __init__(self, adjacency_list):
        """Initializes the graph with an adjacency list."""
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        """Returns the neighbors of a given node."""
        return self.adjacency_list.get(v, [])

    def h(self, n):
        """Heuristic function: estimates the cost from node n to the goal."""
        H = {
            "The": 4,
            "cat": 3,
            "dog": 3,
            "runs": 2,
            "fast": 1
        }
        return H.get(n, float('inf'))

    def a_star_algorithm(self, start_node, stop_node):
        """Implements the A* search algorithm to find the optimal path."""
        open_list = set([start_node])
        closed_list = set([])

        g = {start_node: 0}  # Cost from start node to all other nodes
        parents = {start_node: None}  # Keeps track of paths

        while open_list:
            n = min(open_list, key=lambda node: g[node] + self.h(node))

            if n == stop_node:
                path = []
                while n is not None:
                    path.append(n)
                    n = parents[n]
                path.reverse()
                print("Sentence:", " ".join(path))
                print("Total cost:", g[stop_node])
                return path

            open_list.remove(n)
            closed_list.add(n)

            for (neighbor, cost) in self.get_neighbors(n):
                if neighbor in closed_list:
                    continue

                tentative_g = g[n] + cost

                if neighbor not in open_list or tentative_g < g.get(neighbor, float('inf')):
                    g[neighbor] = tentative_g
                    parents[neighbor] = n
                    open_list.add(neighbor)

        print("Path does not exist!")
        return None


# Define the graph given in adjacency list
adjacency_list = {
    "The": [("cat", 2), ("dog", 2)],
    "cat": [("runs", 2)],
    "dog": [("runs", 2)],
    "runs": [("fast", 2)],
    "fast": []
}

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm("The", "fast")
