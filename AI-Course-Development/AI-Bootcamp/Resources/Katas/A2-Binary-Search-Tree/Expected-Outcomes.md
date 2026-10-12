# A2: Binary Search Tree Visualizer — Expected Outcomes

---

## What the Completed Application Delivers

A user types a value and inserts it into the tree. The animation shows the algorithm descending from the root, comparing at each node, and placing the new node at the correct leaf position. Deleting a value animates the removal and explicitly shows which of the three deletion cases applies. Traversal animations visit each node in the correct order, highlighting each in sequence.

The tree height and balance factor for each node are visible as labels and update after every operation. The layout is readable for trees up to 20+ nodes, including pathological insertion sequences.

---

## Correctness Bar

BST ordering must be maintained after every operation: for any node, all values in its left subtree must be less than it, and all values in its right subtree must be greater. This invariant must hold after insertions, all three deletion cases, and is verifiable by running an in-order traversal and confirming the output is a sorted sequence.

Balance factors must be correct: a node's balance factor equals its left subtree height minus its right subtree height. These must update correctly after every insertion and deletion.

The tree layout must remain usable for sorted input — inserting 20 values in sorted order produces a degenerate tree; the layout must not render all nodes stacked vertically off-screen or otherwise unreadable.
