# Definicje reguł topplingu
RULES = {
    "BTW": {
        "threshold": 4,
        "neighbors": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    },
    "MOORE": {
        "threshold": 8,
        "neighbors": [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
    },
    "STOCHASTIC": {
        "threshold": 4,
        "neighbors": [(-1, 0), (1, 0), (0, -1), (0, 1)],
        "random": True
    }
}
