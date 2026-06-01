# 523. Continuous Subarray Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/continuous-subarray-sum/)


## 📝 Problem Description

Given an integer array nums and an integer k, return `true` *if *`nums`* has a **good subarray** or *`false`* otherwise*.

A **good subarray** is a subarray where:

	- its length is **at least two**, and

	- the sum of the elements of the subarray is a multiple of `k`.

**Note** that:

	- A **subarray** is a contiguous part of the array.

	- An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is **always** a multiple of `k`.

 

Example 1:**

```

**Input:** nums = [23,2,4,6,7], k = 6
**Output:** true
**Explanation:** [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

```

Example 2:**

```

**Input:** nums = [23,2,6,4,7], k = 6
**Output:** true
**Explanation:** [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

```

Example 3:**

```

**Input:** nums = [23,2,6,4,7], k = 13
**Output:** false

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`

	- `0 <= sum(nums[i]) <= 2^31 - 1`

	- `1 <= k <= 2^31 - 1`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 49 ms (Beats 82.05%) |
| 💾 Memory | 38 MB (Beats 96.02%) |
| 📅 Solved | 2025-02-10 |
| 💻 Language | Python |