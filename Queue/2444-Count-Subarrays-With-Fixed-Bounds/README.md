> 📌 **Cross-listed:** Primary location is [Array/2444-Count-Subarrays-With-Fixed-Bounds](../../Array/2444-Count-Subarrays-With-Fixed-Bounds). This problem also appears under: **Array**, **Queue**, **Sliding Window**, **Monotonic Queue**

# 2444. Count Subarrays With Fixed Bounds


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Monotonic Queue](https://img.shields.io/badge/Monotonic%20Queue-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)


## 📝 Problem Description

You are given an integer array `nums` and two integers `minK` and `maxK`.

A **fixed-bound subarray** of `nums` is a subarray that satisfies the following conditions:

	- The **minimum** value in the subarray is equal to `minK`.

	- The **maximum** value in the subarray is equal to `maxK`.

Return *the **number** of fixed-bound subarrays*.

A **subarray** is a **contiguous** part of an array.

 

Example 1:**

```

**Input:** nums = [1,3,5,2,7,5], minK = 1, maxK = 5
**Output:** 2
**Explanation:** The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

```

Example 2:**

```

**Input:** nums = [1,1,1,1], minK = 1, maxK = 1
**Output:** 10
**Explanation:** Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

```

 

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `1 <= nums[i], minK, maxK <= 10^6`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 167 ms (Beats 10.6%) |
| 💾 Memory | 28.9 MB (Beats 100%) |
| 📅 Solved | 2025-04-01 |
| 💻 Language | Python |