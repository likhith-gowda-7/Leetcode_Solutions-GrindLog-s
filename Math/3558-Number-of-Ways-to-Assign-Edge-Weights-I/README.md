# 3558. Number of Ways to Assign Edge Weights I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Tree](https://img.shields.io/badge/Tree-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/)


## 📝 Problem Description

There is an undirected tree with `n` nodes labeled from 1 to `n`, rooted at node 1. The tree is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i`.

Initially, all edges have a weight of 0. You must assign each edge a weight of either **1** or **2**.

The **cost** of a path between any two nodes `u` and `v` is the total weight of all edges in the path connecting them.

Select any one node `x` at the **maximum** depth. Return the number of ways to assign edge weights in the path from node 1 to `x` such that its total cost is **odd**.

Since the answer may be large, return it **modulo** `10^9 + 7`.

**Note:** Ignore all edges **not** in the path from node 1 to `x`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2025/03/23/screenshot-2025-03-24-at-060006.png)

**Input:** edges = [[1,2]]

**Output:** 1

**Explanation:**

	- The path from Node 1 to Node 2 consists of one edge (`1 &rarr; 2`).

	- Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

Example 2:**

![](https://assets.leetcode.com/uploads/2025/03/23/screenshot-2025-03-24-at-055820.png)

**Input:** edges = [[1,2],[1,3],[3,4],[3,5]]

**Output:** 2

**Explanation:**

	- The maximum depth is 2, with nodes 4 and 5 at the same depth. Either node can be selected for processing.

	- For example, the path from Node 1 to Node 4 consists of two edges (`1 &rarr; 3` and `3 &rarr; 4`).

	- Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.

 

**Constraints:**

	- `2 <= n <= 10^5`

	- `edges.length == n - 1`

	- `edges[i] == [u_i, v_i]`

	- `1 <= u_i, v_i <= n`

	- `edges` represents a valid tree.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the number of ways to assign edge weights in an undirected tree such that the total cost of a path from node 1 to a node at maximum depth is odd. We can use a depth-first search (DFS) to traverse the tree and calculate the maximum depth. The key insight is that we can assign weights to edges in a way that ensures the total cost is odd by alternating between 1 and 2 for each edge.

**Approach**
1. Create an adjacency list representation of the tree using the given edges.
2. Define a recursive DFS function to calculate the maximum depth of the tree.
3. In the DFS function, for each node, recursively calculate the maximum depth of its children and update the maximum depth if necessary.
4. After calculating the maximum depth, return the result of `pow(2, max_depth - 1, mod)`, where `mod` is a large prime number to prevent overflow.

**Time Complexity**
O(n), where n is the number of nodes in the tree. This is because we visit each node at most once in the DFS traversal.

**Space Complexity**
O(n), where n is the number of nodes in the tree. This is because we store the adjacency list representation of the tree, which requires O(n) space.

**Key Insight**
The key insight is that we can assign weights to edges in a way that ensures the total cost is odd by alternating between 1 and 2 for each edge. This is because the total cost is the sum of the weights of all edges in the path, and since we are alternating between 1 and 2, the sum will always be odd. Therefore, we can simply calculate the number of ways to assign weights to the edges in the path from node 1 to the node at maximum depth, which is `pow(2, max_depth - 1, mod)`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 307 ms (Beats 79.57%) |
| 💾 Memory | 78.9 MB (Beats 48.39%) |
| 📅 Solved | 2026-06-11 |
| 💻 Language | Python |