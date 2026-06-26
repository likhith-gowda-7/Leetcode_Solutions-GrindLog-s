# 3737. Count Subarrays With Majority Element I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-i/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `target`.

Return the number of **subarrays** of `nums` in which `target` is the **majority element**.

The **majority element** of a subarray is the element that appears **strictly** **more than half** of the times in that subarray.

 

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

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 10^​​​​​​​9`

	- `1 <= target <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer approach to generate all possible subarrays of the input array, and then checks if the target element is the majority element in each subarray. The key insight is that we only need to check if the target element appears more than half of the time in the subarray, which simplifies the problem.

**Approach**
1. Initialize a variable `ans` to store the count of subarrays with the target element as the majority element.
2. Iterate over the array using a left pointer `l` from the start to the end.
3. For each left pointer position, use a right pointer `r` to generate all possible subarrays starting from the left pointer position.
4. For each subarray, count the occurrences of the target element using a variable `target_count`.
5. If the target element appears more than half of the time in the subarray (i.e., `target_count > length // 2`), increment the `ans` variable.
6. Repeat steps 3-5 for all subarrays starting from each left pointer position.
7. Return the total count of subarrays with the target element as the majority element.

**Time Complexity**
O(n^2), where n is the length of the input array. This is because we are generating all possible subarrays of the input array, which takes O(n^2) time.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the variables `ans`, `l`, `r`, `target_count`, and `length`.

**Key Insight**
The key insight is that we only need to check if the target element appears more than half of the time in the subarray, which simplifies the problem and allows us to use a simple two-pointer approach. This is because the majority element of a subarray must appear more than half of the time in that subarray.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1909 ms (Beats 32.88%) |
| 💾 Memory | 19.4 MB (Beats 90.54%) |
| 📅 Solved | 2026-06-25 |
| 💻 Language | Python |