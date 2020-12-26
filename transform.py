def transform_k_vertex(graph: dict, k: int):
    cnf = ""
    number_of_vertexes = len(graph.keys())
    for i in range(k):
        # k vertexes to be chosen
        # create k clauses with number_of_vertexes literals
        clause = "("
        for j in range(number_of_vertexes):
            clause += str(i * number_of_vertexes + j + 1) + "V"
        clause = clause[:-1]
        clause += ")"
        cnf += clause + "^"

        # choose only one variable true in each k clause
        for j in range(number_of_vertexes):
            for m in range(j + 1, number_of_vertexes):
                clause = "(~" + str(j + 1 + i * number_of_vertexes) + "V~" + str(m + 1 + i * number_of_vertexes) + ")"
                cnf += clause + "^"

    # choose only one vertex at a specific position
    for i in range(number_of_vertexes):
        for j in range(k - 1):
            for m in range(j + 1, k):
                clause = "(~" + str(i + 1 + number_of_vertexes * j) + "V~" + str(i + 1 + number_of_vertexes * m) + ")"
                cnf += clause + "^"

    # one vertex from the cover should be from the edges
    print(graph)
    for edges in graph.keys():
        if len(graph[edges]) != 0:
            for edge in graph[edges]:
                clause = "("
                for i in range(k):
                    clause += str(edges + i * number_of_vertexes) + "V" + str(edge + i * number_of_vertexes) + "V"
                clause = clause[:-1]
                clause += ")"
                cnf += clause + "^"
    cnf = cnf[:-1]
    return cnf
