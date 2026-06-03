# 304. Range Sum Query 2D - Immutable


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable/)


## 📝 Problem Description

Given a 2D matrix `matrix`, handle multiple queries of the following type:

	- Calculate the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

Implement the `NumMatrix` class:

	- `NumMatrix(int[][] matrix)` Initializes the object with the integer matrix `matrix`.

	- `int sumRegion(int row1, int col1, int row2, int col2)` Returns the **sum** of the elements of `matrix` inside the rectangle defined by its **upper left corner** `(row1, col1)` and **lower right corner** `(row2, col2)`.

You must design an algorithm where `sumRegion` works on `O(1)` time complexity.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg)
```

**Input**
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
**Output**
[null, 8, 11, 12]

**Explanation**
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 200`

	- `-10^4 <= matrix[i][j] <= 10^4`

	- `0 <= row1 <= row2 < m`

	- `0 <= col1 <= col2 < n`

	- At most `10^4` calls will be made to `sumRegion`.

## 🧠 Solution Explanation

## Intuition
The solution works by precomputing the prefix sum of the entire matrix, which allows for efficient calculation of the sum of any sub-rectangle. This approach takes advantage of the fact that the prefix sum at each cell can be calculated using the values of its neighboring cells. By storing the prefix sum in a separate matrix, we can quickly calculate the sum of any rectangle in constant time.

## Approach
1. Initialize a prefix sum matrix with an extra row and column to handle edge cases.
2. Iterate over each cell in the input matrix, calculating the prefix sum at each cell by adding the current cell's value to the prefix sums of the cells above and to the left, and subtracting the prefix sum of the cell above and to the left.
3. To calculate the sum of a rectangle, use the prefix sum values at the corners of the rectangle to compute the sum in constant time.

## Time Complexity
The time complexity of the `sumRegion` method is O(1), since it only involves a constant number of operations to calculate the sum of the rectangle. The time complexity of the `__init__` method is O(m*n), where m and n are the dimensions of the input matrix, since it needs to iterate over each cell in the matrix to precompute the prefix sum.

## Space Complexity
The space complexity is O(m*n), where m and n are the dimensions of the input matrix, since we need to store the prefix sum matrix.

## Key Insight
The key insight behind this solution is that the prefix sum of a rectangle can be calculated using the inclusion-exclusion principle, which allows us to compute the sum in constant time by using the prefix sum values at the corners of the rectangle. This enables us to efficiently handle multiple queries on the same matrix.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 107 ms (Beats 77.56%) |
| 💾 Memory | 30.8 MB (Beats 100%) |
| 📅 Solved | 2024-12-19 |
| 💻 Language | Python |