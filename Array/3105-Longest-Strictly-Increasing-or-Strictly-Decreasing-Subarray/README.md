# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)


## 📝 Problem Description

You are given an array of integers `nums`. Return *the length of the **longest** subarray of *`nums`* which is either **strictly increasing** or **strictly decreasing***.

 

Example 1:**

**Input:** nums = [1,4,3,3,2]

**Output:** 2

**Explanation:**

The strictly increasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, and `[1,4]`.

The strictly decreasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, `[3,2]`, and `[4,3]`.

Hence, we return `2`.

Example 2:**

**Input:** nums = [3,3,3,3]

**Output:** 1

**Explanation:**

The strictly increasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`.

The strictly decreasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`.

Hence, we return `1`.

Example 3:**

**Input:** nums = [3,2,1]

**Output:** 3

**Explanation:**

The strictly increasing subarrays of `nums` are `[3]`, `[2]`, and `[1]`.

The strictly decreasing subarrays of `nums` are `[3]`, `[2]`, `[1]`, `[3,2]`, `[2,1]`, and `[3,2,1]`.

Hence, we return `3`.

 

**Constraints:**

	- `1 <= nums.length <= 50`

	- `1 <= nums[i] <= 50`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the array twice, once for strictly increasing subarrays and once for strictly decreasing subarrays. It keeps track of the maximum length of such subarrays seen so far.

**Approach**
1. Check if the array has less than 2 elements. If so, return 1 as the longest subarray is the entire array itself.
2. Initialize `maxi` to 1, which will store the maximum length of a monotonic subarray seen so far, and `count` to 1, which will store the length of the current monotonic subarray.
3. Iterate through the array from the second element to the end. If the current element is greater than the previous one, increment `count` and update `maxi` if `count` is greater than `maxi`.
4. If the current element is not greater than the previous one, reset `count` to 1.
5. Repeat steps 3-4 for strictly decreasing subarrays by checking if the current element is less than the previous one.
6. Return `maxi`, which stores the maximum length of a monotonic subarray.

**Time Complexity**
O(n), where n is the length of the array. This is because we are iterating through the array twice, once for increasing subarrays and once for decreasing subarrays.

**Space Complexity**
O(1), as we are using a constant amount of space to store `maxi` and `count`.

**Key Insight**
The key insight is that we can find the longest monotonic subarray by iterating through the array twice, once for increasing subarrays and once for decreasing subarrays. This is because a monotonic subarray can only be either increasing or decreasing, and we can find the longest such subarray by keeping track of the maximum length seen so far.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-02-03 |
| 💻 Language | Python |