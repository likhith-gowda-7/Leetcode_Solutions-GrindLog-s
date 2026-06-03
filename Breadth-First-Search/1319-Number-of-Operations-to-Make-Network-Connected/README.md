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

## 🧠 Solution Explanation

**Intuition**
The solution uses a Union-Find approach to find the minimum number of cables to extract and reconnect to make all computers connected. The idea is to first check if it's possible to make all computers connected, and then use the Union-Find algorithm to find the minimum number of cables to extract and reconnect.

**Approach**
1. Check if it's possible to make all computers connected by comparing the number of connections to the number of computers minus one (n-1).
2. Initialize the parent array and size array for the Union-Find algorithm.
3. Define the find function to find the root of a node in the Union-Find tree.
4. Define the union function to merge two nodes in the Union-Find tree and update the size array.
5. Iterate through the connections and use the union function to merge connected nodes.
6. Count the number of connected components and the number of extra cables.
7. Calculate the minimum number of cables to extract and reconnect.

**Time Complexity**
O(n + m), where n is the number of computers and m is the number of connections. The Union-Find algorithm has a time complexity of O(n + m) for the find and union operations.

**Space Complexity**
O(n), where n is the number of computers. The parent and size arrays have a space complexity of O(n).

**Key Insight**
The key insight is that the Union-Find algorithm can be used to find the minimum number of cables to extract and reconnect to make all computers connected. By counting the number of connected components and the number of extra cables, we can calculate the minimum number of cables to extract and reconnect.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 33 ms (Beats 74.25%) |
| 💾 Memory | 32.3 MB (Beats 99.92%) |
| 📅 Solved | 2025-09-19 |
| 💻 Language | Python |