# 743. Network Delay Time


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/network-delay-time/)


## 📝 Problem Description

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u_i, v_i, w_i)`, where `u_i` is the source node, `v_i` is the target node, and `w_i` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return *the **minimum** time it takes for all the* `n` *nodes to receive the signal*. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)
```

**Input:** times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
**Output:** 2

```

Example 2:**

```

**Input:** times = [[1,2,1]], n = 2, k = 1
**Output:** 1

```

Example 3:**

```

**Input:** times = [[1,2,1]], n = 2, k = 2
**Output:** -1

```

 

**Constraints:**

	- `1 <= k <= n <= 100`

	- `1 <= times.length <= 6000`

	- `times[i].length == 3`

	- `1 <= u_i, v_i <= n`

	- `u_i != v_i`

	- `0 <= w_i <= 100`

	- All the pairs `(u_i, v_i)` are **unique**. (i.e., no multiple edges.)

## 🧠 Solution Explanation

**Intuition**
The solution uses Dijkstra's algorithm to find the minimum time it takes for all nodes to receive the signal. It maintains a priority queue (heap) to keep track of the nodes that have not received the signal yet, sorted by the time it takes to reach them. The algorithm iteratively selects the node with the minimum time, updates the times of its neighbors, and adds them to the heap if necessary.

**Approach**
1. Create an adjacency list to represent the graph, where each node is associated with a list of its neighbors and the time it takes to reach them.
2. Initialize a list `time_needed` to keep track of the minimum time it takes for each node to receive the signal, initialized with a large value (1e9) for all nodes except the source node, which is set to 0.
3. Create a heap with the source node and its initial time (0).
4. While the heap is not empty, pop the node with the minimum time and update the times of its neighbors if a shorter path is found.
5. Repeat step 4 until the heap is empty.
6. Find the maximum time in the `time_needed` list, excluding the source node (index 0). If the maximum time is still 1e9, it means some nodes cannot receive the signal, so return -1.

**Time Complexity**
O((n + m) log n), where n is the number of nodes and m is the number of edges. The reason is that we perform a constant amount of work for each edge (relaxing its neighbors) and each node (adding it to the heap or updating its time). The heap operations (insertion and extraction) take O(log n) time.

**Space Complexity**
O(n + m), where n is the number of nodes and m is the number of edges. We need to store the adjacency list and the `time_needed` list, which require O(n + m) space.

**Key Insight**
The key insight is to use a priority queue (heap) to keep track of the nodes that have not received the signal yet, sorted by the time it takes to reach them. This allows us to efficiently select the node with the minimum time and update the times of its neighbors. By iteratively relaxing the neighbors of the selected node, we can find the minimum time it takes for all nodes to receive the signal.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 364 ms (Beats 14.7%) |
| 💾 Memory | 19.9 MB (Beats 100%) |
| 📅 Solved | 2025-08-31 |
| 💻 Language | Python |