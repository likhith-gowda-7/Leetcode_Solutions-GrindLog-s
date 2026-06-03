# 931. Minimum Falling Path Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-falling-path-sum/)


## 📝 Problem Description

Given an `n x n` array of integers `matrix`, return *the **minimum sum** of any **falling path** through* `matrix`.

A **falling path** starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg)
```

**Input:** matrix = [[2,1,3],[6,5,4],[7,8,9]]
**Output:** 13
**Explanation:** There are two falling paths with a minimum sum as shown.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg)
```

**Input:** matrix = [[-19,57],[-40,-5]]
**Output:** -59
**Explanation:** The falling path with a minimum sum is shown.

```

 

**Constraints:**

	- `n == matrix.length == matrix[i].length`

	- `1 <= n <= 100`

	- `-100 <= matrix[i][j] <= 100`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the minimum sum of a "falling path" in a given matrix. A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. The key insight is that we can use dynamic programming to break down the problem into smaller subproblems and find the minimum sum.

**Approach**
1. Define a helper function `check(r, c)` that returns the value of the element at position `(r, c)` in the matrix, or `inf` if the position is out of bounds.
2. Iterate over the matrix from the second last row to the first row.
3. For each element at position `(row, col)`, calculate the minimum sum of the three possible falling paths:
	* Down: `check(row + 1, col)`
	* Left: `check(row + 1, col - 1)`
	* Right: `check(row + 1, col + 1)`
4. Add the minimum sum of the three paths to the current element.
5. After iterating over all elements, return the minimum value in the first row.

**Time Complexity**
O(n^2), where n is the number of rows (or columns) in the matrix. We iterate over each element in the matrix once, and each iteration involves a constant amount of work.

**Space Complexity**
O(1), excluding the space required for the input matrix. We only use a constant amount of space to store the helper function `check` and the variables used in the iteration.

**Key Insight**
The key insight is that we can use dynamic programming to break down the problem into smaller subproblems and find the minimum sum. By iterating over the matrix from the second last row to the first row, we can calculate the minimum sum of each element based on the minimum sums of its neighbors in the previous row. This allows us to find the minimum sum of the entire falling path in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 31 ms (Beats 32.98%) |
| 💾 Memory | 18.9 MB (Beats 100%) |
| 📅 Solved | 2025-11-11 |
| 💻 Language | Python |