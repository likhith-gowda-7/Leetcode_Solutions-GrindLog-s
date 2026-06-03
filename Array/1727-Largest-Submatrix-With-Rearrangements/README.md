# 1727. Largest Submatrix With Rearrangements


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/largest-submatrix-with-rearrangements/)


## 📝 Problem Description

You are given a binary matrix `matrix` of size `m x n`, and you are allowed to rearrange the **columns** of the `matrix` in any order.

Return *the area of the largest submatrix within *`matrix`* where **every** element of the submatrix is *`1`* after reordering the columns optimally.*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40536-pm.png)
```

**Input:** matrix = [[0,0,1],[1,1,1],[1,0,1]]
**Output:** 4
**Explanation:** You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40852-pm.png)
```

**Input:** matrix = [[1,0,1,0,1]]
**Output:** 3
**Explanation:** You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.

```

Example 3:**

```

**Input:** matrix = [[1,1,0],[1,0,1]]
**Output:** 2
**Explanation:** Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.

```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m * n <= 10^5`

	- `matrix[i][j]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution works by first rearranging the columns of the binary matrix to maximize the height of each column of 1s. This is done by adding the height of each column to the next column, effectively "carrying over" the height of the previous column. Then, for each row, the columns are sorted in descending order, and the area of the largest rectangle that can be formed by the current row is calculated.

**Approach**
1. Initialize variables to store the maximum area `res` and the dimensions of the matrix `m` and `n`.
2. Iterate over each row in the matrix, starting from the second row.
3. For each column in the current row, if the value is 1, add the height of the previous row's column to the current column's height.
4. Iterate over each row in the matrix again.
5. For each row, sort the columns in descending order.
6. For each column in the sorted row, calculate the area of the largest rectangle that can be formed by the current column and the previous columns.
7. Update the maximum area `res` if the calculated area is larger.

**Time Complexity**
O(m*n log n) due to the sorting step in the second iteration over the matrix. The first iteration has a time complexity of O(m*n) as we are iterating over each element in the matrix once.

**Space Complexity**
O(1) as we are only using a constant amount of space to store the maximum area and the dimensions of the matrix.

**Key Insight**
The key insight is that by rearranging the columns to maximize the height of each column of 1s, we can effectively transform the problem into finding the area of the largest rectangle in a histogram, which can be solved efficiently using a sorting-based approach.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 124 ms (Beats 75.07%) |
| 💾 Memory | 36.4 MB (Beats 41.78%) |
| 📅 Solved | 2026-03-17 |
| 💻 Language | Python |