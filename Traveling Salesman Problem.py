from itertools import permutations

V = 4


def travel_salesmen_problem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
            print(vertex)

    minimum_path = []
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_path_weight = 0

        k = s
        for j in i:
            current_path_weight += graph[k][j]
            k = j
        current_path_weight += graph[k][s]
        minimum_path.append(current_path_weight)
        x = sorted(minimum_path)

    return x[0]


if __name__ == "__main__":
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]
             ]
    s = 0

    print(travel_salesmen_problem(graph, s))
