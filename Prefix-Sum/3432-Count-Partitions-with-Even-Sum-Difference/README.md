> 📌 **Cross-listed:** Primary location is [Array/3432-Count-Partitions-with-Even-Sum-Difference](../../Array/3432-Count-Partitions-with-Even-Sum-Difference). This problem also appears under: **Array**, **Math**, **Prefix Sum**

# 3432. Count Partitions with Even Sum Difference


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-partitions-with-even-sum-difference/)


## 📝 Problem Description

You are given an integer array `nums` of length `n`.

A **partition** is defined as an index `i` where `0 <= i < n - 1`, splitting the array into two **non-empty** subarrays such that:

	- Left subarray contains indices `[0, i]`.

	- Right subarray contains indices `[i + 1, n - 1]`.

Return the number of **partitions** where the **difference** between the **sum** of the left and right subarrays is **even**.

 

Example 1:**

**Input:** nums = [10,10,3,7,6]

**Output:** 4

**Explanation:**

The 4 partitions are:

	- `[10]`, `[10, 3, 7, 6]` with a sum difference of `10 - 26 = -16`, which is even.

	- `[10, 10]`, `[3, 7, 6]` with a sum difference of `20 - 16 = 4`, which is even.

	- `[10, 10, 3]`, `[7, 6]` with a sum difference of `23 - 13 = 10`, which is even.

	- `[10, 10, 3, 7]`, `[6]` with a sum difference of `30 - 6 = 24`, which is even.

Example 2:**

**Input:** nums = [1,2,2]

**Output:** 0

**Explanation:**

No partition results in an even sum difference.

Example 3:**

**Input:** nums = [2,4,6,8]

**Output:** 3

**Explanation:**

All partitions result in an even sum difference.

 

**Constraints:**

	- `2 <= n == nums.length <= 100`

	- `1 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution uses the concept of prefix sum to efficiently calculate the sum of the left and right subarrays. By maintaining the running sum of the left subarray and the total sum of the array, we can easily compute the sum of the right subarray. The key insight is that we only need to consider the difference between the sums of the left and right subarrays, which can be efficiently calculated using the prefix sum.

**Approach**
1. Initialize two variables `left` and `right` to store the sum of the left subarray and the total sum of the array, respectively.
2. Iterate through the array, excluding the last element.
3. For each element, add it to `left` and subtract it from `right` to update the sums.
4. Calculate the absolute difference between `left` and `right` and check if it is even.
5. If the difference is even, increment the result counter `res`.
6. Return the final count of partitions with even sum difference.

**Time Complexity**
O(n), where n is the length of the input array. This is because we only need to iterate through the array once to calculate the prefix sum and check for even differences.

**Space Complexity**
O(1), as we only use a constant amount of space to store the prefix sum variables `left` and `right`.

**Key Insight**
The key insight is that we can efficiently calculate the sum of the right subarray by subtracting the current element from the total sum of the array, which is stored in `right`. This allows us to avoid recalculating the sum of the right subarray for each element, resulting in a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-12-06 |
| 💻 Language | Python |