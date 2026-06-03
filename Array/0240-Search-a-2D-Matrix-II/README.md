# 240. Search a 2D Matrix II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/)


## 📝 Problem Description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

	- Integers in each row are sorted in ascending from left to right.

	- Integers in each column are sorted in ascending from top to bottom.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)
```

**Input:** matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg)
```

**Input:** matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
**Output:** false

```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= n, m <= 300`

	- `-10^9 <= matrix[i][j] <= 10^9`

	- All the integers in each row are **sorted** in ascending order.

	- All the integers in each column are **sorted** in ascending order.

	- `-10^9 <= target <= 10^9`

## 🧠 Solution Explanation

## Intuition
This approach works by taking advantage of the fact that the matrix is sorted both row-wise and column-wise. By starting from the top-right corner, we can effectively use a combination of row and column comparisons to narrow down the search space. This allows us to efficiently search for the target value in the matrix.

## Approach
1. Initialize the row index to 0 (top row) and the column index to the last column (rightmost column).
2. Compare the value at the current row and column index with the target value.
3. If the values match, return True.
4. If the current value is greater than the target, move left in the current row by decrementing the column index.
5. If the current value is less than the target, move down in the current column by incrementing the row index.
6. Repeat steps 2-5 until the target is found or the search space is exhausted.

## Time Complexity
The time complexity is O(m + n), where m is the number of rows and n is the number of columns. This is because in the worst-case scenario, we might need to traverse the entire matrix, either by moving down all rows or left across all columns.

## Space Complexity
The space complexity is O(1), as we only use a constant amount of space to store the row and column indices, regardless of the size of the input matrix.

## Key Insight
The key insight here is to start from the top-right corner and use a combination of row and column comparisons to efficiently search for the target value. This approach allows us to take advantage of the sorted nature of the matrix, reducing the search space and resulting in a more efficient algorithm.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 145 ms (Beats 41.7%) |
| 💾 Memory | 23.5 MB (Beats 100%) |
| 📅 Solved | 2025-12-21 |
| 💻 Language | Python |