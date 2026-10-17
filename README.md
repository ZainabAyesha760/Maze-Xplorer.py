# MazeXplorer - AI Search Algorithms Comparison
### Part 2 of AI Search Algorithm Series

A Python implementation comparing 4 classic AI search algorithms on a cost-based maze.

### 🗺️ Maze Definition
- `S` = Start, `G` = Goal, `#` = Wall
- `.` = Normal Path (Cost 1)
- `F, O` = Mud (Cost 10)
- `E` = Water (Cost 20)

**Maze Layout:**
S . . # .
. # F # .
. . E . .
# # O # .
. . . . G

### 🧠 Algorithms Compared
1.  **BFS (Breadth-First Search):** Queue - Finds shortest path in steps, ignores cost.
2.  **DFS (Depth-First Search):** Stack - Goes deep first, not optimal.
3.  **UCS (Uniform Cost Search):** Priority Queue - Finds lowest-cost path. Optimal.
4.  **A* Search:** f(n) = g(n) + h(n) where h is Manhattan Distance. Optimal + Fastest.

### 📊 Verified Results (from maze_xplorer.py)

| Algorithm | Steps | Total Cost | Nodes Expanded | Optimal? |
| :--- | :---: | :---: | :---: | :--- |
| BFS | 8 | 36 | 18 | No |
| DFS | 8 | 36 | 9 | No |
| UCS | 8 | 27 | 14 | Yes |
| A* | 8 | 27 | 12 | Yes (Fastest) |

**Key Insight:** UCS and A* find cheaper path (Cost 27) by avoiding high-cost water/mud. A* expands only 12 nodes vs BFS 18, making it best for AI.

### 🚀 How to Run
python maze_xplorer.py

### 🛠️ Tech Stack
Python 3, collections.deque, heapq
