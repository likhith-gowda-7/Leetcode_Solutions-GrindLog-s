# 947. Most Stones Removed with Same Row or Column


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple) ![Graph Theory](https://img.shields.io/badge/Graph%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)


## 📝 Problem Description

On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either **the same row or the same column** as another stone that has not been removed.

Given an array `stones` of length `n` where `stones[i] = [x_i, y_i]` represents the location of the `i^th` stone, return *the largest possible number of stones that can be removed*.

 

Example 1:**

```

**Input:** stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
**Output:** 5
**Explanation:** One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

```

Example 2:**

```

**Input:** stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
**Output:** 3
**Explanation:** One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

```

Example 3:**

```

**Input:** stones = [[0,0]]
**Output:** 0
**Explanation:** [0,0] is the only stone on the plane, so you cannot remove it.

```

 

**Constraints:**

	- `1 <= stones.length <= 1000`

	- `0 <= x_i, y_i <= 10^4`

	- No two stones are at the same coordinate point.

## 🧠 Solution Explanation

**Intuition**
The solution uses a Union-Find data structure to group stones that share the same row or column. By treating each row and column as a separate node, we can efficiently identify connected components and remove stones that are part of the same group.

**Approach**
1. Find the maximum row and column indices to determine the number of nodes needed.
2. Initialize a Union-Find data structure with `n+1` nodes, where `n` is the number of stones.
3. Define a `find` function to find the root of a node and a `union` function to merge two nodes.
4. Iterate through each stone and create two nodes: one for the row and one for the column.
5. Use the `union` function to merge the row and column nodes if they share the same stone.
6. Keep track of used nodes to avoid duplicate merges.
7. Find the roots of all used nodes and return the difference between the total number of stones and the number of roots.

**Time Complexity**
The time complexity is O(n log n) due to the `union` operation, which takes O(log n) time in the worst case. The `find` operation takes O(1) time on average.

**Space Complexity**
The space complexity is O(n) for storing the Union-Find data structure and used nodes.

**Key Insight**
The key insight is to treat each row and column as a separate node, allowing us to efficiently identify connected components using the Union-Find data structure. This approach enables us to remove stones that share the same row or column in a single pass, resulting in a efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 85.75%) |
| 💾 Memory | 19.2 MB (Beats 99.82%) |
| 📅 Solved | 2025-09-20 |
| 💻 Language | Python |