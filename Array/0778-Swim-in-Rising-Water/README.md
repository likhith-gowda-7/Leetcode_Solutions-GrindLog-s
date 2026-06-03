# 778. Swim in Rising Water


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/swim-in-rising-water/)


## 📝 Problem Description

You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`.

It starts raining, and water gradually rises over time. At time `t`, the water level is `t`, meaning **any** cell with elevation less than equal to `t` is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return *the minimum time until you can reach the bottom right square *`(n - 1, n - 1)`* if you start at the top left square *`(0, 0)`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/29/swim1-grid.jpg)
```

**Input:** grid = [[0,2],[1,3]]
**Output:** 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg)
```

**Input:** grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
**Output:** 16
**Explanation:** The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

```

 

**Constraints:**

	- `n == grid.length`

	- `n == grid[i].length`

	- `1 <= n <= 50`

	- `0 <= grid[i][j] < n^2`

	- Each value `grid[i][j]` is **unique**.

## 🧠 Solution Explanation

**Intuition**
The problem can be solved by using a modified Dijkstra's algorithm to find the minimum time it takes to reach the bottom right square from the top left square. The key insight is to use a priority queue (min heap) to efficiently find the minimum cost path.

**Approach**
1. Initialize a min heap with the starting point (0, 0) and its corresponding maximum elevation value.
2. While the min heap is not empty, pop the node with the minimum cost (maximum elevation value) from the heap.
3. If the popped node is the bottom right square, return its cost as the minimum time.
4. For each of the four adjacent squares (up, down, left, right) of the popped node, check if it is within the grid boundaries and not visited before.
5. If the adjacent square is valid, calculate its maximum elevation value by taking the maximum of its current elevation value and the cost of the popped node.
6. Push the adjacent square into the min heap with its updated maximum elevation value.
7. Mark the adjacent square as visited by setting its elevation value to -1.

**Time Complexity**
O(n^2 * log(n^2)) = O(n^4)
The time complexity is dominated by the heap operations (push and pop) which take log(n^2) time each. Since we perform these operations for each cell in the grid, the total time complexity is O(n^2 * log(n^2)).

**Space Complexity**
O(n^2)
We use a min heap to store the nodes to be processed, which requires O(n^2) space. We also use a 2D grid to mark the visited nodes, which requires O(n^2) space.

**Key Insight**
The key insight is to use a priority queue (min heap) to efficiently find the minimum cost path. By using the maximum elevation value as the cost, we can ensure that the node with the minimum cost (maximum elevation value) is always popped from the heap, allowing us to find the minimum time it takes to reach the bottom right square.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 23 ms (Beats 68.38%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-10-06 |
| 💻 Language | Python |