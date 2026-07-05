# 2492. Minimum Score of a Path Between Two Cities


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)


## 📝 Problem Description

You are given a positive integer `n` representing `n` cities numbered from `1` to `n`. You are also given a **2D** array `roads` where `roads[i] = [a_i, b_i, distance_i]` indicates that there is a **bidirectional **road between cities `a_i` and `b_i` with a distance equal to `distance_i`. The cities graph is not necessarily connected.

The **score** of a path between two cities is defined as the **minimum **distance of a road in this path.

Return *the **minimum **possible score of a path between cities *`1`* and *`n`.

**Note**:

	- A path is a sequence of roads between two cities.

	- It is allowed for a path to contain the same road **multiple** times, and you can visit cities `1` and `n` multiple times along the path.

	- The test cases are generated such that there is **at least** one path between `1` and `n`.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2022/10/12/graph11.png)
```

**Input:** n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
**Output:** 5
**Explanation:** The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2022/10/12/graph22.png)
```

**Input:** n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
**Output:** 2
**Explanation:** The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

```

 

**Constraints:**

	- `2 <= n <= 10^5`

	- `1 <= roads.length <= 10^5`

	- `roads[i].length == 3`

	- `1 <= a_i, b_i <= n`

	- `a_i != b_i`

	- `1 <= distance_i <= 10^4`

	- There are no repeated edges.

	- There is at least one path between `1` and `n`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a union-find data structure to efficiently manage the connected components in the graph and keep track of the minimum score for each component. By merging components with the minimum score, it ensures that the minimum score is propagated throughout the graph.

**Approach**
1. Initialize the parent array with each node as its own parent and the minimum score array with infinity for each node.
2. Define a `find` function to find the root of a node using path compression.
3. Define a `union` function to merge two nodes with a given cost, updating the minimum score of the resulting component.
4. Iterate through the roads and apply the `union` function to merge nodes with the given cost.
5. Find the root of node `n` and return the minimum score of that component.

**Time Complexity**
O((n + m) \* alpha(n)), where m is the number of roads and alpha(n) is the inverse Ackermann function, which grows very slowly. The time complexity is dominated by the union-find operations, which take O(log* n) time per operation.

**Space Complexity**
O(n), as we need to store the parent array and the minimum score array.

**Key Insight**
The key insight is that by using a union-find data structure, we can efficiently merge components with the minimum score, ensuring that the minimum score is propagated throughout the graph. This approach allows us to solve the problem in O((n + m) \* alpha(n)) time, which is much faster than a naive approach that would require O(n^2) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 84 ms (Beats 98.8%) |
| 💾 Memory | 52.6 MB (Beats 91.78%) |
| 📅 Solved | 2026-07-04 |
| 💻 Language | Python |