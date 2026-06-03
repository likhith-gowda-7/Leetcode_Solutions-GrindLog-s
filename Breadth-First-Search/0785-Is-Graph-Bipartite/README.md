> 📌 **Cross-listed:** Primary location is [Depth-First Search/0785-Is-Graph-Bipartite](../../Depth-First-Search/0785-Is-Graph-Bipartite). This problem also appears under: **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Graph Theory**

# 785. Is Graph Bipartite?


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/is-graph-bipartite/)


## 📝 Problem Description

There is an **undirected** graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to. More formally, for each `v` in `graph[u]`, there is an undirected edge between node `u` and node `v`. The graph has the following properties:

	- There are no self-edges (`graph[u]` does not contain `u`).

	- There are no parallel edges (`graph[u]` does not contain duplicate values).

	- If `v` is in `graph[u]`, then `u` is in `graph[v]` (the graph is undirected).

	- The graph may not be connected, meaning there may be two nodes `u` and `v` such that there is no path between them.

A graph is **bipartite** if the nodes can be partitioned into two independent sets `A` and `B` such that **every** edge in the graph connects a node in set `A` and a node in set `B`.

Return `true`* if and only if it is **bipartite***.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/21/bi2.jpg)
```

**Input:** graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
**Output:** false
**Explanation:** There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg)
```

**Input:** graph = [[1,3],[0,2],[1,3],[0,2]]
**Output:** true
**Explanation:** We can partition the nodes into two sets: {0, 2} and {1, 3}.
```

 

**Constraints:**

	- `graph.length == n`

	- `1 <= n <= 100`

	- `0 <= graph[u].length < n`

	- `0 <= graph[u][i] <= n - 1`

	- `graph[u]` does not contain `u`.

	- All the values of `graph[u]` are **unique**.

	- If `graph[u]` contains `v`, then `graph[v]` contains `u`.

## 🧠 Solution Explanation

**Intuition**
This solution uses a graph coloring approach to determine if a graph is bipartite. The idea is to assign a color (0 or 1) to each node, such that adjacent nodes have different colors. If a node is already colored, we can skip it. If we encounter a node with the same color as its neighbor, it means the graph is not bipartite.

**Approach**
1. Initialize a color array with None values, representing the color of each node.
2. Iterate through each node in the graph.
3. If a node is already colored, skip it.
4. Perform a BFS traversal starting from the current node.
5. For each neighbor of the current node, if it's not colored, assign the opposite color and add it to the queue.
6. If a neighbor has the same color as the current node, return False (graph is not bipartite).
7. If the BFS traversal completes without finding any conflicts, return True (graph is bipartite).

**Time Complexity**
O(n + m), where n is the number of nodes and m is the number of edges. We visit each node and edge once during the BFS traversal.

**Space Complexity**
O(n), where n is the number of nodes. We store the color of each node in the color array.

**Key Insight**
The key insight is that we can use a simple graph coloring approach to determine if a graph is bipartite. By assigning colors to nodes based on their neighbors, we can efficiently detect conflicts and determine if the graph is bipartite. This approach works because a graph is bipartite if and only if it can be colored with two colors such that adjacent nodes have different colors.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-08-27 |
| 💻 Language | Python |