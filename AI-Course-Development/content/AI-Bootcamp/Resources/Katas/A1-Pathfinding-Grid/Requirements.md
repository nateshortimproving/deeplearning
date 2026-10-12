# A1: Pathfinding Grid Explorer — Requirements

**Difficulty:** Advanced
**Primary challenge areas:** Algorithm (high), UI (high), State (medium), Visualization (high)

---

## Challenge

Build an interactive grid where users can place start and end points and draw walls by clicking or dragging. Implement both A* and Dijkstra's algorithms. When the user triggers the search, animate the algorithm's execution step-by-step: show the frontier expansion (cells currently being evaluated), visited nodes (cells already evaluated), and the final path when found. Display the path length (number of steps) and total nodes explored for each algorithm side-by-side to allow comparison.

---

## Key Technical Requirements

- Min-heap priority queue implementation for A* — a naive sorted array is unacceptably slow on larger grids
- Correct heuristic functions for A*: Manhattan distance for grid movement without diagonals, Euclidean distance for diagonal movement
- Click-and-drag wall drawing with interpolation between mouse events — the mouse can move faster than `mousemove` fires, causing gaps in walls without interpolation
- Animation pacing that allows individual steps to be visible without being too slow or too fast to follow

---

## Optional Stretch Goals

- Weighted terrain with different traversal costs: swamp (cost 5), road (cost 1), walls (impassable)
- Bidirectional search running A* simultaneously from start and end, visualizing both frontiers and their meeting point
- Maze generation using recursive backtracking, Prim's, or Kruskal's algorithms
- Diagonal movement with correct cost calculation (diagonal steps cost √2 ≈ 1.414, not 1)
