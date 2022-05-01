class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * self.ROW
        queue = [s]

        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


if __name__ == '__main__':
    graph_info = []
    with open('info.txt', 'r') as data:
        data = data.readlines()
        V = int(data[0].strip())
        for i, row in enumerate(data[1:]):
            row = [int(x.strip()) for x in row.split(" ")]
            graph_info.append(row)

    g = Graph(graph_info)
    source = 0
    sink = 5

    print("Max Flow: %d " % g.ford_fulkerson(source, sink))
