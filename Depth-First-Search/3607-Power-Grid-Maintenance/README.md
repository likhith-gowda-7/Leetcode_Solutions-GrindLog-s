> 📌 **Cross-listed:** Primary location is [Array/3607-Power-Grid-Maintenance](../../Array/3607-Power-Grid-Maintenance). This problem also appears under: **Array**, **Hash Table**, **Depth-First Search**, **Breadth-First Search**, **Union-Find**, **Graph Theory**, **Heap (Priority Queue)**, **Ordered Set**

# 3607. Power Grid Maintenance


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/power-grid-maintenance/)


## 📝 Problem Description

You are given an integer c` representing c` power stations, each with a unique identifier `id` from 1 to `c` (1‑based indexing).

These stations are interconnected via n` **bidirectional** cables, represented by a 2D array connections`, where each element connections[i] = [u_i, v_i]` indicates a connection between station `u_i` and station `v_i`. Stations that are directly or indirectly connected form a **power grid**.

Initially, **all** stations are online (operational).

You are also given a 2D array queries`, where each query is one of the following *two* types:

	
	[1, x]`: A maintenance check is requested for station x`. If station `x` is online, it resolves the check by itself. If station `x` is offline, the check is resolved by the operational station with the smallest `id` in the same **power grid** as `x`. If **no** **operational** station *exists* in that grid, return -1.

	

	
	[2, x]`: Station x` goes offline (i.e., it becomes non-operational).

	

Return an array of integers representing the results of each query of type [1, x]` in the **order** they appear.

**Note:** The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

 

Example 1:**

**Input:** c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

**Output:** [3,2,3]

**Explanation:**

![](https://assets.leetcode.com/uploads/2025/04/15/powergrid.jpg)

	Initially, all stations `{1, 2, 3, 4, 5}` are online and form a single power grid.

	Query `[1,3]`: Station 3 is online, so the maintenance check is resolved by station 3.

	Query `[2,1]`: Station 1 goes offline. The remaining online stations are `{2, 3, 4, 5}`.

	Query `[1,1]`: Station 1 is offline, so the check is resolved by the operational station with the smallest `id` among `{2, 3, 4, 5}`, which is station 2.

	Query `[2,2]`: Station 2 goes offline. The remaining online stations are `{3, 4, 5}`.

	Query `[1,2]`: Station 2 is offline, so the check is resolved by the operational station with the smallest `id` among `{3, 4, 5}`, which is station 3.

Example 2:**

**Input:** c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

**Output:** [1,-1]

**Explanation:**

	There are no connections, so each station is its own isolated grid.

	Query `[1,1]`: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.

	Query `[2,1]`: Station 1 goes offline.

	Query `[1,1]`: Station 1 is offline and there are no other stations in its grid, so the result is -1.

 

**Constraints:**

	`1 <= c <= 10^5`

	`0 <= n == connections.length <= min(10^5, c * (c - 1) / 2)`

	`connections[i].length == 2`

	`1 <= u_i, v_i <= c`

	`u_i != v_i`

	`1 <= queries.length <= 2 * 10^5`

	`queries[i].length == 2`

	`queries[i][0]` is either 1 or 2.

	`1 <= queries[i][1] <= c`

## 🧠 Solution Explanation

**Intuition**
This solution uses a disjoint-set data structure to represent the power grid as a union-find data structure. The key insight is to use a priority queue (heap) to keep track of the online stations in each connected component, allowing for efficient maintenance checks and station shutdowns.

**Approach**
1. Initialize the disjoint-set data structure with each station as its own root.
2. Iterate through the connections and perform union operations to merge stations into connected components.
3. Create a priority queue (heap) for each connected component to store the online stations.
4. Iterate through the queries:
   1. If the query is a maintenance check (mode == 1), find the root of the station's connected component and check if it's online. If not, pop the online stations from the heap until the smallest online station is found.
   2. If the query is a station shutdown (mode == 2), remove the station from the online set.

**Time Complexity**
O(n log n + q log q), where n is the number of connections and q is the number of queries. The union-find operations take O(n) time, and the priority queue operations (heap push and pop) take O(log n) time. The maintenance checks and station shutdowns take O(log q) time.

**Space Complexity**
O(n + q), where n is the number of connections and q is the number of queries. The disjoint-set data structure and priority queues require O(n + q) space.

**Key Insight**
The key insight is to use a priority queue (heap) to keep track of the online stations in each connected component, allowing for efficient maintenance checks and station shutdowns. This approach enables the solution to handle a large number of queries in O(log q) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 368 ms (Beats 61.07%) |
| 💾 Memory | 103.5 MB (Beats 99.62%) |
| 📅 Solved | 2025-11-07 |
| 💻 Language | Python |