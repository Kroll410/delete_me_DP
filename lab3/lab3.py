from sys import maxsize
from itertools import permutations


def travelling_salesman_problem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        current_path_weight = 0

        k = s
        for j in i:
            current_path_weight += graph[k][j]
            k = j
        current_path_weight += graph[k][s]

        min_path = min(min_path, current_path_weight)

    return min_path


if __name__ == "__main__":
    graph_info = []
    with open('info.txt', 'r') as data:
        data = data.readlines()
        V = int(data[0].strip())
        for i, row in enumerate(data[1:]):
            row = [int(x.strip()) for x in row.split(" ")]
            graph_info.append(row)
    s = 0
    print("Lenght of path: ", travelling_salesman_problem(graph_info, s))
