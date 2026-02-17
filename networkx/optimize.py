import itertools
import networkx as nx

def build_base_graph():
    G = nx.DiGraph()

    G.add_edge("Plant", "A", capacity=6)
    G.add_edge("Plant", "B", capacity=4)
    G.add_edge("A", "C", capacity=3)
    G.add_edge("B", "C", capacity=2)
    G.add_edge("C", "City", capacity=4)

    G.add_edge("A", "City", capacity=1)
    G.add_edge("B", "City", capacity=1)

    return G

def apply_upgrades(G, upgrades):
    for u, v, extra_cap, _cost in upgrades:
        if G.has_edge(u, v):
            G[u][v]["capacity"] += extra_cap
        else:
            G.add_edge(u, v, capacity=extra_cap)

def evaluate(G, demand):
    served, flow_dict = nx.maximum_flow(G, "Plant", "City", capacity="capacity")
    served = min(served, demand)
    return served, flow_dict

def optimize_upgrades(demand=8, budget=8):
    base = build_base_graph()

    candidates = [
        ("A", "C", 3, 3), 
        ("B", "C", 3, 3), 
        ("C", "City", 4, 4),
        ("Plant", "A", 4, 4),
        ("Plant", "B", 4, 4),
        ("A", "City", 3, 2),
        ("B", "City", 3, 2),
    ]

    best = None
    best_set = None
    best_flow = None

    for r in range(len(candidates) +1):
        for subset in itertools.combinations(candidates, r):
            cost = sum(u[3] for u in subset)
            if cost > budget:
                continue

            G = base.copy()
            apply_upgrades(G, subset)
            served, flow = evaluate(G, demand)

            score = (served, -cost, -len(subset))

            if best is None or score > best:
                best = score
                best_set = subset
                best_flow = flow

    served_best, neg_cost, neg_n = best
    total_cost = -neg_cost

    return served_best, total_cost, best_set, best_flow

def pretty_print_solution(served, cost, upgrades, flow):
    print("\n=== Best Upgrade Plan ===")
    print(f"Served demand: {served}")
    print(f"Upgrade cost : {cost}")

    if upgrades:
        print("\nUpgrades chosen:")
        for u, v, extra, c in upgrades:
            print(f"  - {u}->{v}  +{extra} cap  (cost {c})")
    else:
        print("\nNo upgrades needed / chosen.")

    print("\nFlow on edges (non-zero):")
    for u, nbrs in flow.items():
        for v, f in nbrs.items():
            if f:
                print(f"  {u}->{v}: {f}")

if __name__ == "__main__":
    DEMAND = 8
    BUDGET = 8

    served, cost, upgrades, flow = optimize_upgrades(demand=DEMAND, budget=BUDGET)
    pretty_print_solution(served, cost, upgrades, flow)