> 📌 **Cross-listed:** Primary location is [Dynamic Programming/3699-Number-of-ZigZag-Arrays-I](../../Dynamic-Programming/3699-Number-of-ZigZag-Arrays-I). This problem also appears under: **Dynamic Programming**, **Prefix Sum**

# 3699. Number of ZigZag Arrays I


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-i/)


## 📝 Problem Description

You are given three integers `n`, `l`, and `r`.

A **ZigZag** array of length `n` is defined as follows:

	- Each element lies in the range `[l, r]`.

	- No **two** adjacent elements are equal.

	- No **three** consecutive elements form a **strictly increasing** or **strictly decreasing** sequence.

Return the total number of valid **ZigZag** arrays.

Since the answer may be large, return it **modulo** `10^9 + 7`.

A **sequence** is said to be **strictly increasing** if each element is strictly greater than its previous one (if exists).

A **sequence** is said to be **strictly decreasing** if each element is strictly smaller than its previous one (if exists).

 

Example 1:**

**Input:** n = 3, l = 4, r = 5

**Output:** 2

**Explanation:**

There are only 2 valid ZigZag arrays of length `n = 3` using values in the range `[4, 5]`:

	- `[4, 5, 4]`

	- `[5, 4, 5]`​​​​​​​

Example 2:**

**Input:** n = 3, l = 1, r = 3

**Output:** 10

**Explanation:**

There are 10 valid ZigZag arrays of length `n = 3` using values in the range `[1, 3]`:

	- `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]`

	- `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]`

	- `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]`

All arrays meet the ZigZag conditions.

 

**Constraints:**

	- `3 <= n <= 2000`

	- `1 <= l < r <= 2000`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to count the number of valid ZigZag arrays of length `n`, where each element lies in the range `[l, r]`, no two adjacent elements are equal, and no three consecutive elements form a strictly increasing or strictly decreasing sequence. The key insight is to use dynamic programming to build up the number of valid arrays of length `n` from the number of valid arrays of length `n-1`, `n-2`, and `n-3`.

**Approach**
1. Initialize two arrays `up` and `down` of size `m+1`, where `m = r - l + 1`, to store the number of valid arrays of length `n-1` ending with an increasing and decreasing sequence, respectively.
2. For `n-3` to `n`, update the `up` and `down` arrays by computing the prefix and suffix sums of the previous arrays.
3. For each `x` from `1` to `m`, update the `new_up` and `new_down` arrays by taking the prefix sum of `up` and suffix sum of `down` at position `x`, respectively.
4. Swap the `up` and `new_up` arrays, and the `down` and `new_down` arrays.
5. Repeat steps 3-4 until we reach `n`.
6. Return the sum of the `up` and `down` arrays modulo `10^9 + 7`.

**Time Complexity**
O(n*m), where `n` is the length of the array and `m` is the range of values. We iterate over the range `n-3` to `n` and for each iteration, we iterate over the range `1` to `m`.

**Space Complexity**
O(m), where `m` is the range of values. We use two arrays `up` and `down` of size `m+1` to store the number of valid arrays of length `n-1` ending with an increasing and decreasing sequence, respectively.

**Key Insight**
The key insight is to use dynamic programming to build up the number of valid arrays of length `n` from the number of valid arrays of length `n-1`, `n-2`, and `n-3`. By computing the prefix and suffix sums of the previous arrays, we can efficiently update the number of valid arrays of length `n`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11504 ms (Beats 20.91%) |
| 💾 Memory | 19.5 MB (Beats 70.75%) |
| 📅 Solved | 2026-06-23 |
| 💻 Language | Python |