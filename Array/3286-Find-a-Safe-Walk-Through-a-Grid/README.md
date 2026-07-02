# 3286. Find a Safe Walk Through a Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/)


## 📝 Problem Description

You are given an `m x n` binary matrix `grid` and an integer `health`.

You start on the upper-left corner `(0, 0)` and would like to get to the lower-right corner `(m - 1, n - 1)`.

You can move up, down, left, or right from one cell to another adjacent cell as long as your health *remains* **positive**.

Cells `(i, j)` with `grid[i][j] = 1` are considered **unsafe** and reduce your health by 1.

Return `true` if you can reach the final cell with a health value of 1 or more, and `false` otherwise.

 

Example 1:**

**Input:** grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

**Output:** true

**Explanation:**

The final cell can be reached safely by walking along the gray cells below.

![](https://assets.leetcode.com/uploads/2024/08/04/3868_examples_1drawio.png)

Example 2:**

**Input:** grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

**Output:** false

**Explanation:**

A minimum of 4 health points is needed to reach the final cell safely.

![](https://assets.leetcode.com/uploads/2024/08/04/3868_examples_2drawio.png)

Example 3:**

**Input:** grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

**Output:** true

**Explanation:**

The final cell can be reached safely by walking along the gray cells below.

![](https://assets.leetcode.com/uploads/2024/08/04/3868_examples_3drawio.png)

Any path that does not go through the cell `(1, 1)` is unsafe since your health will drop to 0 when reaching the final cell.

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 50`

	- `2 <= m * n`

	- `1 <= health <= m + n`

	- `grid[i][j]` is either 0 or 1.

## 🧠 Solution Explanation

**Intuition**
This solution uses a priority queue (implemented as a heap) to efficiently explore the grid, prioritizing cells with higher health values. The key insight is that we can safely move to a cell if its health value is greater than or equal to the current health value, and we can also move to a cell if its health value is less than the current health value but we have already visited it.

**Approach**
1. Initialize a priority queue with the starting cell (0, 0) and its health value.
2. While the priority queue is not empty:
   1. Dequeue the cell with the highest health value (i.e., the cell with the lowest negative health value).
   2. If the health value of the dequeued cell is less than 1, skip it.
   3. If the dequeued cell is the target cell (m-1, n-1), return True.
   4. Mark the dequeued cell as visited.
   5. For each adjacent cell (up, down, left, right):
      1. If the adjacent cell is within the grid boundaries and has not been visited:
         1. Calculate the health value of the adjacent cell by subtracting the health value of the dequeued cell from the health value of the adjacent cell.
         2. If the health value of the adjacent cell is greater than or equal to 1, enqueue it.
3. If the priority queue is empty and the target cell has not been reached, return False.

**Time Complexity**
O(m*n*log(m*n)) due to the use of a priority queue. The priority queue operations (enqueue and dequeue) take O(log(m*n)) time, and we perform these operations for each cell in the grid.

**Space Complexity**
O(m*n) due to the use of a priority queue and a set to keep track of visited cells. In the worst case, we need to store all cells in the priority queue and the set.

**Key Insight**
The key insight is that we can safely move to a cell if its health value is greater than or equal to the current health value, and we can also move to a cell if its health value is less than the current health value but we have already visited it. This allows us to efficiently explore the grid using a priority queue.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 106 ms (Beats 56.13%) |
| 💾 Memory | 19.9 MB (Beats 33.02%) |
| 📅 Solved | 2026-07-02 |
| 💻 Language | Python |