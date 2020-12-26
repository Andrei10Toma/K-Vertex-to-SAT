import sys


def read():
    graph = {}
    # k for the vertex cover
    k = int(sys.stdin.readline().strip())
    # number of vertexes
    n = int(sys.stdin.readline().strip())
    # number of edges
    m = int(sys.stdin.readline().strip())
    # initialise graph
    for i in range(n):
        graph[i + 1] = []
    for i in range(m):
        edge = sys.stdin.readline().split()
        graph[int(edge[0])].append(int(edge[1]))
        # graph[int(edge[1])].append(int(edge[0]))
    return graph, k, m
