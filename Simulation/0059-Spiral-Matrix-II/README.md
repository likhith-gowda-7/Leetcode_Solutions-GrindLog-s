> 📌 **Cross-listed:** Primary location is [Array/0059-Spiral-Matrix-II](../../Array/0059-Spiral-Matrix-II). This problem also appears under: **Array**, **Matrix**, **Simulation**

# 59. Spiral Matrix II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/spiral-matrix-ii/)


## 📝 Problem Description

Given a positive integer `n`, generate an `n x n` `matrix` filled with elements from `1` to `n^2` in spiral order.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg)
```

**Input:** n = 3
**Output:** [[1,2,3],[8,9,4],[7,6,5]]

```

Example 2:**

```

**Input:** n = 1
**Output:** [[1]]

```

 

**Constraints:**

	- `1 <= n <= 20`

## 🧠 Solution Explanation

## Intuition
The solution works by simulating the process of filling a matrix in spiral order, starting from the top-left corner and moving clockwise. It uses four pointers (left, right, top, bottom) to keep track of the current boundaries of the matrix. The spiral pattern is achieved by iterating over the elements in a specific order, first from left to right, then from top to bottom, then from right to left, and finally from bottom to top.

## Approach
1. Initialize an `n x n` matrix with zeros and set up the four pointers (left, right, top, bottom) to their initial positions.
2. Iterate over the elements in the matrix in spiral order, filling in the values from 1 to `n^2`.
3. In each iteration, fill in the elements in the top row from left to right, then the elements in the right column from top to bottom, then the elements in the bottom row from right to left, and finally the elements in the left column from bottom to top.
4. After each iteration, update the pointers to move the boundaries of the matrix inward.

## Time Complexity
The time complexity is O(n^2), where n is the size of the matrix. This is because we are filling in `n^2` elements in the matrix, and each element is visited once.

## Space Complexity
The space complexity is O(n^2), where n is the size of the matrix. This is because we need to store the `n x n` matrix in memory.

## Key Insight
The key insight behind this solution is the use of the four pointers (left, right, top, bottom) to keep track of the current boundaries of the matrix, allowing us to iterate over the elements in spiral order and fill in the values correctly. This approach ensures that we visit each element exactly once and fill in the values in the correct order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-01-13 |
| 💻 Language | Python |