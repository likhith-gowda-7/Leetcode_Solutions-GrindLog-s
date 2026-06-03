# 802. Find Eventual Safe States


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Topological Sort](https://img.shields.io/badge/Topological%20Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-eventual-safe-states/)


## 📝 Problem Description

There is a directed graph of `n` nodes with each node labeled from `0` to `n - 1`. The graph is represented by a **0-indexed** 2D integer array `graph` where `graph[i]` is an integer array of nodes adjacent to node `i`, meaning there is an edge from node `i` to each node in `graph[i]`.

A node is a **terminal node** if there are no outgoing edges. A node is a **safe node** if every possible path starting from that node leads to a **terminal node** (or another safe node).

Return *an array containing all the **safe nodes** of the graph*. The answer should be sorted in **ascending** order.

 

Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png)
```

**Input:** graph = [[1,2],[2,3],[5],[0],[5],[],[]]
**Output:** [2,4,5,6]
**Explanation:** The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
```

Example 2:**

```

**Input:** graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
**Output:** [4]
**Explanation:**
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

```

 

**Constraints:**

	- `n == graph.length`

	- `1 <= n <= 10^4`

	- `0 <= graph[i].length <= n`

	- `0 <= graph[i][j] <= n - 1`

	- `graph[i]` is sorted in a strictly increasing order.

	- The graph may contain self-loops.

	- The number of edges in the graph will be in the range `[1, 4 * 10^4]`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a depth-first search (DFS) approach to traverse the graph and identify safe nodes. A node is considered safe if all its neighboring nodes are either terminal nodes or safe nodes. The key insight is to use a state array to keep track of the visiting status of each node, which helps to detect cycles and avoid revisiting nodes.

**Approach**
1. Initialize a state array of size `n` to keep track of the visiting status of each node (0: unvisited, 1: visiting, 2: visited).
2. Define a DFS function that takes a node as input and returns a boolean indicating whether the node is safe.
3. In the DFS function:
   a. If the node is being visited (state[node] == 1), it means a cycle is detected, so return False.
   b. If the node has already been marked safe (state[node] == 2), return True.
   c. Mark the node as visiting (state[node] = 1) and iterate over its neighboring nodes.
   d. For each neighboring node, recursively call the DFS function and return False if it's not safe.
   e. If all neighboring nodes are safe, mark the current node as safe (state[node] = 2) and return True.
4. Iterate over all nodes in the graph and call the DFS function to check if each node is safe.
5. If a node is safe, add it to the safe_nodes list.

**Time Complexity**
O(n + m), where n is the number of nodes and m is the number of edges. This is because each node and edge is visited at most once during the DFS traversal.

**Space Complexity**
O(n), which is the space required to store the state array.

**Key Insight**
The key insight is to use a state array to keep track of the visiting status of each node, which helps to detect cycles and avoid revisiting nodes. This allows the DFS function to correctly identify safe nodes in the graph.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 24 ms (Beats 88.2%) |
| 💾 Memory | 23.4 MB (Beats 100%) |
| 📅 Solved | 2025-08-27 |
| 💻 Language | Python |