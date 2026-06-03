# 326. Power of Three


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/power-of-three/)


## 📝 Problem Description

Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3^x`.

 

Example 1:**

```

**Input:** n = 27
**Output:** true
**Explanation:** 27 = 3^3

```

Example 2:**

```

**Input:** n = 0
**Output:** false
**Explanation:** There is no x where 3^x = 0.

```

Example 3:**

```

**Input:** n = -1
**Output:** false
**Explanation:** There is no x where 3^x = (-1).

```

 

**Constraints:**

	- `-2^31 <= n <= 2^31 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## 🧠 Solution Explanation

**Intuition**
This solution works by continuously dividing the input number `n` by 3 until it reaches 1. If `n` is a power of three, it will eventually reach 1. If `n` is not a power of three, it will reach a number that is not divisible by 3, at which point the function returns `False`.

**Approach**
1. Check if `n` is less than or equal to 0. If so, return `False` because negative numbers and 0 are not powers of three.
2. While `n` is greater than 1, check if `n` is divisible by 3.
   - If `n` is divisible by 3, divide `n` by 3.
   - If `n` is not divisible by 3, return `False` because `n` is not a power of three.
3. If `n` is 1, return `True` because `n` is a power of three (specifically, 3^0).

**Time Complexity**
O(log n) because in the worst case, we divide `n` by 3 until it reaches 1. The number of divisions required is proportional to the logarithm of `n` to the base 3.

**Space Complexity**
O(1) because we only use a constant amount of space to store the input `n` and the temporary result of the division.

**Key Insight**
The key insight here is that if `n` is a power of three, it can be written as 3^x for some integer x. This means that `n` can be divided by 3 repeatedly until it reaches 1, and this process will terminate if and only if `n` is a power of three.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 5 ms (Beats 76.59%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-08-13 |
| 💻 Language | Python |