> 📌 **Cross-listed:** Primary location is [Array/2257-Count-Unguarded-Cells-in-the-Grid](../../Array/2257-Count-Unguarded-Cells-in-the-Grid). This problem also appears under: **Array**, **Matrix**, **Simulation**

# 2257. Count Unguarded Cells in the Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/)


## 📝 Problem Description

You are given two integers `m` and `n` representing a **0-indexed** `m x n` grid. You are also given two 2D integer arrays `guards` and `walls` where `guards[i] = [row_i, col_i]` and `walls[j] = [row_j, col_j]` represent the positions of the `i^th` guard and `j^th` wall respectively.

A guard can see **every** cell in the four cardinal directions (north, east, south, or west) starting from their position unless **obstructed** by a wall or another guard. A cell is **guarded** if there is **at least** one guard that can see it.

Return* the number of unoccupied cells that are **not** **guarded**.*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png)
```

**Input:** m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
**Output:** 7
**Explanation:** The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2022/03/10/example2drawio.png)
```

**Input:** m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
**Output:** 4
**Explanation:** The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.

```

 

**Constraints:**

	- `1 <= m, n <= 10^5`

	- `2 <= m * n <= 10^5`

	- `1 <= guards.length, walls.length <= 5 * 10^4`

	- `2 <= guards.length + walls.length <= m * n`

	- `guards[i].length == walls[j].length == 2`

	- `0 <= row_i, row_j < m`

	- `0 <= col_i, col_j < n`

	- All the positions in `guards` and `walls` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution uses a grid-based approach to simulate the guards' vision. It first initializes a grid with all cells marked as unguarded (0), then marks the walls (1) and guards (2) on the grid. The solution then iterates over each guard, simulating its vision in all four directions (up, down, left, right) and marking the cells it can see as guarded (3). Finally, it returns the count of unguarded cells.

**Approach**
1. Initialize a grid of size `m x n` with all cells marked as unguarded (0).
2. Mark the walls (1) and guards (2) on the grid.
3. Define a function `guards_vision(row, col)` to simulate a guard's vision from a given position.
4. Iterate over each guard and call `guards_vision(row, col)` to simulate its vision.
5. In `guards_vision(row, col)`, iterate over the four directions (up, down, left, right) and mark the cells that can be seen by the guard as guarded (3).
6. Return the count of unguarded cells.

**Time Complexity**
O(m*n), where m is the number of rows and n is the number of columns in the grid. This is because we iterate over each cell in the grid once to simulate the guards' vision.

**Space Complexity**
O(m*n), where m is the number of rows and n is the number of columns in the grid. This is because we need to store the grid with all cells marked as unguarded, walls, or guards.

**Key Insight**
The key insight is to use a grid-based approach to simulate the guards' vision, which allows us to efficiently mark the cells that can be seen by each guard. By iterating over each guard and simulating its vision, we can accurately count the number of unguarded cells.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 365 ms (Beats 45.5%) |
| 💾 Memory | 39.4 MB (Beats 100%) |
| 📅 Solved | 2025-11-07 |
| 💻 Language | Python |