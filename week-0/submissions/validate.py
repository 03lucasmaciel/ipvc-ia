import importlib.util
import os
import sys

# --- CONFIGURAÇÃO DE TESTE (CASO A DO ENUNCIADO) ---
GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
START_A = ((1, 2, 3), (0, 4, 5), (7, 8, 6))


def check_format(path):
    """Verifica se o caminho é uma lista de tuplos de tuplos 3x3."""
    if not isinstance(path, list): return False, "O caminho deve ser uma LISTA."
    if len(path) == 0: return False, "O caminho está vazio."
    for state in path:
        if not (isinstance(state, tuple) and len(state) == 3 and
        all(isinstance(row, tuple) and len(row) == 3 for row in state)):
            return False, "Cada estado deve ser um TUPLO de 3 tuplos (3x3)."
    return True, "OK"

def validate_student_file(filename):
    print("\n" + "="*50)
    print(f"--- A VALIDAR: {filename} ---")
    
    try:
        # Tentar importar o módulo
        spec = importlib.util.spec_from_file_location("student_mod", filename)
        student = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student)
        
        # Verificar existência das funções obrigatórias
        for func in ['bfs', 'dfs', 'ucs']:
            if not hasattr(student, func):
                print(f"[ERRO] Função '{func}' não encontrada no ficheiro.")
                return

        print("[OK] Funções detetadas. A iniciar testes de formato no Caso A...")

        # Testar BFS
        print("\n> A testar BFS...")
        res_bfs = student.bfs(START_A, GOAL)
        if not isinstance(res_bfs, tuple) or len(res_bfs) != 3:
            print("[ERRO] bfs() deve retornar (caminho, custo, memoria).")
        else:
            path, cost, mem = res_bfs
            valid, msg = check_format(path)
            if valid: print(f"  - BFS OK. Passos: {len(path)-1}, Custo Reportado: {cost}, Memória: {mem}")
            else: print(f"  - BFS ERRO de Formato: {msg}")

        # Testar DFS
        print("\n> A testar DFS...")
        res_dfs = student.dfs(START_A, GOAL)
        if not isinstance(res_dfs, tuple) or len(res_dfs) != 3:
            print("[ERRO] dfs() deve retornar (caminho, custo, memoria).")
        else:
            path, cost, mem = res_dfs
            valid, msg = check_format(path)
            if valid: print(f"  - DFS OK. Passos: {len(path)-1}, Custo Reportado: {cost}, Memória: {mem}")
            else: print(f"  - DFS ERRO de Formato: {msg}")

        # Testar UCS
        print("\n> A testar UCS...")
        res_ucs = student.ucs(START_A, GOAL)
        if not isinstance(res_ucs, tuple) or len(res_ucs) != 3:
            print("[ERRO] ucs() deve retornar (caminho, custo, memoria).")
        else:
            path, cost, mem = res_ucs
            valid, msg = check_format(path)
            if valid: 
                print(f"  - UCS OK. Passos: {len(path)-1}, Custo Reportado: {cost}, Memória: {mem}")
                if cost == len(path)-1:
                    print(f"  - Nota: Verifica se o teu custo reflete as regras (Cima=2, Baixo=0.5, etc.).")
            else: print(f"  - UCS ERRO de Formato: {msg}")

        print("\n--- VALIDAÇÃO CONCLUÍDA ---")

    except Exception as e:
        print(f"\n[ERRO FATAL] Ocorreu um erro ao executar o teu código:")
        print(f"Tipo: {type(e).__name__}")
        print(f"Mensagem: {e}")

if __name__ == "__main__":
    # Procura ficheiro exsps_*.py na pasta atual
    files = [f for f in os.listdir('.') if f.startswith("exsps_") and f.endswith(".py")]
    if not files:
        print("Erro: Nenhum ficheiro 'exsps_<numero>.py' encontrado nesta pasta.")
    else:
        if len(files) > 1:
            print("Aviso: mais de um ficheiro exsps_*.py encontrado. A usar:", files[0])
        validate_student_file(files[0])