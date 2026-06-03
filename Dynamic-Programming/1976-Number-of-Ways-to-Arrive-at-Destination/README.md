# 1976. Number of Ways to Arrive at Destination


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Topological Sort](https://img.shields.io/badge/Topological%20Sort-purple) ![Shortest Path](https://img.shields.io/badge/Shortest%20Path-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)


## 📝 Problem Description

You are in a city that consists of `n` intersections numbered from `0` to `n - 1` with **bi-directional** roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer `n` and a 2D integer array `roads` where `roads[i] = [u_i, v_i, time_i]` means that there is a road between intersections `u_i` and `v_i` that takes `time_i` minutes to travel. You want to know in how many ways you can travel from intersection `0` to intersection `n - 1` in the **shortest amount of time**.

Return *the **number of ways** you can arrive at your destination in the **shortest amount of time***. Since the answer may be large, return it **modulo** `10^9 + 7`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2025/02/14/1976_corrected.png)
```

**Input:** n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
**Output:** 4
**Explanation:** The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

```

Example 2:**

```

**Input:** n = 2, roads = [[1,0,10]]
**Output:** 1
**Explanation:** There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

```

 

**Constraints:**

	- `1 <= n <= 200`

	- `n - 1 <= roads.length <= n * (n - 1) / 2`

	- `roads[i].length == 3`

	- `0 <= u_i, v_i <= n - 1`

	- `1 <= time_i <= 10^9`

	- `u_i != v_i`

	- There is at most one road connecting any two intersections.

	- You can reach any intersection from any other intersection.

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using a modified version of Dijkstra's algorithm, which is typically used for finding the shortest path in a graph. However, in this case, we're interested in the number of ways to reach the destination in the shortest amount of time, not just the shortest time itself. This requires keeping track of the number of paths that reach each node in the shortest possible time.

**Approach**
1. Create an adjacency list representation of the graph, where each edge is weighted with the time it takes to travel.
2. Initialize a priority queue (heap) with the starting node (0) and its initial time (0).
3. Initialize arrays to keep track of the shortest time needed to reach each node (`time_needed`) and the number of ways to reach each node in the shortest time (`shortest_time_count`).
4. While the heap is not empty, pop the node with the shortest time and explore its neighbors:
   - If a neighbor has not been visited before or if the current path is shorter than the previously known shortest path, update its shortest time and the number of ways to reach it.
   - If the current path is equally short as the previously known shortest path, add the number of ways to reach the current node to the number of ways to reach the neighbor.
5. Return the number of ways to reach the destination node (`n-1`) in the shortest time.

**Time Complexity**
O((n + m) log n), where n is the number of nodes and m is the number of edges. This is because we perform a constant amount of work for each edge and each node, and we use a heap to efficiently select the node with the shortest time.

**Space Complexity**
O(n + m), where n is the number of nodes and m is the number of edges. This is because we store the adjacency list representation of the graph and the arrays to keep track of the shortest time and the number of ways to reach each node.

**Key Insight**
The key insight is to recognize that the number of ways to reach a node in the shortest time is the same as the number of ways to reach its predecessor node, because we can only reach the node in the shortest time by following the shortest path from its predecessor. This allows us to efficiently compute the number of ways to reach each node in the shortest time by keeping track of the number of ways to reach its predecessor node.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 72.01%) |
| 💾 Memory | 25.4 MB (Beats 48.79%) |
| 📅 Solved | 2025-09-06 |
| 💻 Language | Python |