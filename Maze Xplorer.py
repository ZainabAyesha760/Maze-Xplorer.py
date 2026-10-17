# MAZE SOLVER - BFS vs DFS vs UCS vs A* Search
# Part 2 of AI Search Algorithm Series

from collections import deque
import heapq

# 1. MAZE DEFINITION
# S = Start, G = Goal, # = Wall
# . = Normal Cost(1), F,O = Mud Cost(10), E = Water Cost(20)
maze = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', 'F', '#', '.'],
    ['.', '.', 'E', '.', '.'],
    ['#', '#', 'O', '#', '.'],
    ['.', '.', '.', '.', 'G']
]

ROWS, COLS = 5, 5
START = (0, 0)
GOAL = (4, 4)

COST_MAP = {
    '.': 1, 'S': 1, 'G': 1,
    'F': 10, 'O': 10,
    'E': 20
}

def get_neighbors(pos):
    r, c = pos
    neighbors = []
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]: # Up, Down, Left, Right
        nr, nc = r+dr, c+dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if maze[nr][nc] != '#':
                neighbors.append((nr, nc))
    return neighbors

def manhattan_heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 2. ALGORITHMS

def bfs(start, goal):
    frontier = deque([ (start, [start]) ])
    explored = set()
    while frontier:
        pos, path = frontier.popleft()
        if pos in explored: continue
        explored.add(pos)
        if pos == goal: return path, len(explored)
        for n in get_neighbors(pos):
            if n not in explored:
                frontier.append((n, path + [n]))
    return None, len(explored)

def dfs(start, goal):
    frontier = [(start, [start])]
    explored = set()
    while frontier:
        pos, path = frontier.pop()
        if pos in explored: continue
        explored.add(pos)
        if pos == goal: return path, len(explored)
        for n in get_neighbors(pos):
            if n not in explored:
                frontier.append((n, path + [n]))
    return None, len(explored)

def ucs(start, goal):
    frontier = [(0, start, [start])] # cost, pos, path
    explored = set()
    while frontier:
        cost, pos, path = heapq.heappop(frontier)
        if pos in explored: continue
        explored.add(pos)
        if pos == goal: return path, cost, len(explored)
        for n in get_neighbors(pos):
            if n not in explored:
                new_cost = cost + COST_MAP[maze[n[0]][n[1]]]
                heapq.heappush(frontier, (new_cost, n, path + [n]))
    return None, 0, len(explored)

def astar(start, goal):
    # f = g + h
    frontier = [(manhattan_heuristic(start, goal), 0, start, [start])] # f, g, pos, path
    explored = set()
    while frontier:
        f, g, pos, path = heapq.heappop(frontier)
        if pos in explored: continue
        explored.add(pos)
        if pos == goal: return path, g, len(explored)
        for n in get_neighbors(pos):
            if n not in explored:
                new_g = g + COST_MAP[maze[n[0]][n[1]]]
                new_f = new_g + manhattan_heuristic(n, goal)
                heapq.heappush(frontier, (new_f, new_g, n, path + [n]))
    return None, 0, len(explored)

def calculate_path_cost(path):
    if not path: return 0
    return sum(COST_MAP[maze[r][c]] for r,c in path[1:])

# 3. RUN AND COMPARE
print("--- MAZE SOLVING RESULTS ---")
bfs_path, bfs_exp = bfs(START, GOAL)
dfs_path, dfs_exp = dfs(START, GOAL)
ucs_path, ucs_cost, ucs_exp = ucs(START, GOAL)
astar_path, astar_cost, astar_exp = astar(START, GOAL)

print(f"BFS Path: {bfs_path} | Steps: {len(bfs_path)-1} | Cost: {calculate_path_cost(bfs_path)} | Nodes: {bfs_exp}")
print(f"DFS Path: {dfs_path} | Steps: {len(dfs_path)-1} | Cost: {calculate_path_cost(dfs_path)} | Nodes: {dfs_exp}")
print(f"UCS Path: {ucs_path} | Steps: {len(ucs_path)-1} | Cost: {ucs_cost} | Nodes: {ucs_exp}")
print(f"A*  Path: {astar_path} | Steps: {len(astar_path)-1} | Cost: {astar_cost} | Nodes: {astar_exp}")

# Comparison Table for LinkedIn
print("\n| Algorithm | Path Length | Total Cost | Nodes Expanded | Optimal? |")
print("|---|---|---|---|---|")
print(f"| BFS | {len(bfs_path)-1} | {calculate_path_cost(bfs_path)} | {bfs_exp} | No (ignores cost) |")
print(f"| DFS | {len(dfs_path)-1} | {calculate_path_cost(dfs_path)} | {dfs_exp} | No |")
print(f"| UCS | {len(ucs_path)-1} | {ucs_cost} | {ucs_exp} | Yes |")
print(f"| A* | {len(astar_path)-1} | {astar_cost} | {astar_exp} | Yes (Fastest) |")
