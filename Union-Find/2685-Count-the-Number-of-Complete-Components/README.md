> 📌 **Cross-listed:** Primary location is [Depth-First Search/2685-Count-the-Number-of-Complete-Components](../../Depth-First-Search/2685-Count-the-Number-of-Complete-Components). This problem also appears under: **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Graph Theory**

# 2685. Count the Number of Complete Components


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-the-number-of-complete-components/)


## 📝 Problem Description

You are given an integer `n`. There is an **undirected** graph with `n` vertices, numbered from `0` to `n - 1`. You are given a 2D integer array `edges` where `edges[i] = [a_i, b_i]` denotes that there exists an **undirected** edge connecting vertices `a_i` and `b_i`.

Return *the number of **complete connected components** of the graph*.

A **connected component** is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be **complete** if there exists an edge between every pair of its vertices.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-31-23.png)**

```

**Input:** n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
**Output:** 3
**Explanation:** From the picture above, one can see that all of the components of this graph are complete.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-32-00.png)**

```

**Input:** n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
**Output:** 1
**Explanation:** The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

```

 

**Constraints:**

	- `1 <= n <= 50`

	- `0 <= edges.length <= n * (n - 1) / 2`

	- `edges[i].length == 2`

	- `0 <= a_i, b_i <= n - 1`

	- `a_i != b_i`

	- There are no repeated edges.

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to count the number of complete connected components in the graph. It first constructs an adjacency list representation of the graph, then iterates over each unvisited node, performing a DFS traversal to mark all reachable nodes as visited and count the number of edges. The key insight is that a complete connected component has a specific property: the number of edges is equal to the number of vertices times the number of vertices minus one.

**Approach**
1. Construct an adjacency list representation of the graph using the given edges.
2. Initialize a boolean array `seen` to keep track of visited nodes.
3. Iterate over each node in the graph. If the node has not been visited, perform a DFS traversal:
   1. Mark the current node as visited.
   2. Initialize counters for the number of vertices and edges in the current connected component.
   3. Recursively visit all unvisited neighbors of the current node, incrementing the vertex and edge counters.
   4. After the DFS traversal, check if the number of edges is equal to the number of vertices times the number of vertices minus one. If so, increment the result count.
5. Return the total count of complete connected components.

**Time Complexity**
O(n + m), where n is the number of vertices and m is the number of edges. This is because we visit each node and edge once during the DFS traversal.

**Space Complexity**
O(n + m), as we need to store the adjacency list representation of the graph and the `seen` array.

**Key Insight**
The key insight is that a complete connected component has a specific property: the number of edges is equal to the number of vertices times the number of vertices minus one. This allows us to efficiently count the number of complete connected components by checking this property after each DFS traversal.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 38 ms (Beats 68.17%) |
| 💾 Memory | 21 MB (Beats 27.33%) |
| 📅 Solved | 2026-07-11 |
| 💻 Language | Python |