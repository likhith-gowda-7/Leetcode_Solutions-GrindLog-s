# 219. Contains Duplicate II


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return `true` *if there are two **distinct indices** *`i`* and *`j`* in the array such that *`nums[i] == nums[j]`* and *`abs(i - j) <= k`.

 

Example 1:**

```

**Input:** nums = [1,2,3,1], k = 3
**Output:** true

```

Example 2:**

```

**Input:** nums = [1,0,1,1], k = 1
**Output:** true

```

Example 3:**

```

**Input:** nums = [1,2,3,1,2,3], k = 2
**Output:** false

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

	- `0 <= k <= 10^5`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 27 ms (Beats 88.64%) |
| 💾 Memory | 36.7 MB (Beats 29.38%) |
| 📅 Solved | 2025-11-26 |
| 💻 Language | Python |