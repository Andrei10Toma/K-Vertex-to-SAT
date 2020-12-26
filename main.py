from stdin_read import read
from transform import transform_k_vertex

if __name__ == '__main__':
    graph, k, number_edges = read()
    cnf = transform_k_vertex(graph, k)
    print(cnf)
