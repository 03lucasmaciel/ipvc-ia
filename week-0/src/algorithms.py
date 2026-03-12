from collections import deque
import sys
import os

# Adiciona a pasta src ao path para podermos importar o utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_successors, reconstruct_path

def bfs(start, goal):
    # Fronteira: armazena tuplos de (estado_atual, custo_acumulado)
    # Usamos uma fila (FIFO) para o BFS
    queue = deque([(start, 0)])
    
    # visitados: dicionário para evitar ciclos e reconstruir o caminho
    # { estado_filho: estado_pai }
    visited = {start: None}
    
    max_memory = 1
    
    while queue:
        # Atualiza a métrica de memória máxima (tamanho da fronteira)
        max_memory = max(max_memory, len(queue))
        
        current_state, current_cost = queue.popleft()
        
        # Teste do Objetivo
        if current_state == goal:
            path = reconstruct_path(visited, goal)
            # No BFS, cada passo tem custo 1
            return path, float(len(path) - 1), max_memory
        
        # Expansão de sucessores
        for next_state, direction, move_cost in get_successors(current_state):
            if next_state not in visited:
                visited[next_state] = current_state
                queue.append((next_state, current_cost + 1))
                
    return None, 0, max_memory
  
def dfs(start, goal):
    # Fronteira: usamos uma lista como Pilha (LIFO)
    # Guardamos (estado_atual, custo_acumulado)
    stack = [(start, 0)]
    
    # visitados: { estado_filho: estado_pai }
    visited = {start: None}
    
    max_memory = 1
    
    while stack:
        # Atualiza a métrica de memória máxima
        max_memory = max(max_memory, len(stack))
        
        current_state, current_cost = stack.pop() # LIFO
        
        # Teste do Objetivo
        if current_state == goal:
            path = reconstruct_path(visited, goal)
            return path, float(len(path) - 1), max_memory
        
        # Expansão de sucessores
        for next_state, direction, move_cost in get_successors(current_state):
            if next_state not in visited:
                visited[next_state] = current_state
                stack.append((next_state, current_cost + 1))
                
    return None, 0, max_memory