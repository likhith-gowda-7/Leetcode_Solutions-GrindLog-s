# 3753. Total Waviness of Numbers in Range II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/)


## 📝 Problem Description

You are given two integers `num1` and `num2` representing an **inclusive** range `[num1, num2]`.

The **waviness** of a number is defined as the total count of its **peaks** and **valleys**:

	- A digit is a **peak** if it is **strictly greater** than both of its immediate neighbors.

	- A digit is a **valley** if it is **strictly less** than both of its immediate neighbors.

	- The first and last digits of a number **cannot** be peaks or valleys.

	- Any number with fewer than 3 digits has a waviness of 0.

Return the total sum of waviness for all numbers in the range `[num1, num2]`.
 

Example 1:**

**Input:** num1 = 120, num2 = 130

**Output:** 3

**Explanation:**

In the range `[120, 130]`:

	- `120`: middle digit 2 is a peak, waviness = 1.

	- `121`: middle digit 2 is a peak, waviness = 1.

	- `130`: middle digit 3 is a peak, waviness = 1.

	- All other numbers in the range have a waviness of 0.

Thus, total waviness is `1 + 1 + 1 = 3`.

Example 2:**

**Input:** num1 = 198, num2 = 202

**Output:** 3

**Explanation:**

In the range `[198, 202]`:

	- `198`: middle digit 9 is a peak, waviness = 1.

	- `201`: middle digit 0 is a valley, waviness = 1.

	- `202`: middle digit 0 is a valley, waviness = 1.

	- All other numbers in the range have a waviness of 0.

Thus, total waviness is `1 + 1 + 1 = 3`.

Example 3:**

**Input:** num1 = 4848, num2 = 4848

**Output:** 2

**Explanation:**

Number `4848`: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

 

**Constraints:**

	- `1 <= num1 <= num2 <= 10^15`​​​​​​​

## 🧠 Solution Explanation

**Intuition**
The solution uses a dynamic programming approach to calculate the total waviness of numbers in a given range. It first precomputes a list of numbers with a single peak or valley, then uses this list to count the number of ways to form each number in the range.

**Approach**
1. Precompute a list of numbers with a single peak or valley by iterating over all possible 3-digit numbers and checking if the middle digit is a peak or valley.
2. Define a function `totalWaviness` to calculate the total waviness of numbers in the range `[A, B]` by subtracting the waviness of numbers less than `A` from the waviness of numbers less than or equal to `B`.
3. Define a function `waveCount` to calculate the waviness of numbers less than or equal to a given number by summing the number of ways to form each number using the precomputed list of numbers with a single peak or valley.
4. Define a function `countWays` to calculate the number of ways to form a given number using the precomputed list of numbers with a single peak or valley.

**Time Complexity**
O(n * m * k), where n is the number of numbers in the range, m is the number of possible 3-digit numbers, and k is the number of possible single-digit peaks or valleys.

**Space Complexity**
O(m), where m is the number of possible 3-digit numbers.

**Key Insight**
The key insight is to precompute a list of numbers with a single peak or valley, which allows us to efficiently count the number of ways to form each number in the range. This approach avoids the need to iterate over all possible numbers in the range, resulting in a significant reduction in time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 862 ms (Beats 28.57%) |
| 💾 Memory | 19.4 MB (Beats 93.57%) |
| 📅 Solved | 2026-06-05 |
| 💻 Language | Python |