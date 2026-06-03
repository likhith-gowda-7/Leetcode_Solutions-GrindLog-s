# 3477. Fruits Into Baskets II


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/fruits-into-baskets-ii/)


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

	- `1 <= n <= 100`

	- `1 <= fruits[i], baskets[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution iterates through each fruit and checks if it can be placed in any of the baskets. If a fruit can be placed, it marks the corresponding basket as unavailable and decrements the count of remaining fruits. This process continues until all fruits have been checked.

**Approach**
1. Initialize a variable `remaining` to store the count of remaining fruits.
2. Iterate through each fruit in the `fruits` array.
3. For each fruit, iterate through each basket in the `baskets` array.
4. If the capacity of the current basket is greater than or equal to the quantity of the current fruit, mark the basket as unavailable by setting its value to -1 and decrement the `remaining` count.
5. After checking all fruits, return the `remaining` count.

**Time Complexity**
O(n*m), where n is the number of fruits and m is the number of baskets. This is because we are iterating through each fruit and each basket.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the `remaining` count and the indices of the baskets.

**Key Insight**
The key insight is that we only need to check if a fruit can be placed in any of the baskets, and if it can, we mark the corresponding basket as unavailable. This approach ensures that we don't need to keep track of the actual allocation of fruits to baskets, making the solution efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 18 ms (Beats 75.96%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-08-05 |
| 💻 Language | Python |