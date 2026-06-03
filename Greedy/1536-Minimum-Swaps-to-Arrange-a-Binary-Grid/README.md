> 📌 **Cross-listed:** Primary location is [Array/1536-Minimum-Swaps-to-Arrange-a-Binary-Grid](../../Array/1536-Minimum-Swaps-to-Arrange-a-Binary-Grid). This problem also appears under: **Array**, **Greedy**, **Matrix**

# 1536. Minimum Swaps to Arrange a Binary Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/)


## 📝 Problem Description

Given an `n x n` binary `grid`, in one step you can choose two **adjacent rows** of the grid and swap them.

A grid is said to be **valid** if all the cells above the main diagonal are **zeros**.

Return *the minimum number of steps* needed to make the grid valid, or **-1** if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell `(1, 1)` and ends at cell `(n, n)`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/07/28/fw.jpg)
```

**Input:** grid = [[0,0,1],[1,1,0],[1,0,0]]
**Output:** 3

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/07/16/e2.jpg)
```

**Input:** grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
**Output:** -1
**Explanation:** All rows are similar, swaps have no effect on the grid.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2020/07/16/e3.jpg)
```

**Input:** grid = [[1,0,0],[1,1,0],[1,1,1]]
**Output:** 0

```

 

**Constraints:**

	- `n == grid.length` `== grid[i].length`

	- `1 <= n <= 200`

	- `grid[i][j]` is either `0` or `1`

## 🧠 Solution Explanation

**Intuition**
The solution works by treating each row as a sequence of trailing zeros and ones, and then greedily selecting the row with the most trailing zeros to fill in the current position. This approach is based on the observation that the minimum number of swaps required to make the grid valid is equivalent to the minimum number of rows that need to be swapped to make all cells above the main diagonal zeros.

**Approach**
1. Convert each row into a sequence of trailing zeros and ones by iterating over the columns in reverse order.
2. Initialize a variable `ans` to store the minimum number of swaps required.
3. Iterate over each row in the grid. For each row, find the first row with enough trailing zeros (i.e., `v <= k`) and increment `ans` by the index of this row. Remove the value from the `row` list to avoid duplicates.
4. If no such row is found, return -1, indicating that the grid cannot be made valid.
5. Repeat step 3 until all rows have been processed.

**Time Complexity**
O(n^2), where n is the number of rows in the grid. This is because we iterate over each row and column in the grid once.

**Space Complexity**
O(n), where n is the number of rows in the grid. This is because we store the sequence of trailing zeros and ones for each row in the `row` list.

**Key Insight**
The key insight behind this solution is that the minimum number of swaps required to make the grid valid is equivalent to the minimum number of rows that need to be swapped to make all cells above the main diagonal zeros. By treating each row as a sequence of trailing zeros and ones, we can greedily select the row with the most trailing zeros to fill in the current position, resulting in the minimum number of swaps required.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1 ms (Beats 97.81%) |
| 💾 Memory | 20.9 MB (Beats 20.18%) |
| 📅 Solved | 2026-03-02 |
| 💻 Language | Python |