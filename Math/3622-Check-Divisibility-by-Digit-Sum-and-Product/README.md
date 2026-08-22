# 3622. Check Divisibility by Digit Sum and Product


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/)


## 📝 Problem Description

You are given a positive integer `n`. Determine whether `n` is divisible by the **sum **of the following two values:

	- 
	The **digit sum** of `n` (the sum of its digits).

	

	- 
	The **digit** **product** of `n` (the product of its digits).

	

Return `true` if `n` is divisible by this sum; otherwise, return `false`.

 

Example 1:**

**Input:** n = 99

**Output:** true

**Explanation:**

Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

Example 2:**

**Input:** n = 23

**Output:** false

**Explanation:**

Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.

 

**Constraints:**

	- `1 <= n <= 10^6`

## 🧠 Solution Explanation

**Intuition**  
The only thing that matters is the digits of `n`.  
If we can compute the sum of the digits and the product of the digits, their total is a single number; checking whether `n` is divisible by that total is a direct modulus test.

**Approach**  
1. Initialize `total = 0` (digit sum) and `prod = 1` (digit product).  
2. While `n` has digits:  
   - `last = n % 10` (extract the right‑most digit).  
   - Add `last` to `total`.  
   - Multiply `prod` by `last`.  
   - Remove the last digit: `n //= 10`.  
3. After the loop, `total + prod` is the value to test.  
4. Return `True` if `original_n % (total + prod) == 0`, otherwise `False`.

**Time Complexity**  
`O(d)` where `d` is the number of digits in `n` (≤ 7 for `n ≤ 10^6`).  
Each digit is processed once.

**Space Complexity**  
`O(1)` – only a few integer variables are used regardless of input size.

**Key Insight**  
The problem reduces to a single modulus operation once the digit sum and product are known; no extra data structures or iterations are needed.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 58.35%) |
| 📅 Solved | 2026-08-22 |
| 💻 Language | Python |