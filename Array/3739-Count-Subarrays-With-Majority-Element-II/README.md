# 3739. Count Subarrays With Majority Element II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-ii/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `target`.

Return the number of **subarrays** of `nums` in which `target` is the **majority element**.

The **majority element** of a subarray is the element that appears **strictly more than half** of the times in that subarray.

 

Example 1:**

**Input:** nums = [1,2,2,3], target = 2

**Output:** 5

**Explanation:**

Valid subarrays with `target = 2` as the majority element:

	- `nums[1..1] = [2]`

	- `nums[2..2] = [2]`

	- `nums[1..2] = [2,2]`

	- `nums[0..2] = [1,2,2]`

	- `nums[1..3] = [2,2,3]`

So there are 5 such subarrays.

Example 2:**

**Input:** nums = [1,1,1,1], target = 1

**Output:** 10

**Explanation: **

**​​​​​​​**All 10 subarrays have 1 as the majority element.

Example 3:**

**Input:** nums = [1,2,3], target = 4

**Output:** 0

**Explanation:**

`target = 4` does not appear in `nums` at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.

 

**Constraints:**

	- `1 <= nums.length <= 10^​​​​​​​5`

	- `1 <= nums[i] <= 10^​​​​​​​9`

	- `1 <= target <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to count the number of subarrays in which the target element is the majority element. To solve this, we can use a clever technique involving prefix sums and a frequency array to efficiently count the valid subarrays.

**Approach**
1. First, we iterate through the array and mark the indices of the target element with a value of 1 and other elements with a value of -1.
2. Then, we calculate the prefix sum array `pref`, where `pref[i]` represents the sum of elements from index 0 to `i`.
3. We initialize a frequency array `freq` to keep track of the frequency of each prefix sum value.
4. We iterate through the prefix sum array and for each prefix sum value, we update the valid count by adding the frequency of the previous prefix sum value minus the frequency of the current prefix sum value.
5. We also update the frequency array and the valid count for each prefix sum value.

**Time Complexity**
O(n), where n is the length of the array. This is because we make three passes through the array: one to mark the indices, one to calculate the prefix sum array, and one to iterate through the prefix sum array.

**Space Complexity**
O(n), where n is the length of the array. This is because we need to store the prefix sum array and the frequency array.

**Key Insight**
The key insight is to use the prefix sum array to efficiently count the valid subarrays. By iterating through the prefix sum array, we can update the valid count by adding or subtracting the frequency of the previous prefix sum value, which allows us to count the valid subarrays in O(n) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 135 ms (Beats 65.49%) |
| 💾 Memory | 32.4 MB (Beats 90.85%) |
| 📅 Solved | 2026-06-26 |
| 💻 Language | Python |