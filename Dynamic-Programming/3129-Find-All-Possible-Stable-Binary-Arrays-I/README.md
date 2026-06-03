# 3129. Find All Possible Stable Binary Arrays I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/)


## 📝 Problem Description

You are given 3 positive integers `zero`, `one`, and `limit`.

A binary array `arr` is called **stable** if:

	- The number of occurrences of 0 in `arr` is **exactly **`zero`.

	- The number of occurrences of 1 in `arr` is **exactly** `one`.

	- Each subarray of `arr` with a size greater than `limit` must contain **both **0 and 1.

Return the *total* number of **stable** binary arrays.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

 

Example 1:**

**Input:** zero = 1, one = 1, limit = 2

**Output:** 2

**Explanation:**

The two possible stable binary arrays are `[1,0]` and `[0,1]`, as both arrays have a single 0 and a single 1, and no subarray has a length greater than 2.

Example 2:**

**Input:** zero = 1, one = 2, limit = 1

**Output:** 1

**Explanation:**

The only possible stable binary array is `[1,0,1]`.

Note that the binary arrays `[1,1,0]` and `[0,1,1]` have subarrays of length 2 with identical elements, hence, they are not stable.

Example 3:**

**Input:** zero = 3, one = 3, limit = 2

**Output:** 14

**Explanation:**

All the possible stable binary arrays are `[0,0,1,0,1,1]`, `[0,0,1,1,0,1]`, `[0,1,0,0,1,1]`, `[0,1,0,1,0,1]`, `[0,1,0,1,1,0]`, `[0,1,1,0,0,1]`, `[0,1,1,0,1,0]`, `[1,0,0,1,0,1]`, `[1,0,0,1,1,0]`, `[1,0,1,0,0,1]`, `[1,0,1,0,1,0]`, `[1,0,1,1,0,0]`, `[1,1,0,0,1,0]`, and `[1,1,0,1,0,0]`.

 

**Constraints:**

	- `1 <= zero, one, limit <= 200`

## 🧠 Solution Explanation

**Intuition**
The problem requires finding the total number of stable binary arrays given certain constraints. The key insight is to use dynamic programming and combinatorics to break down the problem into smaller sub-problems. We can use the concept of combinations to calculate the number of stable arrays for each sub-problem.

**Approach**
1. Calculate the factorial and inverse factorial of numbers up to `maxN` (the sum of `zero` and `one`) modulo `10^9 + 7` to use in combination calculations.
2. Define a function `C(n, k)` to calculate the number of combinations of `n` items taken `k` at a time modulo `10^9 + 7`.
3. Define a function `F(N, K, L)` to calculate the number of stable arrays with `N` elements, `K` zeros, and a limit `L` on the subarray size. This function uses the combination function to calculate the number of ways to choose the positions of zeros and ones.
4. Initialize an array `fOne` to store the number of stable arrays with `one` ones and varying numbers of zeros.
5. Iterate over the possible numbers of zeros `k` from 1 to `maxK` (the minimum of `zero` and `one + 1`), and for each `k`, calculate the number of stable arrays with `k` zeros using the function `F`.
6. Iterate over the possible numbers of zeros `k` from 1 to `maxK`, and for each `k`, calculate the number of stable arrays with `k` zeros by multiplying the number of ways to choose the positions of zeros and ones.

**Time Complexity**
The time complexity is O(maxN^2) due to the two nested loops in the `F` function, where `maxN` is the sum of `zero` and `one`. The combination calculations also take O(maxN) time.

**Space Complexity**
The space complexity is O(maxN) due to the arrays `fact`, `invFact`, and `fOne`.

**Key Insight**
The key insight is to use dynamic programming and combinatorics to break down the problem into smaller sub-problems. By using the concept of combinations, we can calculate the number of stable arrays for each sub-problem efficiently. The use of modular arithmetic also helps to prevent overflow and improve the performance of the algorithm.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 21 ms (Beats 95.77%) |
| 💾 Memory | 19.5 MB (Beats 95.77%) |
| 📅 Solved | 2026-03-09 |
| 💻 Language | Python |