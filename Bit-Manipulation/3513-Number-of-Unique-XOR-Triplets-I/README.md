> 📌 **Cross-listed:** Primary location is [Array/3513-Number-of-Unique-XOR-Triplets-I](../../Array/3513-Number-of-Unique-XOR-Triplets-I). This problem also appears under: **Array**, **Math**, **Bit Manipulation**

# 3513. Number of Unique XOR Triplets I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-unique-xor-triplets-i/)


## 📝 Problem Description

You are given an integer array `nums` of length `n`, where `nums` is a **permutation** of the numbers in the range `[1, n]`.

A **XOR triplet** is defined as the XOR of three elements `nums[i] XOR nums[j] XOR nums[k]` where `i <= j <= k`.

Return the number of **unique** XOR triplet values from all possible triplets `(i, j, k)`.

 

Example 1:**

**Input:** nums = [1,2]

**Output:** 2

**Explanation:**

The possible XOR triplet values are:

	- `(0, 0, 0) &rarr; 1 XOR 1 XOR 1 = 1`

	- `(0, 0, 1) &rarr; 1 XOR 1 XOR 2 = 2`

	- `(0, 1, 1) &rarr; 1 XOR 2 XOR 2 = 1`

	- `(1, 1, 1) &rarr; 2 XOR 2 XOR 2 = 2`

The unique XOR values are `{1, 2}`, so the output is 2.

Example 2:**

**Input:** nums = [3,1,2]

**Output:** 4

**Explanation:**

The possible XOR triplet values include:

	- `(0, 0, 0) &rarr; 3 XOR 3 XOR 3 = 3`

	- `(0, 0, 1) &rarr; 3 XOR 3 XOR 1 = 1`

	- `(0, 0, 2) &rarr; 3 XOR 3 XOR 2 = 2`

	- `(0, 1, 2) &rarr; 3 XOR 1 XOR 2 = 0`

The unique XOR values are `{0, 1, 2, 3}`, so the output is 4.

 

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= n`

	- `nums` is a permutation of integers from `1` to `n`.

## 🧠 Solution Explanation

**Intuition**
The solution leverages the property of XOR operation that `a XOR a = 0` and `a XOR 0 = a`. This allows us to count the unique XOR triplet values by finding the number of possible XOR combinations of three elements in the array.

**Approach**
1. Check if the length of the array is less than 3. If true, return the length as there can be at most `n` unique XOR values (each element can be XORed with itself).
2. Calculate the maximum power of 2 that is less than or equal to the length of the array. This is done by shifting the bits of the number 2 to the left until we reach the desired power.
3. The maximum power of 2 represents the number of unique XOR triplet values.

**Time Complexity**
O(1) - The solution involves a constant number of operations, regardless of the input size.

**Space Complexity**
O(1) - The solution uses a constant amount of space to store the variables, regardless of the input size.

**Key Insight**
The key insight is that the number of unique XOR triplet values is equal to the maximum power of 2 that is less than or equal to the length of the array. This is because each element can be XORed with itself, resulting in 0, and each pair of elements can be XORed with each other, resulting in a unique value. The maximum power of 2 represents the number of possible XOR combinations of three elements.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 34.1 MB (Beats 27.12%) |
| 📅 Solved | 2026-07-23 |
| 💻 Language | Python |