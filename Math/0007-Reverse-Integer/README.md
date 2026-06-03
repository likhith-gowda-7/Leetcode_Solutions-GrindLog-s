# 7. Reverse Integer


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-integer/)


## 📝 Problem Description

Given a signed 32-bit integer `x`, return `x`* with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

 

Example 1:**

```

**Input:** x = 123
**Output:** 321

```

Example 2:**

```

**Input:** x = -123
**Output:** -321

```

Example 3:**

```

**Input:** x = 120
**Output:** 21

```

 

**Constraints:**

	- `-2^31 <= x <= 2^31 - 1`

## 🧠 Solution Explanation

**Intuition**
The solution works by first converting the integer to a string, reversing the string, and then converting it back to an integer. However, this approach can lead to overflow issues when dealing with large numbers. To mitigate this, we check if the reversed integer is within the 32-bit signed integer range before returning it.

**Approach**
1. Convert the input integer `x` to a string `s`.
2. If `x` is negative, remove the negative sign and reverse the string from index 1 to the end (`s[1:][::-1]`).
3. If `x` is non-negative, simply reverse the entire string (`s[::-1]`).
4. Convert the reversed string back to an integer `res`.
5. Check if `res` is within the 32-bit signed integer range. If not, return 0; otherwise, return `res`.

**Time Complexity**
O(n), where n is the number of digits in the input integer. This is because we're performing a string reversal operation, which has a linear time complexity.

**Space Complexity**
O(n), where n is the number of digits in the input integer. This is because we're converting the integer to a string, which requires additional space proportional to the number of digits.

**Key Insight**
The key insight here is to recognize that we can avoid overflow issues by checking the reversed integer against the 32-bit signed integer range before returning it. This allows us to safely reverse large integers without worrying about exceeding the maximum value that can be represented by a 32-bit signed integer.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 28 ms (Beats 99.82%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-05-07 |
| 💻 Language | Python |