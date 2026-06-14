import numpy as np

states = ("Rainy", "Sunny")
observations = ["walk", "shop", "clean"]

start_p = {"Rainy": 0.6, "Sunny": 0.4}

trans_p = {
    "Rainy": {"Rainy": 0.7, "Sunny": 0.3},
    "Sunny": {"Rainy": 0.4, "Sunny": 0.6},
}

emit_p = {
    "Rainy": {"walk": 0.1, "shop": 0.4, "clean": 0.5},
    "Sunny": {"walk": 0.6, "shop": 0.3, "clean": 0.1},
}


def viterbi(obs):
    V = [{}]

    for st in states:
        V[0][st] = start_p[st] * emit_p[st][obs[0]]

    for t in range(1, len(obs)):
        V.append({})

        for st in states:
            V[t][st] = max(
                V[t - 1][prev] * trans_p[prev][st] * emit_p[st][obs[t]]
                for prev in states
            )

    for t in range(len(V)):
        print(f"Step {t+1}: {V[t]}")


viterbi(observations)