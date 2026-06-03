# 2894. Divisible and Non-divisible Sums Difference


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/)


## 📝 Problem Description

You are given positive integers `n` and `m`.

Define two integers as follows:

	- `num1`: The sum of all integers in the range `[1, n]` (both **inclusive**) that are **not divisible** by `m`.

	- `num2`: The sum of all integers in the range `[1, n]` (both **inclusive**) that are **divisible** by `m`.

Return *the integer* `num1 - num2`.

 

Example 1:**

```

**Input:** n = 10, m = 3
**Output:** 19
**Explanation:** In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.

```

Example 2:**

```

**Input:** n = 5, m = 6
**Output:** 15
**Explanation:** In the given example:
- Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], num1 is the sum of those integers = 15.
- Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.
We return 15 - 0 = 15 as the answer.

```

Example 3:**

```

**Input:** n = 5, m = 1
**Output:** -15
**Explanation:** In the given example:
- Integers in the range [1, 5] that are not divisible by 1 are [], num1 is the sum of those integers = 0.
- Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], num2 is the sum of those integers = 15.
We return 0 - 15 = -15 as the answer.

```

 

**Constraints:**

	- `1 <= n, m <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over the range `[1, n]` and calculating the sum of numbers that are not divisible by `m` (`num1_sum`) and the sum of numbers that are divisible by `m` (`num2_sum`). The difference between these two sums is then returned.

**Approach**
1. Initialize two variables `num1_sum` and `num2_sum` to store the sum of numbers not divisible by `m` and the sum of numbers divisible by `m`, respectively.
2. Iterate over the range `[1, n]` using a for loop.
3. For each number `i` in the range, check if it is not divisible by `m` by using the modulo operator (`i % m != 0`).
4. If `i` is not divisible by `m`, add it to `num1_sum`.
5. If `i` is divisible by `m`, add it to `num2_sum`.
6. After iterating over the entire range, return the difference between `num1_sum` and `num2_sum`.

**Time Complexity**
O(n)
The time complexity is linear because we are iterating over the range `[1, n]` once.

**Space Complexity**
O(1)
The space complexity is constant because we are only using a fixed amount of space to store the two sums, regardless of the input size.

**Key Insight**
The key insight is that we can calculate the sum of numbers not divisible by `m` and the sum of numbers divisible by `m` separately, and then return their difference. This approach avoids the need to calculate the sum of all numbers in the range and then subtract the sum of numbers divisible by `m`, which would be more complex and less efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-05-27 |
| 💻 Language | Python |