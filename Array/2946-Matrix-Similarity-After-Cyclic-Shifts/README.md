# 2946. Matrix Similarity After Cyclic Shifts


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/)


## 📝 Problem Description

You are given an `m x n` integer matrix `mat` and an integer `k`. The matrix rows are 0-indexed.

The following proccess happens `k` times:

	- **Even-indexed** rows (0, 2, 4, ...) are cyclically shifted to the left.

![](https://assets.leetcode.com/uploads/2024/05/19/lshift.jpg)

	- **Odd-indexed** rows (1, 3, 5, ...) are cyclically shifted to the right.

![](https://assets.leetcode.com/uploads/2024/05/19/rshift-stlone.jpg)

Return `true` if the final modified matrix after `k` steps is identical to the original matrix, and `false` otherwise.

 

Example 1:**

**Input:** mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4

**Output:** false

**Explanation:**

In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).

![](https://assets.leetcode.com/uploads/2024/05/19/t1-2.jpg)

Example 2:**

**Input:** mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2

**Output:** true

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/05/19/t1-3.jpg)

Example 3:**

**Input:** mat = [[2,2],[2,2]], k = 3

**Output:** true

**Explanation:**

As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.

 

**Constraints:**

	- `1 <= mat.length <= 25`

	- `1 <= mat[i].length <= 25`

	- `1 <= mat[i][j] <= 25`

	- `1 <= k <= 50`

## 🧠 Solution Explanation

**Intuition**
The solution checks if the final modified matrix after `k` steps is identical to the original matrix by comparing each element in the original matrix with the corresponding element in the modified matrix. The key insight is that the cyclic shifts can be simulated by adding or subtracting the shift amount `k` to the column index, taking into account whether the row index is even or odd.

**Approach**
1. Initialize variables `n` and `m` to store the number of rows and columns in the matrix, respectively.
2. Iterate over each row `i` in the matrix.
3. For each row `i`, iterate over each column `j`.
4. If `i` is even, check if the element at `(i, j)` in the original matrix is equal to the element at `(i, (j + k) % m)` in the modified matrix. If not, return `False`.
5. If `i` is odd, check if the element at `(i, j)` in the original matrix is equal to the element at `(i, (j - k) % m)` in the modified matrix. If not, return `False`.
6. If all elements match, return `True`.

**Time Complexity**
O(n*m), where n is the number of rows and m is the number of columns in the matrix. This is because we iterate over each element in the matrix once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the variables `n`, `m`, and `k`.

**Key Insight**
The key insight is that we can simulate the cyclic shifts by adding or subtracting `k` to the column index, taking into account whether the row index is even or odd. This allows us to avoid actually performing the shifts and instead just compare the elements directly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 9 ms (Beats 11.33%) |
| 💾 Memory | 19.2 MB (Beats 96.89%) |
| 📅 Solved | 2026-04-12 |
| 💻 Language | Python |