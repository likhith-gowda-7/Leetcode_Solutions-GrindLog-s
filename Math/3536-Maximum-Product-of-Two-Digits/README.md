# 3536. Maximum Product of Two Digits


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-product-of-two-digits/)


## 📝 Problem Description

You are given a positive integer `n`.

Return the **maximum** product of any two digits in `n`.

**Note:** You may use the **same** digit twice if it appears more than once in `n`.

 

Example 1:**

**Input:** n = 31

**Output:** 3

**Explanation:**

	- The digits of `n` are `[3, 1]`.

	- The possible products of any two digits are: `3 * 1 = 3`.

	- The maximum product is 3.

Example 2:**

**Input:** n = 22

**Output:** 4

**Explanation:**

	- The digits of `n` are `[2, 2]`.

	- The possible products of any two digits are: `2 * 2 = 4`.

	- The maximum product is 4.

Example 3:**

**Input:** n = 124

**Output:** 8

**Explanation:**

	- The digits of `n` are `[1, 2, 4]`.

	- The possible products of any two digits are: `1 * 2 = 2`, `1 * 4 = 4`, `2 * 4 = 8`.

	- The maximum product is 8.

 

**Constraints:**

	- `10 <= n <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by first converting the input integer into a list of its digits. It then iterates through the list to find the two largest digits, which are likely to produce the maximum product. This approach leverages the fact that the product of two numbers is maximized when the numbers are as large as possible.

**Approach**
1. Define a helper function `solve` that takes an integer `num` as input.
2. Initialize two variables `max1` and `max2` to store the two largest digits found so far.
3. While `num` is greater than 0, extract the last digit of `num` using the modulo operator (`num % 10`).
4. If the extracted digit is greater than `max1`, update `max2` to be the old value of `max1` and update `max1` to be the extracted digit.
5. If the extracted digit is greater than `max2` but not greater than `max1`, update `max2` to be the extracted digit.
6. Remove the last digit from `num` by performing integer division by 10 (`num //= 10`).
7. Return the product of `max1` and `max2`.
8. Call the `solve` function with the input integer `n` and return the result.

**Time Complexity**
O(log n), where n is the input integer. This is because the while loop runs until `num` is 0, and the number of digits in `num` is proportional to the logarithm of `num`.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the variables `max1`, `max2`, and `num`.

**Key Insight**
The key insight is that the product of two numbers is maximized when the numbers are as large as possible. By finding the two largest digits in the input integer, we can maximize the product of any two digits. This approach is efficient because it only requires a single pass through the digits of the input integer.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 88.69%) |
| 📅 Solved | 2026-07-25 |
| 💻 Language | Python |