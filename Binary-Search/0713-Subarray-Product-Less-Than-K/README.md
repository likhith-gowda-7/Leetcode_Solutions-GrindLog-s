> 📌 **Cross-listed:** Primary location is [Array/0713-Subarray-Product-Less-Than-K](../../Array/0713-Subarray-Product-Less-Than-K). This problem also appears under: **Array**, **Binary Search**, **Sliding Window**, **Prefix Sum**

# 713. Subarray Product Less Than K


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/)


## 📝 Problem Description

Given an array of integers `nums` and an integer `k`, return *the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than *`k`.

 

Example 1:**

```

**Input:** nums = [10,5,2,6], k = 100
**Output:** 8
**Explanation:** The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

```

Example 2:**

```

**Input:** nums = [1,2,3], k = 0
**Output:** 0

```

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `1 <= nums[i] <= 1000`

	- `0 <= k <= 10^6`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 51 ms (Beats 87.81%) |
| 💾 Memory | 19.6 MB (Beats 100%) |
| 📅 Solved | 2024-12-19 |
| 💻 Language | Python |