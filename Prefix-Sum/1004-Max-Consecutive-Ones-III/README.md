> 📌 **Cross-listed:** Primary location is [Array/1004-Max-Consecutive-Ones-III](../../Array/1004-Max-Consecutive-Ones-III). This problem also appears under: **Array**, **Binary Search**, **Sliding Window**, **Prefix Sum**

# 1004. Max Consecutive Ones III


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)


## 📝 Problem Description

Given a binary array `nums` and an integer `k`, return *the maximum number of consecutive *`1`*'s in the array if you can flip at most* `k` `0`'s.

 

Example 1:**

```

**Input:** nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
**Output:** 6
**Explanation:** [1,1,1,0,0,**1**,1,1,1,1,**1**]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

Example 2:**

```

**Input:** nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
**Output:** 10
**Explanation:** [0,0,1,1,**1**,**1**,1,1,1,**1**,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `nums[i]` is either `0` or `1`.

	- `0 <= k <= nums.length`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 67 ms (Beats 28.81%) |
| 💾 Memory | 18.4 MB (Beats 100%) |
| 📅 Solved | 2025-03-09 |
| 💻 Language | Python |