# 594. Longest Harmonious Subsequence


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-harmonious-subsequence/)


## 📝 Problem Description

We define a harmonious array as an array where the difference between its maximum value and its minimum value is **exactly** `1`.

Given an integer array `nums`, return the length of its longest harmonious subsequence among all its possible subsequences.

 

Example 1:**

**Input:** nums = [1,3,2,2,5,2,3,7]

**Output:** 5

**Explanation:**

The longest harmonious subsequence is `[3,2,2,2,3]`.

Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** 2

**Explanation:**

The longest harmonious subsequences are `[1,2]`, `[2,3]`, and `[3,4]`, all of which have a length of 2.

Example 3:**

**Input:** nums = [1,1,1,1]

**Output:** 0

**Explanation:**

No harmonic subsequence exists.

 

**Constraints:**

	- `1 <= nums.length <= 2 * 10^4`

	- `-10^9 <= nums[i] <= 10^9`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 12 ms (Beats 97.61%) |
| 💾 Memory | 19.4 MB (Beats 100%) |
| 📅 Solved | 2025-06-30 |
| 💻 Language | Python |