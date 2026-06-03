# 1631. Path With Minimum Effort


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/path-with-minimum-effort/)


## 📝 Problem Description

You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)` (i.e., **0-indexed**). You can move **up**, **down**, **left**, or **right**, and you wish to find a route that requires the minimum **effort**.

A route's **effort** is the **maximum absolute difference**** **in heights between two consecutive cells of the route.

Return *the minimum **effort** required to travel from the top-left cell to the bottom-right cell.*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/04/ex1.png)

```

**Input:** heights = [[1,2,2],[3,8,2],[5,3,5]]
**Output:** 2
**Explanation:** The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/04/ex2.png)

```

**Input:** heights = [[1,2,3],[3,8,4],[5,3,5]]
**Output:** 1
**Explanation:** The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

```

Example 3:**

![](https://assets.leetcode.com/uploads/2020/10/04/ex3.png)
```

**Input:** heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
**Output:** 0
**Explanation:** This route does not require any effort.

```

 

**Constraints:**

	- `rows == heights.length`

	- `columns == heights[i].length`

	- `1 <= rows, columns <= 100`

	- `1 <= heights[i][j] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
This solution uses Dijkstra's algorithm with a twist, where it inverts the thinking by considering the effort required to travel between cells as the maximum absolute difference in heights. This allows it to use a priority queue to efficiently explore the most promising paths.

**Approach**
1. Initialize a matrix `efforts_mat` to store the minimum effort required to reach each cell, with all values initially set to infinity.
2. Create a priority queue `heap` and add the starting point (bottom-right cell) with an effort of 0.
3. While the heap is not empty, pop the cell with the minimum effort.
4. If the popped cell is the top-left cell, return its effort as the minimum effort required to travel from the top-left cell to the bottom-right cell.
5. For each neighboring cell, calculate the effort required to reach it by taking the maximum of the current effort and the absolute difference in heights between the current cell and the neighboring cell.
6. If the calculated effort is less than the stored effort in `efforts_mat`, update the stored effort and add the neighboring cell to the heap.

**Time Complexity**
O(m*n*log(m*n)), where m and n are the number of rows and columns in the `heights` matrix. This is because each cell is visited at most once, and the priority queue operations (insertion and extraction) take O(log(m*n)) time.

**Space Complexity**
O(m*n), where m and n are the number of rows and columns in the `heights` matrix. This is because we need to store the minimum effort required to reach each cell in the `efforts_mat` matrix.

**Key Insight**
The key insight here is to use a priority queue to efficiently explore the most promising paths, and to invert the thinking by considering the effort required to travel between cells as the maximum absolute difference in heights. This allows us to use a simple and efficient algorithm to find the minimum effort required to travel from the top-left cell to the bottom-right cell.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 175 ms (Beats 99.94%) |
| 💾 Memory | 19 MB (Beats 100%) |
| 📅 Solved | 2025-09-04 |
| 💻 Language | Python |