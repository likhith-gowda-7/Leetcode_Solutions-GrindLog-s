> 📌 **Cross-listed:** Primary location is [Math/0231-Power-of-Two](../../Math/0231-Power-of-Two). This problem also appears under: **Math**, **Bit Manipulation**, **Recursion**

# 231. Power of Two


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/power-of-two/)


## 📝 Problem Description

Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2^x`.

 

Example 1:**

```

**Input:** n = 1
**Output:** true
**Explanation: **2^0 = 1

```

Example 2:**

```

**Input:** n = 16
**Output:** true
**Explanation: **2^4 = 16

```

Example 3:**

```

**Input:** n = 3
**Output:** false

```

 

**Constraints:**

	- `-2^31 <= n <= 2^31 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## 🧠 Solution Explanation

**Intuition**
This solution works by utilizing the binary representation of the input number `n`. Since a power of two in binary has exactly one `1` bit and all other bits are `0`, we can check if `n` is a power of two by counting the number of `1` bits in its binary representation.

**Approach**
1. Convert the input number `n` to its binary representation using the built-in `bin()` function.
2. Count the number of `1` bits in the binary representation using the `count()` method.
3. Return `True` if `n` is greater than 0 and there is exactly one `1` bit in the binary representation; otherwise, return `False`.

**Time Complexity**
O(log n), where n is the input number. This is because the binary representation of a number has a logarithmic number of bits (specifically, log2(n) bits). The `bin()` function and `count()` method both operate on the binary representation, which has a length proportional to log n.

**Space Complexity**
O(log n), where n is the input number. This is because the binary representation of a number has a logarithmic number of bits, and we need to store this binary representation in memory.

**Key Insight**
The key insight here is that a power of two in binary has exactly one `1` bit, which makes it easy to check if a number is a power of two by counting the number of `1` bits in its binary representation. This approach is efficient and elegant, and it avoids the need for loops or recursion.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-08-09 |
| 💻 Language | Python |