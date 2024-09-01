# Classic trolley problem
class link:
    def __init__(self, destination: int, cost: int):
        self.destination = destination
        self.cost = cost


class node:
    def __init__(self, node_id: int, start: bool, end: bool, links: list[link]):
        self.node_id = node_id
        self.start = start
        self.end = end
        self.links = links


class result:
    def __init__(self, cost: int, steps: list[int]):
        self.cost = cost
        self.steps = steps

    def __lt__(self, other):
        if self.cost == other.cost:
            return len(self.steps) < len(other.steps)
        return self.cost < other.cost


network = [node(1, True, False, [link(2, 10), link(3, 5)]),
           node(2, False, False, [link(1, 10),link(10, 6)]),
           node(3, False, False, [link(1, 5), link(9, 1), link(4, 5)]),
           node(4, False, False, [link(3, 5), link(8, 2), link(7, 5), link(5, 1)]),
           node(5, False, False, [link(4, 1), link(6, 1)]),
           node(6, False, False, [link(5, 1), link(7, 1)]),
           node(7, False, False, [link(6, 1), link(4, 5), link(29, 0)]),
           node(8, False, False, [link(4, 2), link(9, 1), link(17, 10)]),
           node(9, False, False, [link(3, 1), link(8, 1), link(16, 10), link(15, 10), link(10, 10)]),
           node(10, False, False, [link(2, 6), link(11, 1), link(14, 5), link(15, 1), link(9, 10)]),
           node(11, False, False, [link(10, 1), link(12, 1)]),
           node(12, False, False, [link(11, 1), link(26,0), link(13, 1)]),
           node(13, False, False, [link(12, 1), link(25, 1), link(14, 0)]),
           node(14, False, False, [link(10, 5), link(15, 5), link(23, 1), link(13, 0)]),
           node(15, False, False, [link(14, 5), link(20, 10), link(16, 1), link(9, 10), link(10, 1)]),
           node(16, False, False, [link(9, 10), link(15, 1), link(17, 1)]),
           node(17, False, False, [link(16, 1), link(18,5), link(29, 0), link(8, 10)]),
           node(18, False, False, [link(17, 5), link(19, 1)]),
           node(19, False, False, [link(18, 1), link(20, 4)]),
           node(20, False, False, [link(19, 4), link(15,10), link(22, 1), link(21, 1)]),
           node(21, False, False, [link(20, 1), link(22, 5), link(27, 1)]),
           node(22, False, False, [link(21, 5), link(20, 1), link(23, 1), link(27, 5)]),
           node(23, False, False, [link(22, 1), link(14, 1), link(24, 0)]),
           node(24, False, False, [link(23, 0), link(25, 5), link(28, 5)]),
           node(25, False, False, [link(24, 5), link(13, 1), link(26, 0)]),
           node(26, False, False, [link(25,0), link(12, 0)]),
           node(27, False, False, [link(21, 1), link(22,5), link(28,0), link(30, 0)]),
           node(28, False, False, [link(27, 0), link(24, 5), link(30, 0)]),
           node(29, False, False, [link(7, 0), link(17, 0)]),
           node(30, False, True, [link(27, 0), link(28, 0)])]


# Recursive Traverse
def traverse(node_id: int, network_path: result):
    global network
    global results
    cur_node = list(filter(lambda x: x.node_id == node_id, network))

    new_path = result(network_path.cost, network_path.steps.copy())
    new_path.steps.append(node_id)

    # Exit Condition
    if cur_node[0].end:
        results.append(new_path)
        return

    # Explore paths
    for route in cur_node[0].links:
        if route.destination not in network_path.steps:
            network_path.cost += route.cost
            traverse(route.destination, result(new_path.cost + route.cost, new_path.steps))


# DP Traverse
def traverse_dp():
    global network
    global results

    dp = {node.node_id: 99999 for node in network}
    parent = {node.node_id: None for node in network}

    dp[1] = 0  # Start at nodeid 1, with 0 cost

    # Fill min dp table and paths
    for _ in range(len(network) - 1):
        updated = False
        for node in network:
            for link in node.links:
                if dp[node.node_id] + link.cost < dp[link.destination]:
                    dp[link.destination] = dp[node.node_id] + link.cost
                    parent[link.destination] = node.node_id
                    updated = True
        if not updated:
            break

    if dp[30] == 99999:
        return   # no path to exit

    # backtrack to get min path
    path = []
    current_node = 30   # end node
    while current_node is not None:
        path.append(current_node)
        current_node = parent[current_node]
    path.reverse()
    min_result = result(dp[30], path)
    results.append(min_result)


results = []
start_path = result(0, [])

traverse(1, start_path)
min_cost = min(results)
max_cost = max(results)

print(f'{len(results)} Recursive Routes')
print(f'Recursive Min Cost {min_cost.cost} {min_cost.steps}')
print(f'Recursive Max Cost {max_cost.cost} {max_cost.steps}')

results = []
traverse_dp()
min_cost = min(results)

print(f'DP Min Cost {min_cost.cost} {min_cost.steps}')
