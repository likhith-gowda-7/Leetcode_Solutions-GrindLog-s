> 📌 **Cross-listed:** Primary location is [Array/3719-Longest-Balanced-Subarray-I](../../Array/3719-Longest-Balanced-Subarray-I). This problem also appears under: **Array**, **Hash Table**, **Divide and Conquer**, **Segment Tree**, **Prefix Sum**

# 3719. Longest Balanced Subarray I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-balanced-subarray-i/)


## 📝 Problem Description

You are given an integer array `nums`.

A **subarray** is called **balanced** if the number of **distinct even** numbers in the subarray is equal to the number of **distinct odd** numbers.

Return the length of the **longest** balanced subarray.

 

Example 1:**

**Input:** nums = [2,5,4,3]

**Output:** 4

**Explanation:**

	- The longest balanced subarray is `[2, 5, 4, 3]`.

	- It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[5, 3]`. Thus, the answer is 4.

Example 2:**

**Input:** nums = [3,2,2,5,4]

**Output:** 5

**Explanation:**

	- The longest balanced subarray is `[3, 2, 2, 5, 4]`.

	- It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[3, 5]`. Thus, the answer is 5.

Example 3:**

**Input:** nums = [1,2,3,2]

**Output:** 3

**Explanation:**

	- The longest balanced subarray is `[2, 3, 2]`.

	- It has 1 distinct even number `[2]` and 1 distinct odd number `[3]`. Thus, the answer is 3.

 

**Constraints:**

	- `1 <= nums.length <= 1500`

	- `1 <= nums[i] <= 10^5`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1269 ms (Beats 58.75%) |
| 💾 Memory | 19.6 MB (Beats 18.51%) |
| 📅 Solved | 2026-02-10 |
| 💻 Language | Python |