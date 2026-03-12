from algorithms import bfs, dfs, ucs

START_A = ((1, 2, 3), (0, 4, 5), (7, 8, 6))
GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def run_test(name, func):
    print(f"\n--- A testar {name} ---")
    path, cost, mem = func(START_A, GOAL)
    if path:
        print(f"Sucesso! Passos: {len(path)-1}")
        print(f"Custo Total: {cost}")
        print(f"Memória Máxima: {mem}")
    else:
        print("Falhou!")

run_test("BFS", bfs)
run_test("DFS", dfs)
run_test("UCS", ucs)