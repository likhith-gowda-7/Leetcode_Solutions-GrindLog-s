# 1588. Sum of All Odd Length Subarrays


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)


## 📝 Problem Description

Given an array of positive integers `arr`, return *the sum of all possible **odd-length subarrays** of *`arr`.

A **subarray** is a contiguous subsequence of the array.

 

Example 1:**

```

**Input:** arr = [1,4,2,5,3]
**Output:** 58
**Explanation: **The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```

Example 2:**

```

**Input:** arr = [1,2]
**Output:** 3
**Explanation: **There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
```

Example 3:**

```

**Input:** arr = [10,11,12]
**Output:** 66

```

 

**Constraints:**

	- `1 <= arr.length <= 100`

	- `1 <= arr[i] <= 1000`

 

**Follow up:**

Could you solve this problem in O(n) time complexity?

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-09 |
| 💻 Language | Python |