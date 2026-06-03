# 1192. Critical Connections in a Network


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Biconnected Component](https://img.shields.io/badge/Biconnected%20Component-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/critical-connections-in-a-network/)


## 📝 Problem Description

There are `n` servers numbered from `0` to `n - 1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a_i, b_i]` represents a connection between servers `a_i` and `b_i`. Any server can reach other servers directly or indirectly through the network.

A *critical connection* is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png)
```

**Input:** n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
**Output:** [[1,3]]
**Explanation:** [[3,1]] is also accepted.

```

Example 2:**

```

**Input:** n = 2, connections = [[0,1]]
**Output:** [[0,1]]

```

 

**Constraints:**

	- `2 <= n <= 10^5`

	- `n - 1 <= connections.length <= 10^5`

	- `0 <= a_i, b_i <= n - 1`

	- `a_i != b_i`

	- There are no repeated connections.

## 🧠 Solution Explanation

**Intuition**
This solution uses a depth-first search (DFS) approach to find critical connections in the network. The key insight is that a critical connection is one that, if removed, would disconnect a server from the rest of the network. This can be detected by checking if the lowest reachable ancestor of a node is greater than the time at which the node was first visited.

**Approach**
1. Create an adjacency list representation of the graph from the given connections.
2. Initialize arrays to keep track of the time at which each node was first visited (`tin`), the lowest reachable ancestor of each node (`low`), and whether each node has been visited (`visited`).
3. Perform a DFS traversal of the graph, starting from an arbitrary node (in this case, node 0).
4. During the DFS, update the `tin` and `low` values for each node, and check if the lowest reachable ancestor of a node is greater than the time at which the node was first visited. If so, add the connection between the current node and its parent to the result list.
5. Return the list of critical connections.

**Time Complexity**
O(n + m), where n is the number of nodes and m is the number of edges. This is because each node and edge is visited once during the DFS traversal.

**Space Complexity**
O(n + m), where n is the number of nodes and m is the number of edges. This is because we need to store the adjacency list, as well as the `tin`, `low`, and `visited` arrays.

**Key Insight**
The key to this solution is the use of the `low` value to detect critical connections. By keeping track of the lowest reachable ancestor of each node, we can determine whether a connection is critical by checking if the lowest reachable ancestor of a node is greater than the time at which the node was first visited. This allows us to efficiently identify critical connections in the network.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 349 ms (Beats 9.78%) |
| 💾 Memory | 75.4 MB (Beats 90.22%) |
| 📅 Solved | 2025-09-30 |
| 💻 Language | Python |