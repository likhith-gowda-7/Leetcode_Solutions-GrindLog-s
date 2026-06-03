# 52. N-Queens II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/n-queens-ii/)


## 📝 Problem Description

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *the number of distinct solutions to the **n-queens puzzle***.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
```

**Input:** n = 4
**Output:** 2
**Explanation:** There are two distinct solutions to the 4-queens puzzle as shown.

```

Example 2:**

```

**Input:** n = 1
**Output:** 1

```

 

**Constraints:**

	- `1 <= n <= 9`

## 🧠 Solution Explanation

**Intuition**
The solution uses backtracking to explore all possible configurations of queens on the board. The key insight is to track the diagonals and used columns to efficiently prune branches that lead to invalid configurations.

**Approach**
1. Initialize a boolean array `diagonal` of size `2n` to track the diagonals, a boolean array `anti_diagonal` of size `2n` to track the anti-diagonals, and a boolean array `used_col` of size `n` to track the used columns.
2. Define a recursive function `backtracking` that takes the current row as input.
3. If the current row is equal to `n`, increment the count of distinct solutions.
4. Iterate over each column in the current row, and for each column:
   a. Calculate the diagonal and anti-diagonal indices.
   b. Check if the column is not used and the diagonals are not attacked.
   c. If the column is valid, mark it as used, update the diagonals, and recursively call `backtracking` for the next row.
   d. After the recursive call, undo the changes to backtrack and explore other branches.
5. Call `backtracking` with the initial row index 0.

**Time Complexity**
O(n!) due to the exponential number of possible configurations, where `n` is the size of the board.

**Space Complexity**
O(n) for the boolean arrays `diagonal`, `anti_diagonal`, and `used_col`.

**Key Insight**
The solution's efficiency relies on the clever use of boolean arrays to track the diagonals and used columns, which allows it to prune branches that lead to invalid configurations, reducing the search space from O(n!) to O(n!).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 97.67%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-08-02 |
| 💻 Language | Python |