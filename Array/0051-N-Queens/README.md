# 51. N-Queens


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/n-queens/)


## 📝 Problem Description

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
```

**Input:** n = 4
**Output:** [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
**Explanation:** There exist two distinct solutions to the 4-queens puzzle as shown above

```

Example 2:**

```

**Input:** n = 1
**Output:** [["Q"]]

```

 

**Constraints:**

	- `1 <= n <= 9`

## 🧠 Solution Explanation

## Intuition
The N-Queens problem can be solved using a backtracking approach, where we try to place a queen in each column of the current row and recursively check if the placement is valid. This approach works because it allows us to explore all possible configurations of the board. We use additional data structures to keep track of the columns and diagonals that are under attack by a queen.

## Approach
1. Initialize an empty board and data structures to keep track of used columns and diagonals.
2. Define a recursive function `backtrack` that takes the current row and the board as input.
3. In the `backtrack` function, iterate over each column in the current row and check if the placement of a queen is valid by checking the used columns and diagonals.
4. If the placement is valid, mark the column and diagonals as used, place the queen on the board, and recursively call the `backtrack` function for the next row.
5. If the recursive call returns, reset the board and the used columns and diagonals to their previous state (backtracking).

## Time Complexity
The time complexity is O(N!), where N is the number of queens. This is because in the worst case, we have to try all possible configurations of the board, which is N! (N factorial).

## Space Complexity
The space complexity is O(N), where N is the number of queens. This is because we need to store the board and the used columns and diagonals, which requires O(N) space.

## Key Insight
The key insight to this solution is the use of additional data structures to keep track of the columns and diagonals that are under attack by a queen, which allows us to efficiently check if a placement is valid and avoid unnecessary recursive calls. This optimization is crucial to solving the problem within a reasonable time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 6 ms (Beats 97.56%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-08-01 |
| 💻 Language | Python |