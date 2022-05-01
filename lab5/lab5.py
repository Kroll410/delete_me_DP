import networkx as nx


if __name__ == '__main__':
    G1 = nx.Graph()
    G1.add_edge("A", "D")
    G1.add_edge("A", "C")
    G1.add_edge("C", "B")
    G1.add_edge("C", "D")

    G2 = nx.Graph()
    G2.add_edge("C", "B")
    G2.add_edge("A", "C")
    G2.add_edge("D", "C")
    G2.add_edge("A", "D")

    print(nx.is_isomorphic(G1, G2))