> 📌 **Cross-listed:** Primary location is [Array/0994-Rotting-Oranges](../../Array/0994-Rotting-Oranges). This problem also appears under: **Array**, **Breadth-First Search**, **Matrix**

# 994. Rotting Oranges


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotting-oranges/)


## 📝 Problem Description

You are given an `m x n` `grid` where each cell can have one of three values:

	- `0` representing an empty cell,

	- `1` representing a fresh orange, or

	- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)
```

**Input:** grid = [[2,1,1],[1,1,0],[0,1,1]]
**Output:** 4

```

Example 2:**

```

**Input:** grid = [[2,1,1],[0,1,1],[1,0,1]]
**Output:** -1
**Explanation:** The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

```

Example 3:**

```

**Input:** grid = [[0,2]]
**Output:** 0
**Explanation:** Since there are already no fresh oranges at minute 0, the answer is just 0.

```

 

**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 10`

	- `grid[i][j]` is `0`, `1`, or `2`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a multi-source Breadth-First Search (BFS) approach to find the minimum number of minutes required for all fresh oranges to rot. The idea is to simulate the process of oranges rotting by exploring all possible directions (up, down, left, right) from each rotten orange.

**Approach**
1. Initialize a queue to store the coordinates of rotten oranges and a counter to store the number of fresh oranges.
2. Iterate through the grid to find all rotten oranges and add them to the queue. Also, update the grid by marking the rotten oranges as visited (0).
3. Define a helper function `add_item` to add fresh oranges adjacent to the current rotten orange to the queue and update the grid.
4. Perform a BFS traversal by iterating through the queue. For each rotten orange, add its adjacent fresh oranges to the queue and update the grid.
5. Increment the `min_time` counter after each BFS traversal.
6. If there are still fresh oranges left after the BFS traversal, return -1. Otherwise, return the `min_time` counter.

**Time Complexity**
O(m*n), where m and n are the dimensions of the grid. This is because we need to iterate through each cell in the grid to find all rotten oranges and perform the BFS traversal.

**Space Complexity**
O(m*n), where m and n are the dimensions of the grid. This is because we need to store the coordinates of all rotten oranges in the queue and the updated grid.

**Key Insight**
The key insight is to use a multi-source BFS approach to simulate the process of oranges rotting. By exploring all possible directions from each rotten orange, we can find the minimum number of minutes required for all fresh oranges to rot. The solution also handles the case where it's impossible for all fresh oranges to rot by returning -1.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 76.36%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-08-14 |
| 💻 Language | Python |