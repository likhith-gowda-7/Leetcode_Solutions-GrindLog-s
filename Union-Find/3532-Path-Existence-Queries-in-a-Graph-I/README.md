> 📌 **Cross-listed:** Primary location is [Array/3532-Path-Existence-Queries-in-a-Graph-I](../../Array/3532-Path-Existence-Queries-in-a-Graph-I). This problem also appears under: **Array**, **Hash Table**, **Binary Search**, **Union-Find**, **Graph Theory**

# 3532. Path Existence Queries in a Graph I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-i/)


## 📝 Problem Description

You are given an integer `n` representing the number of nodes in a graph, labeled from 0 to `n - 1`.

You are also given an integer array `nums` of length `n` sorted in **non-decreasing** order, and an integer `maxDiff`.

An **undirected **edge exists between nodes `i` and `j` if the **absolute** difference between `nums[i]` and `nums[j]` is **at most** `maxDiff` (i.e., `|nums[i] - nums[j]| <= maxDiff`).

You are also given a 2D integer array `queries`. For each `queries[i] = [u_i, v_i]`, determine whether there exists a path between nodes `u_i` and `v_i`.

Return a boolean array `answer`, where `answer[i]` is `true` if there exists a path between `u_i` and `v_i` in the `i^th` query and `false` otherwise.

 

Example 1:**

**Input:** n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]

**Output:** [true,false]

**Explanation:**

	- Query `[0,0]`: Node 0 has a trivial path to itself.

	- Query `[0,1]`: There is no edge between Node 0 and Node 1 because `|nums[0] - nums[1]| = |1 - 3| = 2`, which is greater than `maxDiff`.

	- Thus, the final answer after processing all the queries is `[true, false]`.

Example 2:**

**Input:** n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]

**Output:** [false,false,true,true]

**Explanation:**

The resulting graph is:

![](https://assets.leetcode.com/uploads/2025/03/25/screenshot-2025-03-26-at-122249.png)

	- Query `[0,1]`: There is no edge between Node 0 and Node 1 because `|nums[0] - nums[1]| = |2 - 5| = 3`, which is greater than `maxDiff`.

	- Query `[0,2]`: There is no edge between Node 0 and Node 2 because `|nums[0] - nums[2]| = |2 - 6| = 4`, which is greater than `maxDiff`.

	- Query `[1,3]`: There is a path between Node 1 and Node 3 through Node 2 since `|nums[1] - nums[2]| = |5 - 6| = 1` and `|nums[2] - nums[3]| = |6 - 8| = 2`, both of which are within `maxDiff`.

	- Query `[2,3]`: There is an edge between Node 2 and Node 3 because `|nums[2] - nums[3]| = |6 - 8| = 2`, which is equal to `maxDiff`.

	- Thus, the final answer after processing all the queries is `[false, false, true, true]`.

 

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `0 <= nums[i] <= 10^5`

	- `nums` is sorted in **non-decreasing** order.

	- `0 <= maxDiff <= 10^5`

	- `1 <= queries.length <= 10^5`

	- `queries[i] == [u_i, v_i]`

	- `0 <= u_i, v_i < n`

## 🧠 Solution Explanation

**Intuition**
The solution uses a union-find approach to efficiently determine whether there exists a path between two nodes in the graph. By compressing the graph into a set of connected components based on the absolute difference between node values, we can quickly determine whether two nodes are in the same component.

**Approach**
1. Initialize an array `comp` of size `n` to store the connected component of each node.
2. Iterate through the `nums` array from the second node to the last node. For each node, check if the absolute difference between its value and the previous node's value is less than or equal to `maxDiff`. If it is, assign the same connected component to the current node as the previous node. Otherwise, assign a new connected component to the current node.
3. Return a boolean array `answer` where each element is `True` if the corresponding query node pair is in the same connected component and `False` otherwise.

**Time Complexity**
O(n + q), where n is the number of nodes and q is the number of queries. This is because we iterate through the `nums` array once to compress the graph, and then iterate through the `queries` array to determine the connected components.

**Space Complexity**
O(n), where n is the number of nodes. This is because we need to store the connected component of each node in the `comp` array.

**Key Insight**
The key insight is that by compressing the graph into a set of connected components based on the absolute difference between node values, we can efficiently determine whether two nodes are in the same component. This is because if two nodes are in the same component, it means that there exists a path between them with an absolute difference of at most `maxDiff` between their values.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 101 ms (Beats 56.45%) |
| 💾 Memory | 49.6 MB (Beats 70.16%) |
| 📅 Solved | 2026-07-10 |
| 💻 Language | Python |