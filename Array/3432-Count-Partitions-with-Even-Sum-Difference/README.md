# 3432. Count Partitions with Even Sum Difference


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-partitions-with-even-sum-difference/)


## 📝 Problem Description

You are given an integer array `nums` of length `n`.

A **partition** is defined as an index `i` where `0 <= i < n - 1`, splitting the array into two **non-empty** subarrays such that:

	- Left subarray contains indices `[0, i]`.

	- Right subarray contains indices `[i + 1, n - 1]`.

Return the number of **partitions** where the **difference** between the **sum** of the left and right subarrays is **even**.

 

Example 1:**

**Input:** nums = [10,10,3,7,6]

**Output:** 4

**Explanation:**

The 4 partitions are:

	- `[10]`, `[10, 3, 7, 6]` with a sum difference of `10 - 26 = -16`, which is even.

	- `[10, 10]`, `[3, 7, 6]` with a sum difference of `20 - 16 = 4`, which is even.

	- `[10, 10, 3]`, `[7, 6]` with a sum difference of `23 - 13 = 10`, which is even.

	- `[10, 10, 3, 7]`, `[6]` with a sum difference of `30 - 6 = 24`, which is even.

Example 2:**

**Input:** nums = [1,2,2]

**Output:** 0

**Explanation:**

No partition results in an even sum difference.

Example 3:**

**Input:** nums = [2,4,6,8]

**Output:** 3

**Explanation:**

All partitions result in an even sum difference.

 

**Constraints:**

	- `2 <= n == nums.length <= 100`

	- `1 <= nums[i] <= 100`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-12-06 |
| 💻 Language | Python |