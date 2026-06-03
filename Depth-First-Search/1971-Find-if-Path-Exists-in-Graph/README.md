# 1971. Find if Path Exists in Graph


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-if-path-exists-in-graph/)


## 📝 Problem Description

There is a **bi-directional** graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [u_i, v_i]` denotes a bi-directional edge between vertex `u_i` and vertex `v_i`. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself.

You want to determine if there is a **valid path** that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true`* if there is a **valid path** from *`source`* to *`destination`*, or *`false`* otherwise**.*

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png)
```

**Input:** n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
**Output:** true
**Explanation:** There are two paths from vertex 0 to vertex 2:
- 0 &rarr; 1 &rarr; 2
- 0 &rarr; 2

```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png)
```

**Input:** n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
**Output:** false
**Explanation:** There is no path from vertex 0 to vertex 5.

```

 

**Constraints:**

	- `1 <= n <= 2 * 10^5`

	- `0 <= edges.length <= 2 * 10^5`

	- `edges[i].length == 2`

	- `0 <= u_i, v_i <= n - 1`

	- `u_i != v_i`

	- `0 <= source, destination <= n - 1`

	- There are no duplicate edges.

	- There are no self edges.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes the concept of Union Find (Disjoint-set) to determine if a valid path exists between two vertices in a bi-directional graph. By treating each vertex as a separate set, we can merge sets when an edge is found between two vertices, effectively creating a connected component. If the source and destination vertices belong to the same connected component, a valid path exists.

**Approach**
1. Initialize a list `parent` of size `n` with each element set to its index, representing the root of each set.
2. Define a helper function `find(node)` to determine the root of the set containing the given node. If the node is not its own root, recursively find its root and update the node's parent.
3. Iterate through each edge in the graph, find the roots of the sets containing the edge's vertices, and merge the sets by updating the parent of the root of one set to the root of the other set.
4. Find the root of the set containing the source vertex and compare it with the root of the set containing the destination vertex. If they are the same, a valid path exists.

**Time Complexity**
O(n + m), where n is the number of vertices and m is the number of edges. The find operation takes O(log n) time, but since we perform it n times, the total time complexity is O(n log n). However, since the find operation is dominated by the merge operation, which takes O(1) time, the overall time complexity is O(n + m).

**Space Complexity**
O(n), as we need to store the parent array of size n to keep track of the sets.

**Key Insight**
The key insight is to use the Union Find data structure to efficiently merge sets when edges are found, allowing us to determine if the source and destination vertices belong to the same connected component. This approach takes advantage of the fact that each vertex is connected to at most one other vertex, making the merge operation simple and efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 182 ms (Beats 99.04%) |
| 💾 Memory | 84.1 MB (Beats 91.36%) |
| 📅 Solved | 2025-08-08 |
| 💻 Language | Python |