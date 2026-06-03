> 📌 **Cross-listed:** Primary location is [Array/0498-Diagonal-Traverse](../../Array/0498-Diagonal-Traverse). This problem also appears under: **Array**, **Matrix**, **Simulation**

# 498. Diagonal Traverse


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/diagonal-traverse/)


## 📝 Problem Description

Given an `m x n` matrix `mat`, return *an array of all the elements of the array in a diagonal order*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg)
```

**Input:** mat = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,2,4,7,5,3,6,8,9]

```

Example 2:**

```

**Input:** mat = [[1,2],[3,4]]
**Output:** [1,2,3,4]

```

 

**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1 <= m, n <= 10^4`

	- `1 <= m * n <= 10^4`

	- `-10^5 <= mat[i][j] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The approach to solving this problem is to simulate a diagonal traversal of the matrix. We can achieve this by iterating over the diagonals of the matrix, which can be represented as a series of points (r, c) where r is the row and c is the column. We can traverse each diagonal by moving the row up and the column down.

**Approach**
1. Initialize an empty result list `res` to store the diagonal elements.
2. Define a helper function `check(row, col)` to check if a point (r, c) is within the matrix boundaries.
3. Iterate over the diagonals of the matrix, where each diagonal is represented by a value `d` ranging from 0 to `m + n - 2`.
4. For each diagonal `d`, calculate the starting row `r` and column `c` using the formula `r = 0 if (d < n) else d - n + 1` and `c = d if (d < n) else n - 1`.
5. Traverse the diagonal by moving the row up and the column down, appending each element to the `diag` list.
6. If the diagonal index `d` is even, reverse the `diag` list before appending it to the result list `res`. Otherwise, append it as is.
7. Return the result list `res` containing the diagonal elements.

**Time Complexity**
O(m * n), where m is the number of rows and n is the number of columns. This is because we are traversing each element in the matrix once.

**Space Complexity**
O(m + n), where m is the number of rows and n is the number of columns. This is because we are storing the diagonal elements in the `res` list.

**Key Insight**
The key insight is to recognize that the diagonals of the matrix can be represented as a series of points (r, c) where r is the row and c is the column. By traversing each diagonal, we can efficiently extract the diagonal elements in the correct order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 13 ms (Beats 43.16%) |
| 💾 Memory | 19.5 MB (Beats 100%) |
| 📅 Solved | 2025-08-25 |
| 💻 Language | Python |