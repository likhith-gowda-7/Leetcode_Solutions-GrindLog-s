# 118. Pascal's Triangle


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/pascals-triangle/)


## 📝 Problem Description

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
 

Example 1:**

```
**Input:** numRows = 5
**Output:** [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

```
Example 2:**

```
**Input:** numRows = 1
**Output:** [[1]]

```

 

**Constraints:**

	- `1 <= numRows <= 30`

## 🧠 Solution Explanation

## Intuition
The solution works by iteratively generating each row of Pascal's triangle, using the previous row to calculate the next one. This approach takes advantage of the property of Pascal's triangle where each number is the sum of the two numbers directly above it. By starting with the first row and applying this rule, we can generate the entire triangle.

## Approach
1. Initialize the result with the first row of Pascal's triangle, which is `[1]`.
2. Define a helper function `pascal` that takes a row as input and returns the next row.
3. In the `pascal` function, calculate the next row by summing adjacent elements from the previous row and appending `1` at the beginning and end.
4. Repeat steps 2-3 for `numRows - 1` times, appending each new row to the result.

## Time Complexity
The time complexity is O(n^2), where n is the number of rows. This is because we are generating each row iteratively, and the number of elements in each row increases linearly with the row number.

## Space Complexity
The space complexity is O(n^2), where n is the number of rows. This is because we are storing all the rows in the result, and the total number of elements in the result is proportional to the sum of the first n natural numbers, which is n*(n+1)/2.

## Key Insight
The key insight behind this solution is the realization that each row of Pascal's triangle can be generated independently using only the previous row, allowing us to use a simple iterative approach to generate the entire triangle. This approach avoids the need for explicit recursive function calls, making it more efficient and easier to understand.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-08-01 |
| 💻 Language | Python |