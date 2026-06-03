# 1780. Check if Number is a Sum of Powers of Three


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/)


## 📝 Problem Description

Given an integer `n`, return `true` *if it is possible to represent *`n`* as the sum of distinct powers of three.* Otherwise, return `false`.

An integer `y` is a power of three if there exists an integer `x` such that `y == 3^x`.

 

Example 1:**

```

**Input:** n = 12
**Output:** true
**Explanation:** 12 = 3^1 + 3^2

```

Example 2:**

```

**Input:** n = 91
**Output:** true
**Explanation:** 91 = 3^0 + 3^2 + 3^4

```

Example 3:**

```

**Input:** n = 21
**Output:** false

```

 

**Constraints:**

	- `1 <= n <= 10^7`

## 🧠 Solution Explanation

**Intuition**
The approach is based on the fact that any number can be represented as a sum of distinct powers of three if and only if the binary representation of the number contains only 1s and 0s. This is because each power of three can be represented as a binary digit (0 or 1), and the sum of these digits will give us the binary representation of the number.

**Approach**
1. First, we find the maximum power of three that is less than or equal to the given number `n`. This is done by taking the logarithm base 3 of `n` and rounding down to the nearest integer.
2. Then, we start from the maximum power of three and subtract it from `n` as many times as possible. This is done by repeatedly subtracting the current power of three from `n` until `n` becomes 0.
3. If `n` becomes 0, it means we have successfully represented it as a sum of distinct powers of three, so we return `True`.
4. If we have subtracted all powers of three from `n` and it still doesn't become 0, it means `n` cannot be represented as a sum of distinct powers of three, so we return `False`.

**Time Complexity**
O(log(n)) because we are repeatedly dividing `n` by 3 in the first while loop, which takes log(n) time.

**Space Complexity**
O(1) because we are only using a constant amount of space to store the variables `i` and `power`.

**Key Insight**
The key insight is that any number can be represented as a sum of distinct powers of three if and only if the binary representation of the number contains only 1s and 0s. This is because each power of three can be represented as a binary digit (0 or 1), and the sum of these digits will give us the binary representation of the number.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-03-04 |
| 💻 Language | Python |