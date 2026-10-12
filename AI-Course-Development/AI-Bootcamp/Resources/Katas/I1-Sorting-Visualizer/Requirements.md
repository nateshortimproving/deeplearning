# I1: Sorting Algorithm Visualizer — Requirements

**Difficulty:** Intermediate
**Primary challenge areas:** Algorithm (high), Visualization (high), State (medium), UI (medium)

---

## Challenge

Create a visual comparison tool that animates at least four sorting algorithms simultaneously, side-by-side: bubble sort, insertion sort, merge sort, and quicksort. Each algorithm runs on the same randomly generated array of 50 elements. Include controls for animation speed and array size. Display a step counter for each algorithm showing comparisons made and swaps performed, updating in real time as the animation plays.

---

## Key Technical Requirements

- Correct implementation of all four algorithms with accessible intermediate state — each algorithm must be pauseable and resumable at any comparison or swap; a simple recursive implementation cannot satisfy this requirement; a step-by-step execution model (such as a generator function) is required
- Synchronized animation timing across all four algorithms, which complete at different times
- Step counter accuracy tracking comparisons and swaps at the correct granularity for each algorithm
- State management across multiple simultaneous visualizations

---

## Optional Stretch Goals

- Sound effects where pitch corresponds to the value of the element being compared or swapped
- Big-O notation display with real-time tracking of actual comparisons against the theoretical bound (O(n²) for bubble and insertion, O(n log n) for merge and quicksort)
- Additional algorithms: heap sort, radix sort, shell sort, timsort
- Race mode with a finish-line animation highlighting the first algorithm to complete
