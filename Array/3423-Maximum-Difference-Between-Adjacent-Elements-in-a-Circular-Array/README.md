# 3423. Maximum Difference Between Adjacent Elements in a Circular Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/)


## 📝 Problem Description

Given a **circular** array `nums`, find the **maximum** absolute difference between adjacent elements.

**Note**: In a circular array, the first and last elements are adjacent.

 

Example 1:**

**Input:** nums = [1,2,4]

**Output:** 3

**Explanation:**

Because `nums` is circular, `nums[0]` and `nums[2]` are adjacent. They have the maximum absolute difference of `|4 - 1| = 3`.

Example 2:**

**Input:** nums = [-5,-10,-5]

**Output:** 5

**Explanation:**

The adjacent elements `nums[0]` and `nums[1]` have the maximum absolute difference of `|-5 - (-10)| = 5`.

 

**Constraints:**

	- `2 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by treating the circular array as a linear array, appending the first element to the end, and then iterating through the array to find the maximum absolute difference between adjacent elements.

**Approach**
1. Calculate the length of the input array `n`.
2. Append the first element of the array to the end of the array to simulate a circular array.
3. Initialize a variable `maxi` to store the maximum absolute difference found so far.
4. Iterate through the array from the first element to the second last element (inclusive).
5. For each element, calculate the absolute difference with the next element.
6. If the calculated difference is greater than the current `maxi`, update `maxi` with the new difference.
7. Return the final value of `maxi` as the maximum absolute difference between adjacent elements.

**Time Complexity**
O(n), where n is the length of the input array. This is because we are iterating through the array once to find the maximum absolute difference.

**Space Complexity**
O(1), excluding the input array. We are modifying the input array by appending an element to the end, but this does not affect the space complexity.

**Key Insight**
The key insight is that treating the circular array as a linear array by appending the first element to the end allows us to use a simple iterative approach to find the maximum absolute difference between adjacent elements. This approach avoids the need for complex logic to handle the circular nature of the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2 ms (Beats 46.83%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-06-12 |
| 💻 Language | Python |