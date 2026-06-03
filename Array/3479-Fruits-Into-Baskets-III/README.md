# 3479. Fruits Into Baskets III


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple) ![Ordered Set](https://img.shields.io/badge/Ordered%20Set-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/fruits-into-baskets-iii/)


## 📝 Problem Description

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where `fruits[i]` represents the **quantity** of the `i^th` type of fruit, and `baskets[j]` represents the **capacity** of the `j^th` basket.

From left to right, place the fruits according to these rules:

	- Each fruit type must be placed in the **leftmost available basket** with a capacity **greater than or equal** to the quantity of that fruit type.

	- Each basket can hold **only one** type of fruit.

	- If a fruit type **cannot be placed** in any basket, it remains **unplaced**.

Return the number of fruit types that remain unplaced after all possible allocations are made.

 

Example 1:**

**Input:** fruits = [4,2,5], baskets = [3,5,4]

**Output:** 1

**Explanation:**

	- `fruits[0] = 4` is placed in `baskets[1] = 5`.

	- `fruits[1] = 2` is placed in `baskets[0] = 3`.

	- `fruits[2] = 5` cannot be placed in `baskets[2] = 4`.

Since one fruit type remains unplaced, we return 1.

Example 2:**

**Input:** fruits = [3,6,1], baskets = [6,4,7]

**Output:** 0

**Explanation:**

	- `fruits[0] = 3` is placed in `baskets[0] = 6`.

	- `fruits[1] = 6` cannot be placed in `baskets[1] = 4` (insufficient capacity) but can be placed in the next available basket, `baskets[2] = 7`.

	- `fruits[2] = 1` is placed in `baskets[1] = 4`.

Since all fruits are successfully placed, we return 0.

 

**Constraints:**

	- `n == fruits.length == baskets.length`

	- `1 <= n <= 10^5`

	- `1 <= fruits[i], baskets[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a Segment Tree to efficiently find the leftmost available basket with a capacity greater than or equal to the quantity of each fruit type. This approach allows for fast updates and queries, enabling the algorithm to handle the dynamic allocation of fruits to baskets.

**Approach**
1. Build a Segment Tree from the baskets array, where each node represents the maximum capacity of a range of baskets.
2. Iterate through the fruits array, and for each fruit type, query the Segment Tree to find the leftmost available basket with a capacity greater than or equal to the fruit's quantity.
3. If such a basket is found, update the Segment Tree by setting the capacity of the basket to 0.
4. If no such basket is found, increment the unplaced counter.
5. After iterating through all fruit types, return the unplaced counter.

**Time Complexity**
O(n log n), where n is the number of baskets. The Segment Tree operations (build, update, query) take O(log n) time, and we perform these operations n times.

**Space Complexity**
O(n), where n is the number of baskets. We store the Segment Tree, which requires O(n) space.

**Key Insight**
The key insight is to use a Segment Tree to efficiently manage the availability of baskets. By storing the maximum capacity of each range of baskets, we can quickly find the leftmost available basket for each fruit type, allowing us to allocate fruits to baskets in a dynamic and efficient manner.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1932 ms (Beats 70.59%) |
| 💾 Memory | 39.2 MB (Beats 66.18%) |
| 📅 Solved | 2025-08-06 |
| 💻 Language | Python |