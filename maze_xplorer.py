# maze_xplorer.py - AI Search Algorithms Comparison
# Part 2 of AI Search Algorithm Series

from collections import deque
import heapq

# Maze: S=Start, G=Goal, #=Wall, .=Cost1, F,O=Mud Cost10, E=Water Cost20
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

COST_MAP = {'.':1, 'S':1, 'G':1, 'F':10, 'O':10, 'E':20}

def get_neighbors(pos):
    r, c = pos
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and maze[nr][nc] != '#':
            yield (nr, nc)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def path_cost(path):
    return sum(COST_MAP[maze[r][c]] for r,c in path[1:])

def bfs(start, goal):
    q = deque([(start, [start])])
    visited = set()
    while q:
        pos, path = q.popleft()
        if pos in visited: continue
        visited.add(pos)
        if pos == goal: return path, visited
        for n in get_neighbors(pos):
           
