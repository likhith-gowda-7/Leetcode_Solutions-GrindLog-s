# 3559. Number of Ways to Assign Edge Weights II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/)


## 📝 Problem Description

There is an undirected tree with `n` nodes labeled from 1 to `n`, rooted at node 1. The tree is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i`.

Initially, all edges have a weight of 0. You must assign each edge a weight of either **1** or **2**.

The **cost** of a path between any two nodes `u` and `v` is the total weight of all edges in the path connecting them.

You are given a 2D integer array `queries`. For each `queries[i] = [u_i, v_i]`, determine the number of ways to assign weights to edges **in the path** such that the cost of the path between `u_i` and `v_i` is **odd**.

Return an array `answer`, where `answer[i]` is the number of valid assignments for `queries[i]`.

Since the answer may be large, apply **modulo** `10^9 + 7` to each `answer[i]`.

**Note:** For each query, disregard all edges **not** in the path between node `u_i` and `v_i`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2025/03/23/screenshot-2025-03-24-at-060006.png)

**Input:** edges = [[1,2]], queries = [[1,1],[1,2]]

**Output:** [0,1]

**Explanation:**

	- Query `[1,1]`: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0.

	- Query `[1,2]`: The path from Node 1 to Node 2 consists of one edge (`1 &rarr; 2`). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

Example 2:**

![](https://assets.leetcode.com/uploads/2025/03/23/screenshot-2025-03-24-at-055820.png)

**Input:** edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]

**Output:** [2,1,4]

**Explanation:**

	- Query `[1,4]`: The path from Node 1 to Node 4 consists of two edges (`1 &rarr; 3` and `3 &rarr; 4`). Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.

	- Query `[3,4]`: The path from Node 3 to Node 4 consists of one edge (`3 &rarr; 4`). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

	- Query `[2,5]`: The path from Node 2 to Node 5 consists of three edges (`2 &rarr; 1, 1 &rarr; 3`, and `3 &rarr; 5`). Assigning (1,2,2), (2,1,2), (2,2,1), or (1,1,1) makes the cost odd. Thus, the number of valid assignments is 4.

 

**Constraints:**

	- `2 <= n <= 10^5`

	- `edges.length == n - 1`

	- `edges[i] == [u_i, v_i]`

	- `1 <= queries.length <= 10^5`

	- `queries[i] == [u_i, v_i]`

	- `1 <= u_i, v_i <= n`

	- `edges` represents a valid tree.

## 🧠 Solution Explanation

**Intuition**
The solution uses a technique called "LCA (Lowest Common Ancestor) with Binary Lift" to efficiently calculate the number of ways to assign edge weights to make the cost of a path between two nodes odd. The idea is to use the LCA to find the distance between the two nodes, and then use modular exponentiation to calculate the number of ways to assign weights.

**Approach**
1. Initialize the adjacency list `adj` to represent the tree, and the `depth` array to store the depth of each node.
2. Perform a depth-first search (DFS) to build the `up` array, which stores the parent of each node at each level.
3. For each query, find the LCA of the two nodes using the `lca` function.
4. Calculate the distance between the two nodes by subtracting the depth of the LCA from the depths of the two nodes.
5. If the distance is 0, there are no ways to assign weights to make the cost odd, so append 0 to the answer array.
6. Otherwise, use modular exponentiation to calculate the number of ways to assign weights, and append the result to the answer array.

**Time Complexity**
The time complexity is O(n + q * log n), where n is the number of nodes and q is the number of queries. The DFS and LCA operations take O(n) time, and the modular exponentiation takes O(log n) time per query.

**Space Complexity**
The space complexity is O(n + q), where n is the number of nodes and q is the number of queries. The `adj` and `up` arrays take O(n) space, and the `depth` array takes O(n) space. The answer array takes O(q) space.

**Key Insight**
The key insight is to use the LCA to find the distance between the two nodes, and then use modular exponentiation to calculate the number of ways to assign weights. This approach allows us to efficiently calculate the answer for each query, and the use of binary lift to calculate the LCA reduces the time complexity of the LCA operation.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1447 ms (Beats 47.92%) |
| 💾 Memory | 99.7 MB (Beats 85.42%) |
| 📅 Solved | 2026-06-13 |
| 💻 Language | Python |