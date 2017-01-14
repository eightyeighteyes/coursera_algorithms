import random


def min_cut(matrix):
    return min([karger(matrix) for _ in range(25)])


def karger(matrix):
    nodes = make_nodes(matrix)
    edges = make_edges(nodes)

    while len(nodes) > 2:
        rand_edge = random.randint(0, len(edges) - 1)
        contract_nodes(nodes, edges[rand_edge])
        edges = make_edges(nodes)

    return count_edges(nodes)


def make_nodes(matrix):
    return {node[0]: node[1:] for node in matrix}


def make_edges(nodes):
    edges = []
    for node in nodes:
        for path in nodes[node]:
            edge = [node, path]
            edges.append((edge[0], edge[1]))

    edges.sort()

    return edges


def contract_nodes(nodes, edge):
    # node b will be contracted into node a
    node_a = edge[0]
    node_b = edge[1]

    edges_a = nodes[node_a]
    edges_b = nodes[node_b]

    # remove the merged node
    nodes.pop(node_b)

    for node in nodes:
        edges = nodes[node]

        # establish new edges
        if node != node_a:
            for _ in range(edges_b.count(node)):
                edges.append(node_a)
                edges.sort()

        # remove references to the node being absorbed
        while edges.count(node_b):
            edges.remove(node_b)

    # remove self references
    while edges_b.count(node_a):
        edges_b.remove(node_a)

    new_a = edges_a + edges_b
    new_a.sort()

    nodes[node_a] = new_a

    return nodes


def count_edges(nodes):
    condensed = []
    for node in nodes:
        for path in nodes[node]:
            if node == path:
                continue
            edge = [node, path]
            if edge == [min(edge), max(edge)]:
                condensed.append(edge)

    return len(condensed)
