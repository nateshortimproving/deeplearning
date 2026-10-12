# A1: Pathfinding Grid Explorer — Expected Outcomes

---

## What the Completed Application Delivers

A user places a start point and end point on the grid by clicking. Walls are drawn by clicking or dragging. Pressing the search button animates both A* and Dijkstra's running simultaneously. Cells change color as they move from unvisited to frontier to visited. When each algorithm finds the path, the path is highlighted. The sidebar shows path length and total nodes explored for each algorithm.

The user can clear walls, reposition start/end points, and re-run on a different configuration. Dragging quickly to draw walls produces a solid wall with no gaps.

---

## Correctness Bar

Both algorithms must find the shortest path when one exists. On an unweighted grid without diagonal movement, A* with the Manhattan heuristic must find the same path length as Dijkstra's.

A* must explore fewer or equal nodes than Dijkstra's on the same grid — if A* explores more nodes, the heuristic is implemented incorrectly or is inadmissible.

Wall drawing interpolation must be correct: dragging the mouse quickly across the grid must produce a solid wall with no gaps, regardless of how fast the mouse moves. A wall with holes that allow a path to pass through when none should exist is a functional failure.
