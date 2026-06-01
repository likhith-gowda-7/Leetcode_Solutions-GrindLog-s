> 📌 **Cross-listed:** Primary location is [Array/2033-Minimum-Operations-to-Make-a-Uni-Value-Grid](../../Array/2033-Minimum-Operations-to-Make-a-Uni-Value-Grid). This problem also appears under: **Array**, **Math**, **Sorting**, **Matrix**

# 2033. Minimum Operations to Make a Uni-Value Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/)


## 📝 Problem Description

You are given a 2D integer `grid` of size `m x n` and an integer `x`. In one operation, you can **add** `x` to or **subtract** `x` from any element in the `grid`.

A **uni-value grid** is a grid where all the elements of it are equal.

Return *the **minimum** number of operations to make the grid **uni-value***. If it is not possible, return `-1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/09/21/gridtxt.png)
```

**Input:** grid = [[2,4],[6,8]], x = 2
**Output:** 4
**Explanation:** We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/09/21/gridtxt-1.png)
```

**Input:** grid = [[1,5],[2,3]], x = 1
**Output:** 5
**Explanation:** We can make every element equal to 3.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/09/21/gridtxt-2.png)
```

**Input:** grid = [[1,2],[3,4]], x = 2
**Output:** -1
**Explanation:** It is impossible to make every element equal.

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 10^5`

	- `1 <= m * n <= 10^5`

	- `1 <= x, grid[i][j] <= 10^4`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 147 ms (Beats 54.49%) |
| 💾 Memory | 41.1 MB (Beats 39.18%) |
| 📅 Solved | 2026-04-28 |
| 💻 Language | Python |