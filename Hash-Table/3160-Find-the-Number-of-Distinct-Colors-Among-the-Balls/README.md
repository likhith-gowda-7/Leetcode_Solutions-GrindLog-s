> 📌 **Cross-listed:** Primary location is [Array/3160-Find-the-Number-of-Distinct-Colors-Among-the-Balls](../../Array/3160-Find-the-Number-of-Distinct-Colors-Among-the-Balls). This problem also appears under: **Array**, **Hash Table**, **Simulation**

# 3160. Find the Number of Distinct Colors Among the Balls


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/)


## 📝 Problem Description

You are given an integer `limit` and a 2D array `queries` of size `n x 2`.

There are `limit + 1` balls with **distinct** labels in the range `[0, limit]`. Initially, all balls are uncolored. For every query in `queries` that is of the form `[x, y]`, you mark ball `x` with the color `y`. After each query, you need to find the number of colors among the balls.

Return an array `result` of length `n`, where `result[i]` denotes the number of colors *after* `i^th` query.

**Note** that when answering a query, lack of a color *will not* be considered as a color.

 

Example 1:**

**Input:** limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

**Output:** [1,2,2,3]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/04/17/ezgifcom-crop.gif)

	- After query 0, ball 1 has color 4.

	- After query 1, ball 1 has color 4, and ball 2 has color 5.

	- After query 2, ball 1 has color 3, and ball 2 has color 5.

	- After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.

Example 2:**

**Input:** limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

**Output:** [1,2,2,3,4]

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/04/17/ezgifcom-crop2.gif)**

	- After query 0, ball 0 has color 1.

	- After query 1, ball 0 has color 1, and ball 1 has color 2.

	- After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.

	- After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.

	- After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.

 

**Constraints:**

	- `1 <= limit <= 10^9`

	- `1 <= n == queries.length <= 10^5`

	- `queries[i].length == 2`

	- `0 <= queries[i][0] <= limit`

	- `1 <= queries[i][1] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
This solution utilizes two hash tables, `h1` and `h2`, to efficiently track the colors of the balls and the count of each color. The key insight is to maintain a separate hash table `h2` to store the count of each color, allowing for constant-time lookups and updates.

**Approach**
1. Initialize two empty hash tables `h1` and `h2`, and an empty result list `res`.
2. Iterate through each query in the `queries` list.
3. For each query, check if the ball at position `pos` is already colored (i.e., present in `h1`).
4. If the ball is colored, decrement the count of its current color in `h2` and remove it if the count reaches zero.
5. Update the color of the ball at position `pos` in `h1` to `col`.
6. Increment the count of the new color `col` in `h2`.
7. Append the current count of colors in `h2` to the result list `res`.
8. Return the result list `res`.

**Time Complexity**
O(n * m), where n is the number of queries and m is the maximum value in the `limit` parameter. This is because each query involves a constant-time update of the hash tables, and we iterate through each query once.

**Space Complexity**
O(limit), where limit is the maximum value in the `limit` parameter. This is because we store the count of each color in the `h2` hash table, which can have at most `limit + 1` entries.

**Key Insight**
The key to this solution is maintaining a separate hash table `h2` to store the count of each color, allowing for constant-time lookups and updates. This enables us to efficiently track the number of colors among the balls after each query.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 74 ms (Beats 62.21%) |
| 💾 Memory | 63 MB (Beats 100%) |
| 📅 Solved | 2025-02-07 |
| 💻 Language | Python |