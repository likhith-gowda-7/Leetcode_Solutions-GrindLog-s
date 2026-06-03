# 3370. Smallest Number With All Set Bits


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-number-with-all-set-bits/)


## 📝 Problem Description

You are given a *positive* number `n`.

Return the **smallest** number `x` **greater than** or **equal to** `n`, such that the binary representation of `x` contains only set bits

 

Example 1:**

**Input:** n = 5

**Output:** 7

**Explanation:**

The binary representation of 7 is `"111"`.

Example 2:**

**Input:** n = 10

**Output:** 15

**Explanation:**

The binary representation of 15 is `"1111"`.

Example 3:**

**Input:** n = 3

**Output:** 3

**Explanation:**

The binary representation of 3 is `"11"`.

 

**Constraints:**

	- `1 <= n <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution works by converting the input number to binary, then creating a new binary string with all set bits. This new string is then converted back to decimal, resulting in the smallest number with all set bits greater than or equal to the input number.

**Approach**
1. Convert the input number `n` to its binary representation using the `bin()` function.
2. Remove the '0b' prefix from the binary string, leaving only the binary digits.
3. Create a new binary string `s` with all set bits by repeating the character '1' the same number of times as the length of the original binary string.
4. Convert the new binary string `s` back to decimal using the `int()` function with base 2.

**Time Complexity**
O(1) - The operations involved (string manipulation and conversion) are constant-time, regardless of the size of the input number.

**Space Complexity**
O(1) - The space required to store the binary strings is constant, as it does not depend on the size of the input number.

**Key Insight**
The key insight is that the smallest number with all set bits greater than or equal to the input number can be achieved by simply repeating the character '1' the same number of times as the length of the input number's binary representation. This is because the binary representation of the smallest number with all set bits will have the same number of bits as the input number, and will consist entirely of '1's.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-10-29 |
| 💻 Language | Python |