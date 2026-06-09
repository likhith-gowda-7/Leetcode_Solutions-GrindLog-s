> 📌 **Cross-listed:** Primary location is [Array/3689-Maximum-Total-Subarray-Value-I](../../Array/3689-Maximum-Total-Subarray-Value-I). This problem also appears under: **Array**, **Greedy**

# 3689. Maximum Total Subarray Value I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-i/)


## 📝 Problem Description

You are given an integer array `nums` of length `n` and an integer `k`.

You need to choose **exactly** `k` non-empty subarrays `nums[l..r]` of `nums`. Subarrays may overlap, and the exact same subarray (same `l` and `r`) **can** be chosen more than once.

The **value** of a subarray `nums[l..r]` is defined as: `max(nums[l..r]) - min(nums[l..r])`.

The **total value** is the sum of the **values** of all chosen subarrays.

Return the **maximum** possible total value you can achieve.

 

Example 1:**

**Input:** nums = [1,3,2], k = 2

**Output:** 4

**Explanation:**

One optimal approach is:

	- Choose `nums[0..1] = [1, 3]`. The maximum is 3 and the minimum is 1, giving a value of `3 - 1 = 2`.

	- Choose `nums[0..2] = [1, 3, 2]`. The maximum is still 3 and the minimum is still 1, so the value is also `3 - 1 = 2`.

Adding these gives `2 + 2 = 4`.

Example 2:**

**Input:** nums = [4,2,5,1], k = 3

**Output:** 12

**Explanation:**

One optimal approach is:

	- Choose `nums[0..3] = [4, 2, 5, 1]`. The maximum is 5 and the minimum is 1, giving a value of `5 - 1 = 4`.

	- Choose `nums[0..3] = [4, 2, 5, 1]`. The maximum is 5 and the minimum is 1, so the value is also `4`.

	- Choose `nums[2..3] = [5, 1]`. The maximum is 5 and the minimum is 1, so the value is again `4`.

Adding these gives `4 + 4 + 4 = 12`.

 

**Constraints:**

	- `1 <= n == nums.length <= 5 * 10^​​​​​​​4`

	- `0 <= nums[i] <= 10^9`

	- `1 <= k <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution takes a greedy approach by choosing subarrays that consist of the maximum and minimum elements in the array. This is because the value of a subarray is maximized when the maximum and minimum elements are as far apart as possible. Since subarrays can overlap and the same subarray can be chosen multiple times, it's optimal to choose the subarray with the maximum and minimum elements as many times as possible.

**Approach**
1. Find the maximum element `max_element` in the array `nums`.
2. Find the minimum element `min_element` in the array `nums`.
3. Return the product of the difference between `max_element` and `min_element` and the number of subarrays to choose `k`.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because finding the maximum and minimum elements in the array takes linear time.

**Space Complexity**
O(1), because the solution only uses a constant amount of space to store the maximum and minimum elements, regardless of the size of the input array.

**Key Insight**
The key insight is that the value of a subarray is maximized when the maximum and minimum elements are as far apart as possible, and since subarrays can overlap and be chosen multiple times, it's optimal to choose the subarray with the maximum and minimum elements as many times as possible. This leads to a simple and efficient greedy solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 69.6%) |
| 💾 Memory | 26.4 MB (Beats 60%) |
| 📅 Solved | 2026-06-09 |
| 💻 Language | Python |