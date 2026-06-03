> 📌 **Cross-listed:** Primary location is [Math/2485-Find-the-Pivot-Integer](../../Math/2485-Find-the-Pivot-Integer). This problem also appears under: **Math**, **Prefix Sum**

# 2485. Find the Pivot Integer


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-pivot-integer/)


## 📝 Problem Description

Given a positive integer `n`, find the **pivot integer** `x` such that:

	- The sum of all elements between `1` and `x` inclusively equals the sum of all elements between `x` and `n` inclusively.

Return *the pivot integer *`x`. If no such integer exists, return `-1`. It is guaranteed that there will be at most one pivot index for the given input.

 

Example 1:**

```

**Input:** n = 8
**Output:** 6
**Explanation:** 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

```

Example 2:**

```

**Input:** n = 1
**Output:** 1
**Explanation:** 1 is the pivot integer since: 1 = 1.

```

Example 3:**

```

**Input:** n = 4
**Output:** -1
**Explanation:** It can be proved that no such integer exist.

```

 

**Constraints:**

	- `1 <= n <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a running sum of the left side (from 1 to `x`) and checking if it equals the sum of the right side (from `x` to `n`). This is possible because the total sum of all numbers from 1 to `n` is known and can be calculated in constant time.

**Approach**
1. Calculate the total sum of all numbers from 1 to `n` using the formula for the sum of an arithmetic series: `n * (n + 1) / 2`.
2. Initialize a variable `left` to 0, which will store the running sum of the left side.
3. Iterate over the numbers from 1 to `n`:
   1. Calculate the sum of the right side by subtracting the current `left` from the total sum.
   2. Add the current number to `left`.
   3. Check if the sum of the right side equals the current `left`. If it does, return the current number as the pivot integer.
4. If no pivot integer is found after iterating over all numbers, return -1.

**Time Complexity**
O(n), where n is the input number. This is because we iterate over the numbers from 1 to `n` once.

**Space Complexity**
O(1), which means constant space complexity. We only use a few variables to store the total sum, left sum, and current number, regardless of the input size.

**Key Insight**
The key insight is that we can calculate the total sum of all numbers from 1 to `n` in constant time, allowing us to maintain a running sum of the left side and compare it to the sum of the right side in linear time. This makes the solution efficient and scalable for large input sizes.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 66.31%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-10 |
| 💻 Language | Python |