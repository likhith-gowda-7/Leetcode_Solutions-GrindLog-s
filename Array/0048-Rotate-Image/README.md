# 48. Rotate Image


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotate-image/)


## 📝 Problem Description

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)
```

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [[7,4,1],[8,5,2],[9,6,3]]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)
```

**Input:** matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
**Output:** [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

```

 

**Constraints:**

	- `n == matrix.length == matrix[i].length`

	- `1 <= n <= 20`

	- `-1000 <= matrix[i][j] <= 1000`

## 🧠 Solution Explanation

## Intuition
The approach to rotating the image by 90 degrees clockwise involves a two-step process: transposing the matrix and then reversing each row. This works because transposing the matrix effectively swaps the rows and columns, and then reversing each row achieves the desired rotation.

## Approach
1. Calculate the size of the matrix (`n`).
2. Iterate over the upper triangular part of the matrix, swapping elements to transpose the matrix.
3. Reverse each row of the transposed matrix to achieve the 90-degree clockwise rotation.

## Time Complexity
The time complexity is O(n^2), where n is the size of the matrix. This is because we are iterating over each element in the matrix once to transpose it and then again to reverse each row.

## Space Complexity
The space complexity is O(1), as we are modifying the input matrix in-place and not using any additional space that scales with the input size.

## Key Insight
The key insight here is that a 90-degree clockwise rotation can be achieved by first transposing the matrix (swapping rows and columns) and then reversing each row. This allows us to perform the rotation in-place, without needing to allocate additional space for the rotated matrix.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 69.19%) |
| 📅 Solved | 2026-05-04 |
| 💻 Language | Python |