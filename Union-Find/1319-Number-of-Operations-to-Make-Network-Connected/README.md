> 📌 **Cross-listed:** Primary location is [Depth-First Search/1319-Number-of-Operations-to-Make-Network-Connected](../../Depth-First-Search/1319-Number-of-Operations-to-Make-Network-Connected). This problem also appears under: **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Graph Theory**

# 1319. Number of Operations to Make Network Connected


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)


## 📝 Problem Description

There are `n` computers numbered from `0` to `n - 1` connected by ethernet cables `connections` forming a network where `connections[i] = [a_i, b_i]` represents a connection between computers `a_i` and `b_i`. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network `connections`. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return *the minimum number of times you need to do this in order to make all the computers connected*. If it is not possible, return `-1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/01/02/sample_1_1677.png)
```

**Input:** n = 4, connections = [[0,1],[0,2],[1,2]]
**Output:** 1
**Explanation:** Remove cable between computer 1 and 2 and place between computers 1 and 3.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/01/02/sample_2_1677.png)
```

**Input:** n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
**Output:** 2

```

Example 3:**

```

**Input:** n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
**Output:** -1
**Explanation:** There are not enough cables.

```

 

**Constraints:**

	- `1 <= n <= 10^5`

	- `1 <= connections.length <= min(n * (n - 1) / 2, 10^5)`

	- `connections[i].length == 2`

	- `0 <= a_i, b_i < n`

	- `a_i != b_i`

	- There are no repeated connections.

	- No two computers are connected by more than one cable.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 33 ms (Beats 74.25%) |
| 💾 Memory | 32.3 MB (Beats 99.92%) |
| 📅 Solved | 2025-09-19 |
| 💻 Language | Python |