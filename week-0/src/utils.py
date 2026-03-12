def find_blank(state):
    """Localiza a linha e coluna do espaço vazio (0)."""
    for r, row in enumerate(state):
        for c, val in enumerate(row):
            if val == 0:
                return r, c
    return None

def get_successors(state):
    """
    Gera os estados sucessores movendo o espaço vazio.
    Retorna uma lista de tuplos: (novo_estado, direcao, custo)
    """
    r, c = find_blank(state)
    successors = []
    
    # Definição dos movimentos: (delta_linha, delta_coluna, nome, custo_ucs)
    # Importante: Cima=2.0, Baixo=0.5, Lados=1.0 conforme regras do enunciado
    moves = [
        (-1, 0, 'Cima', 2.0),
        (1, 0, 'Baixo', 0.5),
        (0, -1, 'Esquerda', 1.0),
        (0, 1, 'Direita', 1.0)
    ]

    for dr, dc, move_name, cost in moves:
        nr, nc = r + dr, c + dc
        
        # Verifica se o movimento está dentro dos limites do tabuleiro 3x3
        if 0 <= nr < 3 and 0 <= nc < 3:
            # Converter tuplo em lista de listas para poder trocar as peças
            new_state_list = [list(row) for row in state]
            
            # Troca o 0 com a peça na nova posição
            new_state_list[r][c], new_state_list[nr][nc] = new_state_list[nr][nc], new_state_list[r][c]
            
            # Converter de volta para tuplo de tuplos (imutável e "hashable")
            new_state_tuple = tuple(tuple(row) for row in new_state_list)
            
            successors.append((new_state_tuple, move_name, cost))
            
    return successors

def reconstruct_path(node_map, goal_state):
    """
    Reconstrói o caminho do estado inicial até ao objetivo.
    node_map: dicionário {estado_atual: estado_pai}
    """
    path = []
    current = goal_state
    while current is not None:
        path.append(current)
        current = node_map.get(current)
    return path[::-1] # Inverte a lista para ir do Início -> Fim