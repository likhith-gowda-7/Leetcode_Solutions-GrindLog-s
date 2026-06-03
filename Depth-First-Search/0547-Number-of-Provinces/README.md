# 547. Number of Provinces


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-provinces/)


## 📝 Problem Description

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i^th` city and the `j^th` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return *the total number of **provinces***.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)
```

**Input:** isConnected = [[1,1,0],[1,1,0],[0,0,1]]
**Output:** 2

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)
```

**Input:** isConnected = [[1,0,0],[0,1,0],[0,0,1]]
**Output:** 3

```

 

**Constraints:**

	- `1 <= n <= 200`

	- `n == isConnected.length`

	- `n == isConnected[i].length`

	- `isConnected[i][j]` is `1` or `0`.

	- `isConnected[i][i] == 1`

	- `isConnected[i][j] == isConnected[j][i]`

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to traverse the graph represented by the `isConnected` matrix. The idea is to start from each unvisited node and explore all its connected nodes, effectively grouping them into a province. By counting the number of provinces, we can determine the total number of provinces in the graph.

**Approach**
1. Initialize a visited array to keep track of visited nodes.
2. Define a DFS function that takes a node as input and returns True if the node is connected to other nodes, False otherwise.
3. In the DFS function:
   1. Check if the node is visited; if so, return False.
   2. Mark the node as visited.
   3. Iterate through all nodes and check if they are connected to the current node.
   4. Recursively call the DFS function for each connected node.
4. Initialize a total counter to store the number of provinces.
5. Iterate through all nodes and call the DFS function for each unvisited node.
6. Increment the total counter for each province found.

**Time Complexity**
O(n^2) where n is the number of cities. In the worst case, we visit each node and check all its connections, resulting in a quadratic time complexity.

**Space Complexity**
O(n) where n is the number of cities. We use a visited array of size n to keep track of visited nodes.

**Key Insight**
The key insight is that DFS allows us to efficiently explore the graph and group connected nodes into provinces. By starting from each unvisited node and exploring its connections, we can effectively count the number of provinces in the graph.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 5 ms (Beats 58.41%) |
| 💾 Memory | 19.4 MB (Beats 100%) |
| 📅 Solved | 2025-08-20 |
| 💻 Language | Python |