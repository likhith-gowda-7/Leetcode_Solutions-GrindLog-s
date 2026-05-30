# 1425. Constrained Subsequence Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/constrained-subsequence-sum/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return the maximum sum of a **non-empty** subsequence of that array such that for every two **consecutive** integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` is satisfied.

A *subsequence* of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:**

```

**Input:** nums = [10,2,-10,5,20], k = 2
**Output:** 37
**Explanation:** The subsequence is [10, 2, 5, 20].

```

Example 2:**

```

**Input:** nums = [-1,-2,-3], k = 1
**Output:** -1
**Explanation:** The subsequence must be non-empty, so we choose the largest number.

```

Example 3:**

```

**Input:** nums = [10,-2,-10,-5,20], k = 2
**Output:** 23
**Explanation:** The subsequence is [10, -2, -5, 20].

```

 

**Constraints:**

	- `1 <= k <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 312 ms (Beats 34.48%) |
| 💾 Memory | 28.9 MB (Beats 100%) |
| 📅 Solved | 2025-04-07 |
| 💻 Language | Python |