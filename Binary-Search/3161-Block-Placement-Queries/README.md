> 📌 **Cross-listed:** Primary location is [Array/3161-Block-Placement-Queries](../../Array/3161-Block-Placement-Queries). This problem also appears under: **Array**, **Binary Search**, **Binary Indexed Tree**, **Segment Tree**

# 3161. Block Placement Queries


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Binary Indexed Tree](https://img.shields.io/badge/Binary%20Indexed%20Tree-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/block-placement-queries/)


## 📝 Problem Description

There exists an infinite number line, with its origin at 0 and extending towards the **positive** x-axis.

You are given a 2D array `queries`, which contains two types of queries:

	- For a query of type 1, `queries[i] = [1, x]`. Build an obstacle at distance `x` from the origin. It is guaranteed that there is **no** obstacle at distance `x` when the query is asked.

	- For a query of type 2, `queries[i] = [2, x, sz]`. Check if it is possible to place a block of size `sz` *anywhere* in the range `[0, x]` on the line, such that the block **entirely** lies in the range `[0, x]`. A block **cannot **be placed if it intersects with any obstacle, but it may touch it. Note that you do** not** actually place the block. Queries are separate.

Return a boolean array `results`, where `results[i]` is `true` if you can place the block specified in the `i^th` query of type 2, and `false` otherwise.

 

Example 1:**

**Input:** queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]

**Output:** [false,true,true]

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/04/22/example0block.png)**

For query 0, place an obstacle at `x = 2`. A block of size at most 2 can be placed before `x = 3`.

Example 2:**

**Input:** queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

**Output:** [true,true,false]

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/04/22/example1block.png)**

	- Place an obstacle at `x = 7` for query 0. A block of size at most 7 can be placed before `x = 7`.

	- Place an obstacle at `x = 2` for query 2. Now, a block of size at most 5 can be placed before `x = 7`, and a block of size at most 2 before `x = 2`.

 

**Constraints:**

	- `1 <= queries.length <= 15 * 10^4`

	- `2 <= queries[i].length <= 3`

	- `1 <= queries[i][0] <= 2`

	- `1 <= x, sz <= min(5 * 10^4, 3 * queries.length)`

	- The input is generated such that for queries of type 1, no obstacle exists at distance `x` when the query is asked.

	- The input is generated such that there is at least one query of type 2.

## 🧠 Solution Explanation

**Intuition**
The problem requires us to process queries on a line with obstacles. We use a Fenwick tree to efficiently count the number of obstacles to the left and right of a given point, and a segment tree to store the maximum prefix sum up to each point. This allows us to determine whether a block of a given size can be placed within a range without intersecting any obstacles.

**Approach**
1. Initialize a Fenwick tree and a segment tree with the maximum possible size.
2. Process each query:
   - For type 1 queries, add an obstacle at the given point, update the Fenwick tree, and update the segment tree with the new maximum prefix sum.
   - For type 2 queries, calculate the number of obstacles to the left of the given point, and query the segment tree to get the maximum prefix sum up to the given point. Determine whether a block of the given size can be placed within the range.
3. Return the results as a boolean array.

**Time Complexity**
The time complexity is O(n log n), where n is the number of queries. This is because we process each query in O(log n) time using the Fenwick tree and segment tree, and we perform O(n) queries in total.

**Space Complexity**
The space complexity is O(n), where n is the maximum possible size. This is because we store the Fenwick tree and segment tree with the maximum possible size.

**Key Insight**
The key insight is to use a Fenwick tree to efficiently count the number of obstacles to the left and right of a given point, and a segment tree to store the maximum prefix sum up to each point. This allows us to determine whether a block of a given size can be placed within a range without intersecting any obstacles in O(log n) time per query.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 6352 ms (Beats 9.65%) |
| 💾 Memory | 78.8 MB (Beats 80.52%) |
| 📅 Solved | 2026-05-30 |
| 💻 Language | Python |