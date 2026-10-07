import sys

def minimal_dist(node0, adj, d, r, name):
    for node, dist in adj.items():
        if dist + d[node0] < d[node]:
            d[node] = dist + d[node0]
            r[node] = f'{r[node0]} -{name[0]}-> {node}'

    return d, r

def shortest_path(start, network):

    nodes = set()
    for subset in network.values():
        nodes.update(subset.keys())

    d = dict.fromkeys(nodes, sys.maxsize)
    r = dict.fromkeys(nodes, start)

    d[start] = 0

    while any(v == sys.maxsize for v in d.values()):
        for node in nodes:
            for name, adj in network.items():
                if node in adj:
                    d, r = minimal_dist(node, adj[node], d, r, name)

    return d, r
