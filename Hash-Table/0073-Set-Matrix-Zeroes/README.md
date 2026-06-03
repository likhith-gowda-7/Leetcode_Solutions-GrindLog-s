> 📌 **Cross-listed:** Primary location is [Array/0073-Set-Matrix-Zeroes](../../Array/0073-Set-Matrix-Zeroes). This problem also appears under: **Array**, **Hash Table**, **Matrix**

# 73. Set Matrix Zeroes


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)


## 📝 Problem Description

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)
```

**Input:** matrix = [[1,1,1],[1,0,1],[1,1,1]]
**Output:** [[1,0,1],[0,0,0],[1,0,1]]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)
```

**Input:** matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
**Output:** [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[0].length`

	- `1 <= m, n <= 200`

	- `-2^31 <= matrix[i][j] <= 2^31 - 1`

 

**Follow up:**

	- A straightforward solution using `O(mn)` space is probably a bad idea.

	- A simple improvement uses `O(m + n)` space, but still not the best solution.

	- Could you devise a constant space solution?

## 🧠 Solution Explanation

## Intuition
This approach works by first identifying the rows and columns that need to be zeroed out, and then iterating over the matrix again to set the corresponding elements to zero. The use of sets to store the rows and columns with zeros allows for efficient lookups.

## Approach
1. Initialize two sets, `row_zeros` and `col_zeros`, to store the indices of rows and columns that contain zeros.
2. Iterate over the matrix to find the rows and columns with zeros and add their indices to the respective sets.
3. Iterate over the matrix again, and for each element, check if its row or column index is in the `row_zeros` or `col_zeros` set. If it is, set the element to zero.

## Time Complexity
The time complexity is O(mn), where m is the number of rows and n is the number of columns in the matrix. This is because we are iterating over the matrix twice: once to find the rows and columns with zeros, and again to set the corresponding elements to zero.

## Space Complexity
The space complexity is O(m + n), where m is the number of rows and n is the number of columns in the matrix. This is because in the worst-case scenario, we might need to store all row and column indices in the `row_zeros` and `col_zeros` sets.

## Key Insight
The key insight here is to use sets to store the rows and columns with zeros, which allows for efficient lookups and avoids the need to use extra space that scales with the size of the matrix. This approach enables us to solve the problem in-place, as required.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 91.33%) |
| 💾 Memory | 20.4 MB (Beats 36.82%) |
| 📅 Solved | 2026-05-16 |
| 💻 Language | Python |