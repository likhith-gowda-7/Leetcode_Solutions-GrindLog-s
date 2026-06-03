# 867. Transpose Matrix


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/transpose-matrix/)


## 📝 Problem Description

Given a 2D integer array `matrix`, return *the **transpose** of* `matrix`.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

![](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)

 

Example 1:**

```

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [[1,4,7],[2,5,8],[3,6,9]]

```

Example 2:**

```

**Input:** matrix = [[1,2,3],[4,5,6]]
**Output:** [[1,4],[2,5],[3,6]]

```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 1000`

	- `1 <= m * n <= 10^5`

	- `-10^9 <= matrix[i][j] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The transpose of a matrix is obtained by swapping its row and column indices. This can be achieved by iterating over the columns of the original matrix and treating each column as a row in the resulting matrix.

**Approach**
1. Use the built-in Python `zip` function to transpose the matrix. `zip(*matrix)` unpacks the matrix into separate arguments to the `zip` function, effectively transposing the matrix.
2. Iterate over the result of `zip(*matrix)` using a for loop, which yields tuples representing the rows of the transposed matrix.
3. Append each tuple to the result list `res`.
4. Return the result list `res`, which now contains the transposed matrix.

**Time Complexity**
O(m*n), where m is the number of rows and n is the number of columns in the matrix. This is because we are iterating over each element in the matrix once.

**Space Complexity**
O(m*n), as we are creating a new matrix of the same size as the original matrix to store the transposed result.

**Key Insight**
The key insight here is that the `zip` function can be used to transpose a matrix in a concise and efficient manner. By unpacking the matrix into separate arguments to `zip`, we can take advantage of Python's built-in support for tuple unpacking to swap the row and column indices of the matrix.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-01-16 |
| 💻 Language | Python |