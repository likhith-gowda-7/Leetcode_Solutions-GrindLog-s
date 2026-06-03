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

## 🧠 Solution Explanation

**Intuition**
This solution uses a union-find data structure to group connected `1`s in the grid into separate islands. It then iterates over all `0`s in the grid, considering each one as a potential new island. For each `0`, it calculates the size of the new island by adding the size of the current island to the sizes of all adjacent islands. The maximum size of all new islands is the answer.

**Approach**
1. Initialize a union-find data structure with `n*n` nodes, where `n` is the size of the grid. Each node represents a cell in the grid.
2. Iterate over the grid, and for each `1`, perform a union operation with all adjacent `1`s. This groups connected `1`s into separate islands.
3. Store the size of each island in a dictionary `root_to_size`.
4. Iterate over all `0`s in the grid, and for each one, calculate the size of the new island by adding the size of the current island to the sizes of all adjacent islands.
5. Update the maximum size of all new islands.

**Time Complexity**
The time complexity of this solution is O(n^2), where n is the size of the grid. This is because we iterate over the grid twice: once to group connected `1`s into islands, and once to calculate the size of new islands for each `0`.

**Space Complexity**
The space complexity of this solution is O(n^2), where n is the size of the grid. This is because we store the union-find data structure and the `root_to_size` dictionary, which require O(n^2) space.

**Key Insight**
The key insight behind this solution is that we can calculate the size of new islands by adding the size of the current island to the sizes of all adjacent islands. This is possible because the union-find data structure allows us to efficiently group connected `1`s into separate islands.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1565 ms (Beats 8.23%) |
| 💾 Memory | 90.4 MB (Beats 5.19%) |
| 📅 Solved | 2025-09-28 |
| 💻 Language | Python |