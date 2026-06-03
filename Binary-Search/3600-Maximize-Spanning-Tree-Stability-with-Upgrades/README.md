# 3600. Maximize Spanning Tree Stability with Upgrades


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/)


## 📝 Problem Description

You are given an integer `n`, representing `n` nodes numbered from 0 to `n - 1` and a list of `edges`, where `edges[i] = [u_i, v_i, s_i, must_i]`:

	- `u_i` and `v_i` indicates an undirected edge between nodes `u_i` and `v_i`.

	- `s_i` is the strength of the edge.

	- `must_i` is an integer (0 or 1). If `must_i == 1`, the edge **must** be included in the** ****spanning tree**. These edges **cannot** be **upgraded**.

You are also given an integer `k`, the **maximum** number of upgrades you can perform. Each upgrade **doubles** the strength of an edge, and each eligible edge (with `must_i == 0`) can be upgraded **at most** once.

The **stability** of a spanning tree is defined as the **minimum** strength score among all edges included in it.

Return the **maximum** possible stability of any valid spanning tree. If it is impossible to connect all nodes, return `-1`.

**Note**: A **spanning tree** of a graph with `n` nodes is a subset of the edges that connects all nodes together (i.e. the graph is **connected**) *without* forming any cycles, and uses **exactly** `n - 1` edges.

 

Example 1:**

**Input:** n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1

**Output:** 2

**Explanation:**

	- Edge `[0,1]` with strength = 2 must be included in the spanning tree.

	- Edge `[1,2]` is optional and can be upgraded from 3 to 6 using one upgrade.

	- The resulting spanning tree includes these two edges with strengths 2 and 6.

	- The minimum strength in the spanning tree is 2, which is the maximum possible stability.

Example 2:**

**Input:** n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2

**Output:** 6

**Explanation:**

	- Since all edges are optional and up to `k = 2` upgrades are allowed.

	- Upgrade edges `[0,1]` from 4 to 8 and `[1,2]` from 3 to 6.

	- The resulting spanning tree includes these two edges with strengths 8 and 6.

	- The minimum strength in the tree is 6, which is the maximum possible stability.

Example 3:**

**Input:** n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0

**Output:** -1

**Explanation:**

	- All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.

 

**Constraints:**

	- `2 <= n <= 10^5`

	- `1 <= edges.length <= 10^5`

	- `edges[i] = [u_i, v_i, s_i, must_i]`

	- `0 <= u_i, v_i < n`

	- `u_i != v_i`

	- `1 <= s_i <= 10^5`

	- `must_i` is either `0` or `1`.

	- `0 <= k <= n`

	- There are no duplicate edges.

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a disjoint-set data structure to efficiently manage the edges of the graph and a priority queue to keep track of the minimum strength of the edges. The goal is to maximize the stability of the spanning tree by upgrading the edges with the highest strength.

**Approach**

1. Initialize the disjoint-set data structure with `n` nodes and their corresponding sizes.
2. Separate the edges into two lists: `must` edges that must be included in the spanning tree and `flex` edges that can be upgraded.
3. Iterate through the `must` edges and add them to the disjoint-set data structure, ensuring that they form a single connected component.
4. Sort the `flex` edges in descending order of their strengths.
5. Create a priority queue to store the minimum strength of the edges.
6. Iterate through the `flex` edges and add them to the disjoint-set data structure, updating the priority queue with their strengths.
7. While there are remaining upgrades (`k > 0`) and edges in the priority queue, upgrade the edge with the minimum strength, updating the priority queue and the minimum stability.
8. If the resulting spanning tree has multiple connected components or the priority queue is not empty, return -1, indicating that it is impossible to form a valid spanning tree.

**Time Complexity**
The time complexity of the solution is O((n + m) log m), where `n` is the number of nodes and `m` is the number of edges. This is because the disjoint-set data structure operations (find and union) take O(log n) time, and the priority queue operations (insert and delete) take O(log m) time.

**Space Complexity**
The space complexity of the solution is O(n + m), where `n` is the number of nodes and `m` is the number of edges. This is because we need to store the disjoint-set data structure, the `must` and `flex` edges, and the priority queue.

**Key Insight**
The key insight is to use a priority queue to efficiently keep track of the minimum strength of the edges and to upgrade the edges with the highest strength first. This approach ensures that we maximize the stability of the spanning tree while still satisfying the constraints of the problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 255 ms (Beats 83.02%) |
| 💾 Memory | 74.8 MB (Beats 37.74%) |
| 📅 Solved | 2026-03-12 |
| 💻 Language | Python |