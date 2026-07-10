> 📌 **Cross-listed:** Primary location is [Array/3534-Path-Existence-Queries-in-a-Graph-II](../../Array/3534-Path-Existence-Queries-in-a-Graph-II). This problem also appears under: **Array**, **Two Pointers**, **Binary Search**, **Dynamic Programming**, **Greedy**, **Bit Manipulation**, **Graph Theory**, **Sorting**

# 3534. Path Existence Queries in a Graph II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/)


## 📝 Problem Description

You are given an integer `n` representing the number of nodes in a graph, labeled from 0 to `n - 1`.

You are also given an integer array `nums` of length `n` and an integer `maxDiff`.

An **undirected **edge exists between nodes `i` and `j` if the **absolute** difference between `nums[i]` and `nums[j]` is **at most** `maxDiff` (i.e., `|nums[i] - nums[j]| <= maxDiff`).

You are also given a 2D integer array `queries`. For each `queries[i] = [u_i, v_i]`, find the **minimum** distance between nodes `u_i` and `v_i`_. If no path exists between the two nodes, return -1 for that query.

Return an array `answer`, where `answer[i]` is the result of the `i^th` query.

**Note:** The edges between the nodes are unweighted.

 

Example 1:**

**Input:** n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]

**Output:** [1,1]

**Explanation:**

The resulting graph is:

![](https://assets.leetcode.com/uploads/2025/03/25/4149example1drawio.png)

	
		
			Query
			Shortest Path
			Minimum Distance
		
		
			[0, 3]
			0 &rarr; 3
			1
		
		
			[2, 4]
			2 &rarr; 4
			1
		
	

Thus, the output is `[1, 1]`.

Example 2:**

**Input:** n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]

**Output:** [1,2,-1,1]

**Explanation:**

The resulting graph is:

![](https://assets.leetcode.com/uploads/2025/03/25/4149example2drawio.png)

	
		
			Query
			Shortest Path
			Minimum Distance
		
		
			[0, 1]
			0 &rarr; 1
			1
		
		
			[0, 2]
			0 &rarr; 1 &rarr; 2
			2
		
		
			[2, 3]
			None
			-1
		
		
			[4, 3]
			3 &rarr; 4
			1
		
	

Thus, the output is `[1, 2, -1, 1]`.

Example 3:**

**Input:** n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]

**Output:** [0,-1,-1]

**Explanation:**

There are no edges between any two nodes because:

	- Nodes 0 and 1: `|nums[0] - nums[1]| = |3 - 6| = 3 > 1`

	- Nodes 0 and 2: `|nums[0] - nums[2]| = |3 - 1| = 2 > 1`

	- Nodes 1 and 2: `|nums[1] - nums[2]| = |6 - 1| = 5 > 1`

Thus, no node can reach any other node, and the output is `[0, -1, -1]`.

 

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `0 <= nums[i] <= 10^5`

	- `0 <= maxDiff <= 10^5`

	- `1 <= queries.length <= 10^5`

	- `queries[i] == [u_i, v_i]`

	- `0 <= u_i, v_i < n`

## 🧠 Solution Explanation

**Intuition**
This solution utilizes a combination of sorting, binary lifting, and a clever use of a sparse table to efficiently answer path existence queries in a graph. The key insight is to represent the graph as a sorted array of nodes, where each node is associated with its index in the sorted array. This allows for efficient querying of the minimum distance between two nodes.

**Approach**
1. Sort the nodes based on their values and store their original indices.
2. Create a sparse table `st` to store the maximum right boundary for each node `i` at each level `j`. The value `st[i][j]` represents the maximum right boundary for node `i` at level `j`.
3. Initialize the first column of the sparse table `st` by iterating through the sorted nodes and finding the maximum right boundary for each node.
4. For each level `j` from 2 to `LOG`, populate the sparse table `st` by using the previously computed values.
5. For each query, find the minimum distance between the two nodes `u` and `v` by using the sparse table `st` and binary lifting.

**Time Complexity**
The time complexity of this solution is O(n log n + q log n), where n is the number of nodes and q is the number of queries. This is because we spend O(n log n) time sorting the nodes and O(q log n) time answering each query using the sparse table.

**Space Complexity**
The space complexity of this solution is O(n log n), which is used to store the sparse table `st`.

**Key Insight**
The key insight is to represent the graph as a sorted array of nodes, where each node is associated with its index in the sorted array. This allows for efficient querying of the minimum distance between two nodes by using a sparse table and binary lifting. The use of a sparse table enables us to answer queries in O(log n) time, making the overall solution efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1879 ms (Beats 41.94%) |
| 💾 Memory | 88.6 MB (Beats 35.48%) |
| 📅 Solved | 2026-07-10 |
| 💻 Language | Python |