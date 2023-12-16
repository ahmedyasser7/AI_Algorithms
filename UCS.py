graph = {
    "S": [("A", 2), ("B", 3), ("D", 5)],
    "A": [("C", 4)],
    "B": [("D", 4)],
    "C": [("D", 1), ("G", 2)],
    "D": [("G", 5)],
    "G": [],
}


# helper funciton: sending the total cost of the whole path
def path_cost(path):
    tot_cost = 0
    for node, cost in path:
        tot_cost += cost
    return tot_cost, path[-1][0]  # the last node


# path = [("S", 0), ("D", 5), ("G", 5)]
# path2 = [("S", 0), ("B", 3), ("D", 4)]
# print(path_cost(path))
# print(path_cost(path2))


def UCS(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)  # sorting by cost
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


solution = UCS(graph, "S", "G")
print(solution)
print(path_cost(solution)[0])
