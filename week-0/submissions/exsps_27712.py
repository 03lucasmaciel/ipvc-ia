import heapq
from collections import deque

# Author: Lucas Maciel Andrade @ 27712
# Course: Artificial Intelligence
# Assignment: PC01 - Uninformed Search (8-puzzle)

# --- HELPER FUNCTIONS ---

def find_blank(state):
    for r, row in enumerate(state):
        for c, val in enumerate(row):
            if val == 0: return r, c
    return None

def get_successors(state):
    r, c = find_blank(state)
    successors = []
    # Cost is defined by the TILE movement direction; blank movement is the opposite.
    # Blank up => tile moves down (0.5), blank down => tile moves up (2.0).
    moves = [(-1, 0, 0.5), (1, 0, 2.0), (0, -1, 1.0), (0, 1, 1.0)]
    for dr, dc, cost in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [list(row) for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            successors.append((tuple(tuple(row) for row in new_state), cost))
    return successors

def reconstruct_path(node_map, goal_state):
    path = []
    current = goal_state
    while current is not None:
        path.append(current)
        current = node_map.get(current)
    return path[::-1]

# --- MAIN ALGORITHMS ---

def bfs(start, goal):
    queue = deque([(start, 0)])
    visited = {start: None}
    max_memory = 1
    while queue:
        max_memory = max(max_memory, len(queue))
        curr, cost = queue.popleft()
        if curr == goal:
            p = reconstruct_path(visited, goal)
            return p, float(len(p)-1), max_memory
        for nxt, _ in get_successors(curr):
            if nxt not in visited:
                visited[nxt] = curr
                queue.append((nxt, cost + 1))
    return None, 0, max_memory

def dfs(start, goal):
    stack = [(start, 0)]
    visited = {start: None}
    max_memory = 1
    while stack:
        max_memory = max(max_memory, len(stack))
        curr, cost = stack.pop()
        if curr == goal:
            p = reconstruct_path(visited, goal)
            return p, float(len(p)-1), max_memory
        for nxt, _ in get_successors(curr):
            if nxt not in visited:
                visited[nxt] = curr
                stack.append((nxt, cost + 1))
    return None, 0, max_memory

def ucs(start, goal):
    pq = [(0.0, start)]
    visited_costs = {start: 0.0}
    parent_map = {start: None}
    max_memory = 1
    while pq:
        max_memory = max(max_memory, len(pq))
        curr_cost, curr_state = heapq.heappop(pq)
        if curr_cost > visited_costs.get(curr_state, float("inf")):
            continue
        if curr_state == goal:
            return reconstruct_path(parent_map, goal), curr_cost, max_memory
        for nxt, move_cost in get_successors(curr_state):
            new_cost = curr_cost + move_cost
            if nxt not in visited_costs or new_cost < visited_costs[nxt]:
                visited_costs[nxt] = new_cost
                parent_map[nxt] = curr_state
                heapq.heappush(pq, (new_cost, nxt))
    return None, 0, max_memory