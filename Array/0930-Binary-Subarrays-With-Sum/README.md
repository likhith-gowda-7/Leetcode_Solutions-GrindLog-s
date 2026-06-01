# 930. Binary Subarrays With Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-subarrays-with-sum/)


## 📝 Problem Description

Given a binary array `nums` and an integer `goal`, return *the number of non-empty **subarrays** with a sum* `goal`.

A **subarray** is a contiguous part of the array.

 

Example 1:**

```

**Input:** nums = [1,0,1,0,1], goal = 2
**Output:** 4
**Explanation:** The 4 subarrays are bolded and underlined below:
[**1,0,1**,0,1]
[**1,0,1,0**,1]
[1,**0,1,0,1**]
[1,0,**1,0,1**]

```

Example 2:**

```

**Input:** nums = [0,0,0,0,0], goal = 0
**Output:** 15

```

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `nums[i]` is either `0` or `1`.

	- `0 <= goal <= nums.length`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 26 ms (Beats 92.85%) |
| 💾 Memory | 21.5 MB (Beats 55.55%) |
| 📅 Solved | 2025-03-11 |
| 💻 Language | Python |