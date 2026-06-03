# 120. Triangle


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/triangle/)


## 📝 Problem Description

Given a `triangle` array, return *the minimum path sum from top to bottom*.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

 

Example 1:**

```

**Input:** triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
**Output:** 11
**Explanation:** The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

```

Example 2:**

```

**Input:** triangle = [[-10]]
**Output:** -10

```

 

**Constraints:**

	- `1 <= triangle.length <= 200`

	- `triangle[0].length == 1`

	- `triangle[i].length == triangle[i - 1].length + 1`

	- `-10^4 <= triangle[i][j] <= 10^4`

 

**Follow up:** Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?

## 🧠 Solution Explanation

## Intuition
This approach works by utilizing dynamic programming to build up a solution from the bottom of the triangle to the top. By starting from the second-to-last row and working backwards, we can calculate the minimum path sum for each element in the triangle. This method takes advantage of the fact that the minimum path sum for each element is determined by the minimum path sums of its children in the row below.

## Approach
1. Initialize the number of rows in the triangle (`n`).
2. Iterate over each row in the triangle from the second-to-last row to the first row (in reverse order).
3. For each element in the current row, calculate the minimum path sum by adding the element's value to the minimum of its two children in the row below.
4. Update the element's value with the calculated minimum path sum.
5. After iterating over all rows, the minimum path sum from top to bottom is stored in the first element of the first row.

## Time Complexity
The time complexity is O(n^2), where n is the number of rows in the triangle. This is because we are iterating over each element in the triangle once, and the number of elements in the triangle is proportional to the square of the number of rows.

## Space Complexity
The space complexity is O(1), because we are modifying the input triangle in-place and not using any additional space that scales with the input size.

## Key Insight
The key insight behind this solution is that we can calculate the minimum path sum for each element in the triangle by working backwards from the bottom row, using the minimum path sums of its children to determine its own minimum path sum. This allows us to avoid recalculating the same subproblems multiple times and reduces the time complexity to O(n^2).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 100%) |
| 📅 Solved | 2025-11-08 |
| 💻 Language | Python |