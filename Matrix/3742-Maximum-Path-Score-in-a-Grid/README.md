> 📌 **Cross-listed:** Primary location is [Array/3742-Maximum-Path-Score-in-a-Grid](../../Array/3742-Maximum-Path-Score-in-a-Grid). This problem also appears under: **Array**, **Dynamic Programming**, **Matrix**

# 3742. Maximum Path Score in a Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-path-score-in-a-grid/)


## 📝 Problem Description

You are given an `m x n` grid where each cell contains one of the values 0, 1, or 2. You are also given an integer `k`.

You start from the top-left corner `(0, 0)` and want to reach the bottom-right corner `(m - 1, n - 1)` by moving only **right** or **down**.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

	- 0: adds 0 to your score and costs 0.

	- 1: adds 1 to your score and costs 1.

	- 2: adds 2 to your score and costs 1. ​​​​​​​

Return the **maximum** score achievable without exceeding a total cost of `k`, or -1 if no valid path exists.

**Note:** If you reach the last cell but the total cost exceeds `k`, the path is invalid.

 

Example 1:**

**Input:** grid = [[0, 1],[2, 0]], k = 1

**Output:** 2

**Explanation:**​​​​​​​

The optimal path is:

	
		
			Cell
			grid[i][j]
			Score
			Total

			Score
			Cost
			Total

			Cost
		
	
	
		
			(0, 0)
			0
			0
			0
			0
			0
		
		
			(1, 0)
			2
			2
			2
			1
			1
		
		
			(1, 1)
			0
			0
			2
			0
			1
		
	

Thus, the maximum possible score is 2.

Example 2:**

**Input:** grid = [[0, 1],[1, 2]], k = 1

**Output:** -1

**Explanation:**

There is no path that reaches cell `(1, 1)`​​​​​​​ without exceeding cost k. Thus, the answer is -1.

 

**Constraints:**

	- `1 <= m, n <= 200`

	- `0 <= k <= 10^3​​​​​​​`

	- `^​​​​​​​grid[0][0] == 0`

	- `0 <= grid[i][j] <= 2`

## 🧠 Solution Explanation

**Intuition**
This problem can be solved using dynamic programming by building a 2D table that stores the maximum score achievable for each cell and cost. The key insight is to iterate from the bottom-right corner to the top-left corner, considering the maximum score achievable from the cell below and the cell to the right, while keeping track of the total cost.

**Approach**
1. Initialize a 2D table `dp` of size `(n+1) x (k+1)` with all elements set to `-1`, where `n` is the number of columns in the grid and `k` is the maximum cost.
2. Iterate from the bottom-right corner to the top-left corner of the grid.
3. For each cell `(i, j)`, iterate from the maximum cost `k` down to 0.
4. For each cost `cost`, calculate the value `val` of the current cell in the grid.
5. Calculate the difference `diff` between the cost and the value of the current cell.
6. If the difference is less than or equal to the maximum cost, calculate the maximum score achievable from the cell below and the cell to the right, and update the value of the current cell in the `curr` table.
7. Update the `dp` table with the `curr` table.
8. Return the value of the top-left cell in the `dp` table.

**Time Complexity**
O(m*n*k), where m is the number of rows in the grid and n is the number of columns. This is because we iterate over each cell in the grid and each possible cost.

**Space Complexity**
O(m*n), where m is the number of rows in the grid and n is the number of columns. This is because we need to store the 2D table `dp` of size `(n+1) x (k+1)`.

**Key Insight**
The key insight is to iterate from the bottom-right corner to the top-left corner, considering the maximum score achievable from the cell below and the cell to the right, while keeping track of the total cost. This allows us to efficiently build the 2D table `dp` that stores the maximum score achievable for each cell and cost.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 13965 ms (Beats 6.98%) |
| 💾 Memory | 22.7 MB (Beats 88.62%) |
| 📅 Solved | 2026-04-30 |
| 💻 Language | Python |