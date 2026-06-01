# 974. Subarray Sums Divisible by K


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/subarray-sums-divisible-by-k/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return *the number of non-empty **subarrays** that have a sum divisible by *`k`.

A **subarray** is a **contiguous** part of an array.

 

Example 1:**

```

**Input:** nums = [4,5,0,-2,-3,1], k = 5
**Output:** 7
**Explanation:** There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

```

Example 2:**

```

**Input:** nums = [5], k = 9
**Output:** 0

```

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `-10^4 <= nums[i] <= 10^4`

	- `2 <= k <= 10^4`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 33 ms (Beats 46.79%) |
| 💾 Memory | 21 MB (Beats 100%) |
| 📅 Solved | 2025-11-30 |
| 💻 Language | Python |