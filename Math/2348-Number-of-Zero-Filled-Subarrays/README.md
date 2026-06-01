> 📌 **Cross-listed:** Primary location is [Array/2348-Number-of-Zero-Filled-Subarrays](../../Array/2348-Number-of-Zero-Filled-Subarrays). This problem also appears under: **Array**, **Math**

# 2348. Number of Zero-Filled Subarrays


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-zero-filled-subarrays/)


## 📝 Problem Description

Given an integer array `nums`, return *the number of **subarrays** filled with *`0`.

A **subarray** is a contiguous non-empty sequence of elements within an array.

 

Example 1:**

```

**Input:** nums = [1,3,0,0,2,0,0,4]
**Output:** 6
**Explanation:** 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
```

Example 2:**

```

**Input:** nums = [0,0,0,2,0,0]
**Output:** 9
**Explanation:
**There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

```

Example 3:**

```

**Input:** nums = [2,10,2019]
**Output:** 0
**Explanation:** There is no subarray filled with 0. Therefore, we return 0.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 23 ms (Beats 98.11%) |
| 💾 Memory | 28.3 MB (Beats 99.53%) |
| 📅 Solved | 2025-08-19 |
| 💻 Language | Python |