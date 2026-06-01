> 📌 **Cross-listed:** Primary location is [Array/0827-Making-A-Large-Island](../../Array/0827-Making-A-Large-Island). This problem also appears under: **Array**, **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Matrix**

# 827. Making A Large Island


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/making-a-large-island/)


## 📝 Problem Description

You are given an `n x n` binary matrix `grid`. You are allowed to change **at most one** `0` to be `1`.

Return *the size of the largest **island** in* `grid` *after applying this operation*.

An **island** is a 4-directionally connected group of `1`s.

 

Example 1:**

```

**Input:** grid = [[1,0],[0,1]]
**Output:** 3
**Explanation:** Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

```

Example 2:**

```

**Input:** grid = [[1,1],[1,0]]
**Output:** 4
**Explanation: **Change the 0 to 1 and make the island bigger, only one island with area = 4.
```

Example 3:**

```

**Input:** grid = [[1,1],[1,1]]
**Output:** 4
**Explanation:** Can't change any 0 to 1, only one island with area = 4.

```

 

**Constraints:**

	- `n == grid.length`

	- `n == grid[i].length`

	- `1 <= n <= 500`

	- `grid[i][j]` is either `0` or `1`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1565 ms (Beats 8.23%) |
| 💾 Memory | 90.4 MB (Beats 5.19%) |
| 📅 Solved | 2025-09-28 |
| 💻 Language | Python |