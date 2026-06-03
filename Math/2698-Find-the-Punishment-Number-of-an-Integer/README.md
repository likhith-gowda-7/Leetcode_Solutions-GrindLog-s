# 2698. Find the Punishment Number of an Integer


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-punishment-number-of-an-integer/)


## 📝 Problem Description

Given a positive integer `n`, return *the **punishment number*** of `n`.

The **punishment number** of `n` is defined as the sum of the squares of all integers `i` such that:

	- `1 <= i <= n`

	- The decimal representation of `i * i` can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals `i`.

 

Example 1:**

```

**Input:** n = 10
**Output:** 182
**Explanation:** There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182

```

Example 2:**

```

**Input:** n = 37
**Output:** 1478
**Explanation:** There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478

```

 

**Constraints:**

	- `1 <= n <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution works by precomputing a set of perfect squares that can be formed by summing contiguous substrings of their decimal representation. This set is used to efficiently check if a given square can be formed in this way, allowing for a straightforward calculation of the punishment number.

**Approach**
1. Precompute a set of perfect squares that can be formed by summing contiguous substrings of their decimal representation.
2. Initialize a variable `res` to store the punishment number.
3. Iterate over the range from 1 to `n` (inclusive).
4. For each `i` in the range, check if `i` is in the precomputed set of perfect squares.
5. If `i` is in the set, add `i * i` to the punishment number `res`.
6. Return the calculated punishment number `res`.

**Time Complexity**
O(n) - The precomputation step has a fixed time complexity, and the iteration over the range from 1 to `n` dominates the overall time complexity.

**Space Complexity**
O(k) - where k is the number of precomputed perfect squares, which is a small constant in this case.

**Key Insight**
The key insight is that the punishment number can be efficiently calculated by precomputing a set of perfect squares that can be formed by summing contiguous substrings of their decimal representation. This allows for a straightforward iteration over the range from 1 to `n` to calculate the punishment number.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 82.33%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-15 |
| 💻 Language | Python |