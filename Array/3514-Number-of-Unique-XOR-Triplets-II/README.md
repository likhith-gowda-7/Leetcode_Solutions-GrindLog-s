# 3514. Number of Unique XOR Triplets II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/)


## 📝 Problem Description

You are given an integer array `nums`.

A **XOR triplet** is defined as the XOR of three elements `nums[i] XOR nums[j] XOR nums[k]` where `i <= j <= k`.

Return the number of **unique** XOR triplet values from all possible triplets `(i, j, k)`.

 

Example 1:**

**Input:** nums = [1,3]

**Output:** 2

**Explanation:**

The possible XOR triplet values are:

	`(0, 0, 0) &rarr; 1 XOR 1 XOR 1 = 1`

	`(0, 0, 1) &rarr; 1 XOR 1 XOR 3 = 3`

	`(0, 1, 1) &rarr; 1 XOR 3 XOR 3 = 1`

	`(1, 1, 1) &rarr; 3 XOR 3 XOR 3 = 3`

The unique XOR values are {1, 3}`. Thus, the output is 2.

Example 2:**

**Input:** nums = [6,7,8,9]

**Output:** 4

**Explanation:**

The possible XOR triplet values are {6, 7, 8, 9}`. Thus, the output is 4.

 

**Constraints:**

	- `1 <= nums.length <= 1500`

	- `1 <= nums[i] <= 1500`

## 🧠 Solution Explanation

**Intuition**
The solution uses a clever combination of two passes to count the unique XOR triplet values. The first pass generates all possible pair XORs, and the second pass extends each pair XOR with every element in the array. This approach allows us to efficiently count the unique XOR triplet values without explicitly generating all triplets.

**Approach**
1. Calculate the maximum possible XOR value `mx` by shifting the maximum value in the array by one bit to the left.
2. Initialize a boolean array `pair` of size `mx` to keep track of all possible pair XORs. Set `pair[a ^ b]` to `True` for each pair `(a, b)` in the array.
3. Initialize a boolean array `ans` of size `mx` to keep track of the unique XOR triplet values. For each pair XOR `x` in `pair`, extend it with every element `c` in the array by setting `ans[x ^ c]` to `True`.
4. Return the count of unique XOR triplet values by summing the `True` values in `ans`.

**Time Complexity**
O(n^2 * log(m)), where n is the length of the array and m is the maximum value in the array. This is because we have two nested loops in the first pass (O(n^2)) and one loop in the second pass (O(n log(m))) to generate the pair XORs and extend them with every element.

**Space Complexity**
O(m), where m is the maximum value in the array. This is because we need to store all possible pair XORs in the `pair` array.

**Key Insight**
The key insight is that we can use the property of XOR that `a ^ a = 0` and `a ^ 0 = a` to efficiently count the unique XOR triplet values. By generating all possible pair XORs in the first pass and extending them with every element in the second pass, we can avoid explicitly generating all triplets and reduce the time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4906 ms (Beats 80.23%) |
| 💾 Memory | 19.5 MB (Beats 63.95%) |
| 📅 Solved | 2026-07-25 |
| 💻 Language | Python |