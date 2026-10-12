# I1: Sorting Algorithm Visualizer — Expected Outcomes

---

## What the Completed Application Delivers

A user sees four sorting visualizations running simultaneously on the same input array. Each visualization shows colored bars representing array elements. As the algorithm runs, bars animate to reflect comparisons (highlighted) and swaps (physically moving between positions). Each visualization has its own step counter showing comparisons and swaps so far, updating live.

The user can adjust animation speed with a slider. The user can generate a new random array and restart all four algorithms simultaneously. When one algorithm finishes, its visualization shows the sorted result and final step counts; the others continue until they also finish.

---

## Correctness Bar

All four algorithms must produce correctly sorted output for any input array.

The step counters must reflect actual algorithm behavior — bubble sort on 50 elements must show significantly more comparisons than merge sort, consistent with their Big-O characteristics. The ratio should be in the right order: bubble sort O(n²) vs. merge sort O(n log n) on 50 elements is roughly 2,500 vs. 280 comparisons.

The pauseable execution model must be correct: pausing mid-sort and resuming must continue from exactly the same state without corrupting the array or producing incorrect final output. Swapping elements must be visible as a physical movement between positions — not an instantaneous replacement.
