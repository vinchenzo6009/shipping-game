import sys

def minimal_dist(node0, adj, d, r):
    for node, dist in adj.items():
        if dist + d[node0] < d[node]:
            d[node] = dist + d[node0]
            r[node] = f'{r[node0]} -> {node}'

    return d, r

def shortest_path(start, adj):

    d = dict.fromkeys(adj, sys.maxsize)
    r = dict.fromkeys(adj, start)

    d[start] = 0

    while any(v == sys.maxsize for v in d.values()):
        for node in d:
            d, r = minimal_dist(node, adj[node], d, r)

    return d, r
