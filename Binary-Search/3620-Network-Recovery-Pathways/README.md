> 📌 **Cross-listed:** Primary location is [Array/3620-Network-Recovery-Pathways](../../Array/3620-Network-Recovery-Pathways). This problem also appears under: **Array**, **Binary Search**, **Dynamic Programming**, **Graph Theory**, **Topological Sort**, **Heap (Priority Queue)**, **Shortest Path**

# 3620. Network Recovery Pathways


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/network-recovery-pathways/)


## 📝 Problem Description

You are given a directed acyclic graph of `n` nodes numbered from 0 to `n &minus; 1`. This is represented by a 2D array edges` of length `m`, where edges[i] = [u_i, v_i, cost_i]` indicates a one‑way communication from node u_i` to node v_i` with a recovery cost of cost_i`.

Some nodes may be offline. You are given a boolean array online` where online[i] = true` means node i` is online. Nodes 0 and `n &minus; 1` are always online.

A path from 0 to `n &minus; 1` is valid** if:

	- All intermediate nodes on the path are online.

	The total recovery cost of all edges on the path does not exceed `k`.

For each valid path, define its score** as the minimum edge‑cost along that path.

Return the **maximum** path score (i.e., the largest **minimum**-edge cost) among all valid paths. If no valid path exists, return -1.

 

Example 1:**

**Input:** edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10

**Output:** 3

**Explanation:**

![](https://assets.leetcode.com/uploads/2025/06/06/graph-10.png)

	
	The graph has two possible routes from node 0 to node 3:

	
		
		Path `0 &rarr; 1 &rarr; 3`

		
			
			Total cost = `5 + 10 = 15`, which exceeds k (`15 > 10`), so this path is invalid.

			

		
		

		
		Path `0 &rarr; 2 &rarr; 3`

		
			
			Total cost = `3 + 4 = 7 <= k`, so this path is valid.

			

			
			The minimum edge‐cost along this path is `min(3, 4) = 3`.

			

		
		

	
	

	
	There are no other valid paths. Hence, the maximum among all valid path‐scores is 3.

	

Example 2:**

**Input:** edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12

**Output:** 6

**Explanation:**

![](https://assets.leetcode.com/uploads/2025/06/06/graph-11.png)

	
	Node 3 is offline, so any path passing through 3 is invalid.

	

	
	Consider the remaining routes from 0 to 4:

	
		
		Path `0 &rarr; 1 &rarr; 4`

		
			
			Total cost = `7 + 5 = 12 <= k`, so this path is valid.

			

			
			The minimum edge‐cost along this path is `min(7, 5) = 5`.

			

		
		

		
		Path `0 &rarr; 2 &rarr; 3 &rarr; 4`

		
			
			Node 3 is offline, so this path is invalid regardless of cost.

			

		
		

		
		Path `0 &rarr; 2 &rarr; 4`

		
			
			Total cost = `6 + 6 = 12 <= k`, so this path is valid.

			

			
			The minimum edge‐cost along this path is `min(6, 6) = 6`.

			

		
		

	
	

	
	Among the two valid paths, their scores are 5 and 6. Therefore, the answer is 6.

	

 

**Constraints:**

	n == online.length`

	2 <= n <= 5 * 10^4`

	0 <= m == edges.length <= ``min(10^5, n * (n - 1) / 2)`

	edges[i] = [u_i, v_i, cost_i]`

	0 <= u_i, v_i < n`

	u_i != v_i`

	0 <= cost_i <= 10^9`

	0 <= k <= 5 * 10^13`

	online[i]` is either true` or false`, and both online[0]` and online[n &minus; 1]` are true`.

	The given graph is a directed acyclic graph.

## 🧠 Solution Explanation

**Intuition**
This solution uses a binary search approach to find the maximum path score. It first constructs a topological sort of the graph and then uses a depth-first search (DFS) to find the minimum edge cost for each node. The binary search is used to find the maximum path score by iteratively checking if a given limit is sufficient to reach the last node.

**Approach**
1. Construct a graph using the given edges and calculate the in-degree of each node.
2. Perform a topological sort on the graph using a queue and a list to store the sorted nodes.
3. Initialize a distance array with infinite values and set the distance of the source node (0) to 0.
4. Iterate over the sorted nodes and for each node, update the distance of its neighbors if the edge cost is less than or equal to the current limit and the neighbor is online.
5. Use binary search to find the maximum path score by iteratively checking if a given limit is sufficient to reach the last node.
6. In each iteration of the binary search, call the `find` function to check if the current limit is sufficient to reach the last node.

**Time Complexity**
The time complexity of this solution is O(n + m log n), where n is the number of nodes and m is the number of edges. The topological sort takes O(n + m) time, and the binary search takes O(log n) time. The `find` function takes O(n + m) time in the worst case.

**Space Complexity**
The space complexity of this solution is O(n + m), where n is the number of nodes and m is the number of edges. The graph and the distance array take O(n + m) space.

**Key Insight**
The key insight behind this solution is the use of binary search to find the maximum path score. By iteratively checking if a given limit is sufficient to reach the last node, we can find the maximum path score in O(log n) time. This approach is much more efficient than a brute-force approach that would take O(n^2) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 886 ms (Beats 55.68%) |
| 💾 Memory | 59.2 MB (Beats 52.27%) |
| 📅 Solved | 2026-07-03 |
| 💻 Language | Python |