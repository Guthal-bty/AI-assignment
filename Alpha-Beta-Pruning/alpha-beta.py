import math
import networkx as nx
import matplotlib.pyplot as plt

visited = []
pruned = []

tree = [3, 5, 6, 9, 1, 2, 0, -1]


def alphabeta(depth, node, maximizing, alpha, beta):

    visited.append(node)

    if depth == 3:
        return tree[node]

    if maximizing:

        value = -math.inf

        for i in range(2):

            value = max(
                value,
                alphabeta(
                    depth + 1,
                    node * 2 + i,
                    False,
                    alpha,
                    beta,
                ),
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                pruned.append(node)
                break

        return value

    else:

        value = math.inf

        for i in range(2):

            value = min(
                value,
                alphabeta(
                    depth + 1,
                    node * 2 + i,
                    True,
                    alpha,
                    beta,
                ),
            )

            beta = min(beta, value)

            if alpha >= beta:
                pruned.append(node)
                break

        return value


result = alphabeta(
    0,
    0,
    True,
    -math.inf,
    math.inf
)

print("Optimal Value =", result)

G = nx.Graph()

edges = [
    ("A","B"),("A","C"),
    ("B","D"),("B","E"),
    ("C","F"),("C","G")
]

G.add_edges_from(edges)

colors = []

for node in G.nodes():

    if node in ["B","C"]:
        colors.append("red")
    else:
        colors.append("green")

nx.draw(
    G,
    with_labels=True,
    node_color=colors,
    node_size=2500
)

plt.title("Alpha-Beta Pruning")
plt.show()