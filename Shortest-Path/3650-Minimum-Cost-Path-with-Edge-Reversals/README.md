> 📌 **Cross-listed:** Primary location is [Graph Theory/3650-Minimum-Cost-Path-with-Edge-Reversals](../../Graph-Theory/3650-Minimum-Cost-Path-with-Edge-Reversals). This problem also appears under: **Graph Theory**, **Heap (Priority Queue)**, **Shortest Path**

# 3650. Minimum Cost Path with Edge Reversals


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple) ![Shortest Path](https://img.shields.io/badge/Shortest%20Path-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/)


## 📝 Problem Description

You are given a directed, weighted graph with `n` nodes labeled from 0 to `n - 1`, and an array `edges` where `edges[i] = [u_i, v_i, w_i]` represents a directed edge from node `u_i` to node `v_i` with cost `w_i`.

Each node `u_i` has a switch that can be used **at most once**: when you arrive at `u_i` and have not yet used its switch, you may activate it on one of its incoming edges `v_i &rarr; u_i` reverse that edge to `u_i &rarr; v_i` and **immediately** traverse it.

The reversal is only valid for that single move, and using a reversed edge costs `2 * w_i`.

Return the **minimum** total cost to travel from node 0 to node `n - 1`. If it is not possible, return -1.

 

Example 1:**

**Input:** n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]

**Output:** 5

**Explanation: **

**![](https://assets.leetcode.com/uploads/2025/05/07/e1drawio.png)**

	- Use the path `0 &rarr; 1` (cost 3).

	- At node 1 reverse the original edge `3 &rarr; 1` into `1 &rarr; 3` and traverse it at cost `2 * 1 = 2`.

	- Total cost is `3 + 2 = 5`.

Example 2:**

**Input:** n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]

**Output:** 3

**Explanation:**

	- No reversal is needed. Take the path `0 &rarr; 2` (cost 1), then `2 &rarr; 1` (cost 1), then `1 &rarr; 3` (cost 1).

	- Total cost is `1 + 1 + 1 = 3`.

 

**Constraints:**

	- `2 <= n <= 5 * 10^4`

	- `1 <= edges.length <= 10^5`

	- `edges[i] = [u_i, v_i, w_i]`

	- `0 <= u_i, v_i <= n - 1`

	- `1 <= w_i <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution uses a priority queue (heap) to efficiently explore the graph and find the shortest path from node 0 to node n-1. By maintaining a distance array, it keeps track of the minimum cost to reach each node. The key insight is that we can use the edge reversal operation to reduce the cost of traversing certain edges.

**Approach**
1. Create an adjacency list representation of the graph, where each node has a list of its neighbors and their corresponding costs.
2. Initialize a priority queue (heap) with the starting node (0) and its distance (0).
3. While the heap is not empty, pop the node with the minimum distance and explore its neighbors.
4. For each neighbor, calculate the new distance by adding the cost of the edge to the current node's distance.
5. If the new distance is less than the previously known distance to the neighbor, update the distance array and push the neighbor into the heap.
6. If the final node (n-1) is reached, return its distance; otherwise, return -1 if the heap is empty.

**Time Complexity**
O(n log n), where n is the number of nodes. The priority queue operations (heappush and heappop) take O(log n) time, and we perform these operations for each node, resulting in a total time complexity of O(n log n).

**Space Complexity**
O(n + m), where n is the number of nodes and m is the number of edges. We need to store the adjacency list, distance array, and priority queue, which require O(n + m) space.

**Key Insight**
The key insight is that we can use the edge reversal operation to reduce the cost of traversing certain edges. By maintaining a distance array and using a priority queue to efficiently explore the graph, we can find the minimum cost path from node 0 to node n-1.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 460 ms (Beats 72.71%) |
| 💾 Memory | 70.8 MB (Beats 57.01%) |
| 📅 Solved | 2026-01-29 |
| 💻 Language | Python |