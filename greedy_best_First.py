graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("B", 2), ("C", 5), ("G", 12)],
    "B": [("C", 2)],
    "C": [("G", 3)],
}
# Heuristic table
H_table = {"S": 7, "A": 6, "B": 4, "C": 2, "G": 0}


# helper funciton: sending the F cost of the whole path
def path_h_cost(path):
    g_cost = 0
    for node, cost in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    # f_cost = g_cost + h_cost
    return h_cost, last_node


path = [("S", 0), ("A", 1), ("C", 5)]
path2 = [("S", 0), ("A", 1), ("B", 2)]
print(path_h_cost(path))
print(path_h_cost(path2))


def GreedyBestFirst(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_h_cost)  # sorting by cost
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
        for node2, cost in adjacent_nodes:
            new_path = path.copy()
            new_path.append((node2, cost))
            queue.append(new_path)


solution = GreedyBestFirst(graph, "S", "G")
print(solution)
print(path_h_cost(solution)[0])
