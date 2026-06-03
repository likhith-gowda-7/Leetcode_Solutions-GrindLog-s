# 3130. Find All Possible Stable Binary Arrays II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/)


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

The two possible stable binary arrays are `[1,0]` and `[0,1]`.

Example 2:**

**Input:** zero = 1, one = 2, limit = 1

**Output:** 1

**Explanation:**

The only possible stable binary array is `[1,0,1]`.

Example 3:**

**Input:** zero = 3, one = 3, limit = 2

**Output:** 14

**Explanation:**

All the possible stable binary arrays are `[0,0,1,0,1,1]`, `[0,0,1,1,0,1]`, `[0,1,0,0,1,1]`, `[0,1,0,1,0,1]`, `[0,1,0,1,1,0]`, `[0,1,1,0,0,1]`, `[0,1,1,0,1,0]`, `[1,0,0,1,0,1]`, `[1,0,0,1,1,0]`, `[1,0,1,0,0,1]`, `[1,0,1,0,1,0]`, `[1,0,1,1,0,0]`, `[1,1,0,0,1,0]`, and `[1,1,0,1,0,0]`.

 

**Constraints:**

	- `1 <= zero, one, limit <= 1000`

## 🧠 Solution Explanation

**Intuition**
This solution uses dynamic programming and combinatorics to count the number of stable binary arrays. The key insight is to break down the problem into smaller subproblems and use the concept of combinations to calculate the number of stable arrays for each subproblem.

**Approach**

1.  Calculate the factorial and modular inverse of the factorial up to the maximum possible number of elements in the binary array.
2.  Define a function `C(n, k)` to calculate the number of combinations of `n` items taken `k` at a time, using the precomputed factorial and modular inverse.
3.  Define a function `F(N, K, L)` to calculate the number of stable arrays of length `N` with `K` zeros and `L` as the limit for each subarray.
4.  Initialize an array `fOne` to store the number of stable arrays for each possible number of ones from 1 to `maxK`.
5.  Iterate over each possible number of ones `k` from 1 to `maxK`, and calculate the number of stable arrays for each `k` using the `F` function.
6.  For each `k`, calculate the number of stable arrays with `k` ones and the corresponding number of zeros, and add it to the total count.

**Time Complexity**
The time complexity of this solution is O(maxN^2), where maxN is the maximum possible number of elements in the binary array. This is because we need to iterate over each possible number of ones and zeros, and for each pair, we need to calculate the number of stable arrays using the `F` function.

**Space Complexity**
The space complexity of this solution is O(maxN), which is the space required to store the precomputed factorial and modular inverse, as well as the `fOne` array.

**Key Insight**
The key insight in this solution is to use the concept of combinations to calculate the number of stable arrays for each subproblem. By breaking down the problem into smaller subproblems and using the precomputed factorial and modular inverse, we can efficiently calculate the number of stable arrays for each subproblem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 754 ms (Beats 91.93%) |
| 💾 Memory | 19.4 MB (Beats 98.21%) |
| 📅 Solved | 2026-03-10 |
| 💻 Language | Python |