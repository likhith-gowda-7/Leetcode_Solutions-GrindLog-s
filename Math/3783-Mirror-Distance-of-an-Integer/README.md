# 3783. Mirror Distance of an Integer


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/mirror-distance-of-an-integer/)


## 📝 Problem Description

You are given an integer `n`.

Define its **mirror distance** as: `abs(n - reverse(n))`​​​​​​​ where `reverse(n)` is the integer formed by reversing the digits of `n`.

Return an integer denoting the mirror distance of `n`​​​​​​​.

`abs(x)` denotes the absolute value of `x`.

 

Example 1:**

**Input:** n = 25

**Output:** 27

**Explanation:**

	- `reverse(25) = 52`.

	- Thus, the answer is `abs(25 - 52) = 27`.

Example 2:**

**Input:** n = 10

**Output:** 9

**Explanation:**

	- `reverse(10) = 01` which is 1.

	- Thus, the answer is `abs(10 - 1) = 9`.

Example 3:**

**Input:** n = 7

**Output:** 0

**Explanation:**

	- `reverse(7) = 7`.

	- Thus, the answer is `abs(7 - 7) = 0`.

 

**Constraints:**

	- `1 <= n <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The mirror distance of an integer `n` is calculated by taking the absolute difference between `n` and its reverse. This can be achieved by first reversing the digits of `n` and then subtracting the reversed number from `n`.

**Approach**
1. Convert the integer `n` to a string to easily reverse its digits.
2. Use slicing (`[::-1]`) to reverse the string representation of `n`.
3. Remove leading zeros from the reversed string using `lstrip('0')`.
4. Convert the reversed string back to an integer.
5. Calculate the absolute difference between `n` and the reversed integer.

**Time Complexity**
O(log(n)) - The time complexity is logarithmic because we are converting the integer `n` to a string and back to an integer, which takes O(log(n)) time. The slicing and lstrip operations also take O(log(n)) time.

**Space Complexity**
O(log(n)) - The space complexity is logarithmic because we are converting the integer `n` to a string, which takes O(log(n)) space.

**Key Insight**
The key insight here is that we can easily reverse the digits of an integer by converting it to a string, reversing the string, and then converting it back to an integer. This approach allows us to calculate the mirror distance of an integer in a simple and efficient manner.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 47.8%) |
| 📅 Solved | 2026-04-18 |
| 💻 Language | Python |