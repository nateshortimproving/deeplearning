# A2: Binary Search Tree Visualizer — Requirements

**Difficulty:** Advanced
**Primary challenge areas:** Algorithm (high), State (high), Visualization (high), UI (medium)

---

## Challenge

Build an interactive binary search tree where users can insert values, delete values, and search for values. Animate each operation to show the traversal process: for insertion, show the comparisons at each node as the algorithm descends to find the insertion point. For deletion, show the three cases explicitly — leaf deletion, one-child deletion, and two-child deletion with in-order successor. Support in-order, pre-order, and post-order traversal animations that highlight each visited node in sequence. Display the tree height and balance factor for each node, updating after every operation.

---

## Key Technical Requirements

- Tree layout algorithm that positions nodes readably on a 2D canvas for arbitrary insertion sequences, including degenerate cases (sorted input produces a linked-list-shaped tree with 20+ levels that must remain usable)
- Operation animation sequencing where insert, delete, and traversal each have distinct animation logic that cannot interfere with each other
- Balance factor calculation (height of left subtree minus height of right subtree) with correct height tracking after every mutation
- All three deletion cases must be handled correctly and animated distinctly

---

## Optional Stretch Goals

- AVL tree extension with self-balancing rotations animated explicitly (left, right, left-right, right-left)
- Bulk insert with step-forward and step-backward controls through the tree's evolution
- Pathological case demonstration showing sorted input degenerating the BST to a linked list
- Expression tree support: parse a mathematical expression into a tree and animate its evaluation
