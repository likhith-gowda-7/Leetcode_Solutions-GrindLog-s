# 1925. Count Square Sum Triples


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-square-sum-triples/)


## 📝 Problem Description

A **square triple** `(a,b,c)` is a triple where `a`, `b`, and `c` are **integers** and `a^2 + b^2 = c^2`.

Given an integer `n`, return *the number of **square triples** such that *`1 <= a, b, c <= n`.

 

Example 1:**

```

**Input:** n = 5
**Output:** 2
**Explanation**: The square triples are (3,4,5) and (4,3,5).

```

Example 2:**

```

**Input:** n = 10
**Output:** 4
**Explanation**: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

```

 

**Constraints:**

	- `1 <= n <= 250`

## 🧠 Solution Explanation

**Intuition**
The solution uses a brute-force approach to find all possible square triples within the given range. It first generates a set of squares from 1 to n, then iterates over each pair of squares to check if their sum is also a square.

**Approach**
1. Create a set `squares` to store the squares of numbers from 1 to n.
2. Iterate over each pair of distinct squares `val1` and `val2` in `squares`.
3. Calculate the sum `s` of `val1` and `val2`.
4. Check if `s` is also a square in `squares`. If it is, increment the result counter `res`.
5. Return the total count of square triples.

**Time Complexity**
O(n^2 * sqrt(n)) - The outer loop iterates over n squares, and for each square, the inner loop also iterates over n squares. However, we only need to consider squares up to sqrt(n) because a larger square would have a corresponding smaller square that has already been counted.

**Space Complexity**
O(n) - We store all squares from 1 to n in a set, which requires O(n) space.

**Key Insight**
The key insight is that we only need to consider pairs of squares, and we can use a set to efficiently store and look up squares. This allows us to avoid redundant calculations and reduce the time complexity of the solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 81 ms (Beats 79.5%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-12-08 |
| 💻 Language | Python |