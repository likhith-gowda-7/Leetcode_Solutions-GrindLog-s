# 1301. Number of Paths with Max Score


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-paths-with-max-score/)


## 📝 Problem Description

You are given a square `board` of characters. You can move on the board starting at the bottom right square marked with the character `'S'`.



You need to reach the top left square marked with the character `'E'`. The rest of the squares are labeled either with a numeric character `1, 2, ..., 9` or with an obstacle `'X'`. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.



Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, **taken modulo `10^9 + 7`**.



In case there is no path, return `[0, 0]`.



 


Example 1:**


```
**Input:** board = ["E23","2X2","12S"]
**Output:** [7,1]

```
Example 2:**


```
**Input:** board = ["E12","1X1","21S"]
**Output:** [4,2]

```
Example 3:**


```
**Input:** board = ["E11","XXX","11S"]
**Output:** [0,0]

```

 


**Constraints:**




	- `2 <= board.length == board[i].length <= 100`

## 🧠 Solution Explanation

**Intuition**
This solution uses dynamic programming to find the maximum sum of numeric characters and the number of paths to reach the top-left square from the bottom-right square. The key insight is to break down the problem into smaller sub-problems by considering the maximum sum and number of paths that can be obtained by moving up, left, or diagonally from each cell.

**Approach**
1. Initialize two arrays `max_score` and `no_of_ways` of size `n+1` to store the maximum sum and number of paths for each cell, respectively.
2. Iterate over the board from bottom to top, row by row.
3. For each cell, calculate the maximum sum and number of paths by considering the maximum sum and number of paths that can be obtained by moving up, left, or diagonally from the cell.
4. Update the `max_score` and `no_of_ways` arrays with the calculated values.
5. After iterating over the entire board, return the maximum sum and number of paths for the top-left cell.

**Time Complexity**
O(n^2), where n is the size of the board. This is because we need to iterate over each cell in the board twice: once to calculate the maximum sum and number of paths for each cell, and once to update the `max_score` and `no_of_ways` arrays.

**Space Complexity**
O(n^2), where n is the size of the board. This is because we need to store the `max_score` and `no_of_ways` arrays of size n+1.

**Key Insight**
The key insight is to break down the problem into smaller sub-problems by considering the maximum sum and number of paths that can be obtained by moving up, left, or diagonally from each cell. This allows us to use dynamic programming to efficiently calculate the maximum sum and number of paths for each cell.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 68 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 98.23%) |
| 📅 Solved | 2026-07-05 |
| 💻 Language | Python |