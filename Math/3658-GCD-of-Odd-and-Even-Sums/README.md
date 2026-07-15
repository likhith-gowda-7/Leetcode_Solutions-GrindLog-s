# 3658. GCD of Odd and Even Sums


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Number Theory](https://img.shields.io/badge/Number%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/)


## 📝 Problem Description

You are given an integer `n`. Your task is to compute the **GCD** (greatest common divisor) of two values:

	- 
	`sumOdd`: the sum of the smallest `n` positive odd numbers.

	

	- 
	`sumEven`: the sum of the smallest `n` positive even numbers.

	

Return the GCD of `sumOdd` and `sumEven`.

 

Example 1:**

**Input:** n = 4

**Output:** 4

**Explanation:**

	- Sum of the first 4 odd numbers `sumOdd = 1 + 3 + 5 + 7 = 16`

	- Sum of the first 4 even numbers `sumEven = 2 + 4 + 6 + 8 = 20`

Hence, `GCD(sumOdd, sumEven) = GCD(16, 20) = 4`.

Example 2:**

**Input:** n = 5

**Output:** 5

**Explanation:**

	- Sum of the first 5 odd numbers `sumOdd = 1 + 3 + 5 + 7 + 9 = 25`

	- Sum of the first 5 even numbers `sumEven = 2 + 4 + 6 + 8 + 10 = 30`

Hence, `GCD(sumOdd, sumEven) = GCD(25, 30) = 5`.

 

**Constraints:**

	- `1 <= n <= 10​​​​​​​00`

## 🧠 Solution Explanation

**Intuition**
The key insight here is that the sum of the smallest `n` positive odd numbers is equal to `n^2`, and the sum of the smallest `n` positive even numbers is equal to `n*(n+1)`. This is because the sequence of odd numbers can be represented as `2k-1` and the sequence of even numbers can be represented as `2k`, where `k` ranges from `1` to `n`.

**Approach**
1. Recognize that the sum of the smallest `n` positive odd numbers is `n^2`.
2. Recognize that the sum of the smallest `n` positive even numbers is `n*(n+1)`.
3. Since the GCD of two numbers is the largest number that divides both of them without leaving a remainder, we can directly return `n` as the GCD of `n^2` and `n*(n+1)`.

**Time Complexity**
O(1) - This is a constant time complexity because we are directly returning `n` without performing any loops or recursive calls.

**Space Complexity**
O(1) - This is a constant space complexity because we are only using a constant amount of space to store the input `n` and the output `n`.

**Key Insight**
The key insight here is that the sum of the smallest `n` positive odd numbers and the sum of the smallest `n` positive even numbers can be expressed as simple formulas, which allows us to directly return `n` as the GCD. This is a clever observation that simplifies the problem and makes the solution efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.1 MB (Beats 85.77%) |
| 📅 Solved | 2026-07-15 |
| 💻 Language | Python |