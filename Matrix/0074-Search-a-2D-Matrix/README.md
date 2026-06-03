> 📌 **Cross-listed:** Primary location is [Array/0074-Search-a-2D-Matrix](../../Array/0074-Search-a-2D-Matrix). This problem also appears under: **Array**, **Binary Search**, **Matrix**

# 74. Search a 2D Matrix


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/search-a-2d-matrix/)


## 📝 Problem Description

You are given an `m x n` integer matrix `matrix` with the following two properties:

	- Each row is sorted in non-decreasing order.

	- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.

You must write a solution in `O(log(m * n))` time complexity.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)
```

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
**Output:** true

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)
```

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
**Output:** false

```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 100`

	- `-10^4 <= matrix[i][j], target <= 10^4`

## 🧠 Solution Explanation

## Intuition
This solution works by treating the 2D matrix as a single sorted array, leveraging the given properties of the matrix to perform a binary search. The key idea is to first find the row where the target element could potentially be, and then perform another binary search within that row to find the target.

## Approach
1. Determine the number of rows (`m`) and columns (`n`) in the matrix.
2. Perform a binary search across the rows to find the row where the target element could be, based on the first and last elements of each row.
3. Once the correct row is identified, perform another binary search within that row to find the target element.
4. If the target element is found during the second binary search, return `True`; otherwise, return `False`.

## Time Complexity
The time complexity is O(log(m * n)), which can be broken down into two parts: O(log(m)) for the row search and O(log(n)) for the column search. This is because we are essentially performing two binary searches in sequence.

## Space Complexity
The space complexity is O(1), as we are only using a constant amount of space to store the row and column indices, regardless of the size of the input matrix.

## Key Insight
The crucial insight here is recognizing that the matrix can be treated as a single sorted array, allowing us to apply binary search techniques to find the target element efficiently. By first identifying the correct row and then searching within that row, we can take advantage of the matrix's sorted properties to achieve the required time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.2 MB (Beats 100%) |
| 📅 Solved | 2025-02-23 |
| 💻 Language | Python |