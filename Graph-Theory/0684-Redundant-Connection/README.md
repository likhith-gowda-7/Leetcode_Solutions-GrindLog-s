> 📌 **Cross-listed:** Primary location is [Depth-First Search/0684-Redundant-Connection](../../Depth-First-Search/0684-Redundant-Connection). This problem also appears under: **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Graph Theory**

# 684. Redundant Connection


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/redundant-connection/)


## 📝 Problem Description

In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the graph.

Return *an edge that can be removed so that the resulting graph is a tree of *`n`* nodes*. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg)
```

**Input:** edges = [[1,2],[1,3],[2,3]]
**Output:** [2,3]

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-2-graph.jpg)
```

**Input:** edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
**Output:** [1,4]

```

 

**Constraints:**

	- `n == edges.length`

	- `3 <= n <= 1000`

	- `edges[i].length == 2`

	- `1 <= a_i < b_i <= edges.length`

	- `a_i != b_i`

	- There are no repeated edges.

	- The given graph is connected.

## 🧠 Solution Explanation

**Intuition**
This solution uses a Union-Find (also known as Disjoint-Set) data structure to detect cycles in the graph. The key insight is that if a cycle exists, it means that there's an edge that connects two nodes that are already connected through another path. The Union-Find data structure allows us to efficiently check if two nodes are already connected.

**Approach**
1. Initialize the parent array to contain each node as its own parent, and the rank array to contain all nodes with a rank of 1.
2. Define a `find` function to find the root of a node using path compression.
3. Define a `union` function to merge two nodes. If the two nodes are already connected (i.e., they have the same root), return `False` to indicate a cycle. Otherwise, merge the two nodes and update the rank of the new root.
4. Iterate through the edges and use the `union` function to merge the nodes. If a cycle is detected, return the edge that caused the cycle.

**Time Complexity**
The time complexity of this solution is O(n + m), where n is the number of nodes and m is the number of edges. This is because we're iterating through each edge once, and each `union` operation takes constant time.

**Space Complexity**
The space complexity of this solution is O(n), where n is the number of nodes. This is because we're storing the parent and rank arrays, which require O(n) space.

**Key Insight**
The key insight is that if a cycle exists, it means that there's an edge that connects two nodes that are already connected through another path. The Union-Find data structure allows us to efficiently check if two nodes are already connected, and the `union` function helps us detect cycles by checking if the two nodes have the same root.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1 ms (Beats 70.86%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-08-19 |
| 💻 Language | Python |