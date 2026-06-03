# 2787. Ways to Express an Integer as Sum of Powers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/)


## 📝 Problem Description

Given two **positive** integers `n` and `x`.

Return *the number of ways *`n`* can be expressed as the sum of the *`x^th`* power of **unique** positive integers, in other words, the number of sets of unique integers *`[n_1, n_2, ..., n_k]`* where *`n = n_1^x + n_2^x + ... + n_k^x`*.*

Since the result can be very large, return it modulo `10^9 + 7`.

For example, if `n = 160` and `x = 3`, one way to express `n` is `n = 2^3 + 3^3 + 5^3`.

 

Example 1:**

```

**Input:** n = 10, x = 2
**Output:** 1
**Explanation:** We can express n as the following: n = 3^2 + 1^2 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2^nd power of unique integers.

```

Example 2:**

```

**Input:** n = 4, x = 1
**Output:** 2
**Explanation:** We can express n in the following ways:
- n = 4^1 = 4.
- n = 3^1 + 1^1 = 4.

```

 

**Constraints:**

	- `1 <= n <= 300`

	- `1 <= x <= 5`

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using dynamic programming by breaking down the problem into smaller sub-problems. The key insight is to realize that we can either take the current power of `x` or skip it, and the number of ways to express `n` as the sum of powers of unique integers is the sum of these two possibilities.

**Approach**
1. Initialize a memoization dictionary `memo` to store the results of sub-problems.
2. Define a recursive function `dp` that takes two parameters: `remaining` (the remaining value to be expressed as a sum of powers) and `curr` (the current power of `x`).
3. If the sub-problem has already been solved (i.e., `(remaining, curr)` is in `memo`), return the stored result.
4. If `remaining` is 0, return 1 (since we have expressed `n` as the sum of powers of unique integers).
5. If `power` (the current power of `x`) is greater than `remaining`, return 0 (since we cannot take the current power).
6. Recursively call `dp` with two possibilities: `take` (take the current power of `x` and subtract it from `remaining`) and `skip` (skip the current power of `x` and keep `remaining` the same).
7. Store the result of the current sub-problem in `memo` and return it.

**Time Complexity**
The time complexity of this solution is O(n^(1/x) * x), where n is the input number and x is the power. This is because in the worst case, we need to recursively call `dp` for each possible value of `curr` from 1 to n^(1/x).

**Space Complexity**
The space complexity of this solution is O(n^(1/x) * x), which is the maximum size of the memoization dictionary. This is because we need to store the results of all sub-problems in the memoization dictionary.

**Key Insight**
The key insight is to realize that we can either take the current power of `x` or skip it, and the number of ways to express `n` as the sum of powers of unique integers is the sum of these two possibilities. This allows us to break down the problem into smaller sub-problems and solve them recursively using memoization.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1898 ms (Beats 27.88%) |
| 💾 Memory | 427.3 MB (Beats 12.12%) |
| 📅 Solved | 2025-08-12 |
| 💻 Language | Python |