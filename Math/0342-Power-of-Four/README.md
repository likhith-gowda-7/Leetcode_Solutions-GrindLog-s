# 342. Power of Four


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/power-of-four/)


## 📝 Problem Description

Given an integer `n`, return *`true` if it is a power of four. Otherwise, return `false`*.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4^x`.

 

Example 1:**

```
**Input:** n = 16
**Output:** true

```
Example 2:**

```
**Input:** n = 5
**Output:** false

```
Example 3:**

```
**Input:** n = 1
**Output:** true

```

 

**Constraints:**

	- `-2^31 <= n <= 2^31 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## 🧠 Solution Explanation

**Intuition**
This solution works by repeatedly dividing the input number `n` by 4 as long as it's divisible evenly (i.e., `n % 4 == 0`). If `n` ever becomes 1, it means `n` is a power of four. Otherwise, it's not a power of four.

**Approach**
1. Check if `n` is less than or equal to 0. If so, return `False` immediately, as negative numbers and zero cannot be powers of four.
2. While `n` is greater than 1:
   a. Check if `n` is divisible by 4 (i.e., `n % 4 == 0`).
   b. If it is, divide `n` by 4 (i.e., `n //= 4`).
   c. If it's not divisible by 4, return `False`, as `n` cannot be a power of four.
3. If `n` becomes 1, return `True`, indicating that `n` is a power of four.

**Time Complexity**
O(log n) - The number of divisions by 4 is proportional to the number of times we can divide `n` by 4 before reaching 1. This is equivalent to the number of bits in the binary representation of `n`, which is log(n) in base 2.

**Space Complexity**
O(1) - We only use a constant amount of space to store the input number `n` and a few temporary variables.

**Key Insight**
The key insight here is that a power of four can be uniquely represented as a binary number with exactly one 2-bit (i.e., 10 in binary) and all other bits being zeros. This is because 4 = 2^2, and any power of four can be written as 4^x = (2^2)^x = 2^(2x).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-08-15 |
| 💻 Language | Python |