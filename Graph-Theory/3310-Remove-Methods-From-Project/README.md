> 📌 **Cross-listed:** Primary location is [Depth-First Search/3310-Remove-Methods-From-Project](../../Depth-First-Search/3310-Remove-Methods-From-Project). This problem also appears under: **Depth-First Search**, **Breadth-First Search**, **Graph Theory**

# 3310. Remove Methods From Project


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-methods-from-project/)


## 📝 Problem Description

You are maintaining a project that has `n` methods numbered from `0` to `n - 1`.

You are given two integers `n` and `k`, and a 2D integer array `invocations`, where `invocations[i] = [a_i, b_i]` indicates that method `a_i` invokes method `b_i`.

There is a known bug in method `k`. Method `k`, along with any method invoked by it, either **directly** or **indirectly**, are considered **suspicious** and we aim to remove them.

A group of methods can only be removed if no method **outside** the group invokes any methods **within** it.

Return an array containing all the remaining methods after removing all the **suspicious** methods. You may return the answer in *any order*. If it is not possible to remove **all** the suspicious methods, **none** should be removed.

 

Example 1:**

**Input:** n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]

**Output:** [0,1,2,3]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/07/18/graph-2.png)

Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.

Example 2:**

**Input:** n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]

**Output:** [3,4]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/07/18/graph-3.png)

Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.

Example 3:**

**Input:** n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]

**Output:** []

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/07/20/graph.png)

All methods are suspicious. We can remove them.

 

**Constraints:**

	- `1 <= n <= 10^5`

	- `0 <= k <= n - 1`

	- `0 <= invocations.length <= 2 * 10^5`

	- `invocations[i] == [a_i, b_i]`

	- `0 <= a_i, b_i <= n - 1`

	- `a_i != b_i`

	- `invocations[i] != invocations[j]`

## 🧠 Solution Explanation

**Intuition**
The solution uses a graph traversal approach to identify the connected components in the invocation graph. It marks the suspicious methods and their neighbors as visited, and then checks if any remaining methods have incoming edges from outside the connected component. If so, it marks the entire component as connected and adds all its methods to the result.

**Approach**
1. Create an adjacency list representation of the invocation graph and initialize the in-degree of each node to 0.
2. Iterate through the invocations and update the adjacency list and in-degree of each node.
3. Perform a BFS traversal from the suspicious method `k`, marking all visited nodes as suspicious and decrementing the in-degree of their neighbors.
4. Initialize a flag `connected` to False and an empty result list `res`.
5. Iterate through the nodes and add them to the result list if they are not suspicious. If a node is suspicious but has incoming edges from outside the connected component, set `connected` to True.
6. If `connected` is True, add all suspicious nodes to the result list.

**Time Complexity**
O(n + m), where n is the number of methods and m is the number of invocations. This is because we iterate through the invocations once to create the adjacency list and then perform a BFS traversal.

**Space Complexity**
O(n + m), where n is the number of methods and m is the number of invocations. This is because we store the adjacency list and in-degree of each node.

**Key Insight**
The key insight is to use a BFS traversal to identify the connected components in the invocation graph and then check if any remaining methods have incoming edges from outside the connected component. This allows us to efficiently determine whether it is possible to remove all suspicious methods.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 259 ms (Beats 78.79%) |
| 💾 Memory | 108.4 MB (Beats 52.27%) |
| 📅 Solved | 2026-08-05 |
| 💻 Language | Python |