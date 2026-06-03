# 542. 01 Matrix


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/01-matrix/)


## 📝 Problem Description

Given an `m x n` binary matrix `mat`, return *the distance of the nearest *`0`* for each cell*.

The distance between two cells sharing a common edge is `1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg)
```

**Input:** mat = [[0,0,0],[0,1,0],[0,0,0]]
**Output:** [[0,0,0],[0,1,0],[0,0,0]]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg)
```

**Input:** mat = [[0,0,0],[0,1,0],[1,1,1]]
**Output:** [[0,0,0],[0,1,0],[1,2,1]]

```

 

**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1 <= m, n <= 10^4`

	- `1 <= m * n <= 10^4`

	- `mat[i][j]` is either `0` or `1`.

	- There is at least one `0` in `mat`.

 

**Note:** This question is the same as 1765: [https://leetcode.com/problems/map-of-highest-peak/](https://leetcode.com/problems/map-of-highest-peak/description/)

## 🧠 Solution Explanation

**Intuition**
The solution uses a breadth-first search (BFS) approach to find the distance of the nearest `0` for each cell in the binary matrix. The key insight is to use a queue to keep track of the cells to visit and a visited matrix to avoid revisiting cells.

**Approach**
1. Initialize a queue `q` to store the cells to visit, a visited matrix `visited` to mark visited cells, and a distance variable `dist` to keep track of the current distance.
2. Iterate through the matrix and add all `0` cells to the queue and mark them as visited.
3. Define a helper function `check` to perform the BFS. It checks if a cell is within the matrix boundaries and not visited before. If so, it marks the cell as visited, adds it to the queue, and updates the matrix with the current distance.
4. Perform BFS by iterating through the queue and calling the `check` function for each cell in the queue. Increment the distance variable after each iteration.
5. Repeat step 4 until the queue is empty.

**Time Complexity**
O(m*n), where m is the number of rows and n is the number of columns in the matrix. This is because each cell in the matrix is visited at most once.

**Space Complexity**
O(m*n), where m is the number of rows and n is the number of columns in the matrix. This is because we need to store the visited matrix and the queue, which can grow up to the size of the matrix.

**Key Insight**
The key insight is to use a queue to keep track of the cells to visit and a visited matrix to avoid revisiting cells. This allows us to perform a BFS traversal of the matrix efficiently and find the distance of the nearest `0` for each cell.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 127 ms (Beats 46.48%) |
| 💾 Memory | 20.5 MB (Beats 99.96%) |
| 📅 Solved | 2025-08-14 |
| 💻 Language | Python |