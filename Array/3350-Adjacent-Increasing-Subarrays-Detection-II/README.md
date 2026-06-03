# 3350. Adjacent Increasing Subarrays Detection II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/)


## 📝 Problem Description

Given an array `nums` of `n` integers, your task is to find the **maximum** value of `k` for which there exist **two** adjacent subarrays of length `k` each, such that both subarrays are **strictly** **increasing**. Specifically, check if there are **two** subarrays of length `k` starting at indices `a` and `b` (`a < b`), where:

	- Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly increasing**.

	- The subarrays must be **adjacent**, meaning `b = a + k`.

Return the **maximum** *possible* value of `k`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

 

Example 1:**

**Input:** nums = [2,5,7,8,9,2,3,4,3,1]

**Output:** 3

**Explanation:**

	- The subarray starting at index 2 is `[7, 8, 9]`, which is strictly increasing.

	- The subarray starting at index 5 is `[2, 3, 4]`, which is also strictly increasing.

	- These two subarrays are adjacent, and 3 is the **maximum** possible value of `k` for which two such adjacent strictly increasing subarrays exist.

Example 2:**

**Input:** nums = [1,2,3,4,4,4,4,5,6,7]

**Output:** 2

**Explanation:**

	- The subarray starting at index 0 is `[1, 2]`, which is strictly increasing.

	- The subarray starting at index 2 is `[3, 4]`, which is also strictly increasing.

	- These two subarrays are adjacent, and 2 is the **maximum** possible value of `k` for which two such adjacent strictly increasing subarrays exist.

 

**Constraints:**

	- `2 <= nums.length <= 2 * 10^5`

	- `-10^9 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a binary search approach to find the maximum possible value of `k` for which there exist two adjacent strictly increasing subarrays of length `k`. The idea is to check if there are two such subarrays for a given `k` and adjust the search range accordingly.

**Approach**
1. Define a helper function `sub_detection` that checks if there are two adjacent strictly increasing subarrays of length `k` starting at indices `a` and `b` (`a < b`).
2. Initialize variables `prev_sub`, `sub_max`, and `sub_size` to keep track of the previous subarray, maximum element, and current subarray size, respectively.
3. Iterate through the array `nums` and update `sub_max` and `sub_size` accordingly.
4. Call the `sub_detection` function with the current `sub_size` and `nums` to check if there are two adjacent strictly increasing subarrays of length `k`.
5. If `sub_detection` returns `True`, update the search range and return the maximum possible value of `k`.
6. If `sub_detection` returns `False`, adjust the search range and repeat steps 4-6 until the search range is empty.

**Time Complexity**
The time complexity of the solution is O(n log m), where n is the length of the array `nums` and m is the maximum possible value of `k`. This is because the binary search approach reduces the search range by half at each step, resulting in a logarithmic number of iterations. The `sub_detection` function has a time complexity of O(n) because it iterates through the array `nums` once.

**Space Complexity**
The space complexity of the solution is O(1), as it only uses a constant amount of space to store the variables `prev_sub`, `sub_max`, and `sub_size`.

**Key Insight**
The key insight is to use a binary search approach to find the maximum possible value of `k` by checking if there are two adjacent strictly increasing subarrays of length `k` for a given `k`. This approach reduces the search space and allows us to find the maximum possible value of `k` efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3492 ms (Beats 5.29%) |
| 💾 Memory | 45.9 MB (Beats 100%) |
| 📅 Solved | 2025-10-15 |
| 💻 Language | Python |