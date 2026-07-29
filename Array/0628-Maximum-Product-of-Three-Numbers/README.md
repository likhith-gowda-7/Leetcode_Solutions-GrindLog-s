# 628. Maximum Product of Three Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/)


## 📝 Problem Description

Given an integer array `nums`, *find three numbers whose product is maximum and return the maximum product*.

 

Example 1:**

```
**Input:** nums = [1,2,3]
**Output:** 6

```
Example 2:**

```
**Input:** nums = [1,2,3,4]
**Output:** 24

```
Example 3:**

```
**Input:** nums = [-1,-2,-3]
**Output:** -6

```

 

**Constraints:**

	- `3 <= nums.length <= 10^4`

	- `-1000 <= nums[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
This solution works by maintaining three variables to track the maximum numbers and two variables to track the minimum numbers in the array. The idea is that the maximum product can be achieved by either multiplying the three maximum numbers or by multiplying two maximum numbers and two minimum numbers (since negative numbers can result in a maximum product).

**Approach**
1. Initialize four variables: `max1`, `max2`, `max3` to store the three maximum numbers, and `min1`, `min2` to store the two minimum numbers.
2. Iterate through the array, updating the maximum and minimum numbers as needed:
   - If a number is greater than `max1`, update `max3`, `max2`, and `max1` accordingly.
   - If a number is greater than `max2` but not `max1`, update `max3` and `max2`.
   - If a number is greater than `max3` but not `max1` or `max2`, update `max3`.
   - If a number is less than `min1`, update `min2` and `min1`.
   - If a number is less than `min2` but not `min1`, update `min2`.
3. After iterating through the array, return the maximum product, which can be either `max1*max2*max3` or `max1*min1*min2`.

**Time Complexity**
O(n), where n is the length of the array, since we only need to iterate through the array once to update the maximum and minimum numbers.

**Space Complexity**
O(1), since we only need to use a constant amount of space to store the maximum and minimum numbers.

**Key Insight**
The key insight here is that we can take advantage of the fact that negative numbers can result in a maximum product by considering the product of two maximum numbers and two minimum numbers. This allows us to simplify the problem and avoid the need to consider all possible combinations of numbers.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 10 ms (Beats 82.56%) |
| 💾 Memory | 20.4 MB (Beats 43.9%) |
| 📅 Solved | 2026-07-29 |
| 💻 Language | Python |