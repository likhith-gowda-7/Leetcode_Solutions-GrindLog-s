# 1009. Complement of Base 10 Integer


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/complement-of-base-10-integer/)


## 📝 Problem Description

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

	- For example, The integer `5` is `"101"` in binary and its **complement** is `"010"` which is the integer `2`.

Given an integer `n`, return *its complement*.

 

Example 1:**

```

**Input:** n = 5
**Output:** 2
**Explanation:** 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

```

Example 2:**

```

**Input:** n = 7
**Output:** 0
**Explanation:** 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

```

Example 3:**

```

**Input:** n = 10
**Output:** 5
**Explanation:** 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

```

 

**Constraints:**

	- `0 <= n < 10^9`

 

**Note:** This question is the same as 476: [https://leetcode.com/problems/number-complement/](https://leetcode.com/problems/number-complement/)

## 🧠 Solution Explanation

**Intuition**
The solution works by first converting the input integer `n` to its binary representation. Then, it simply flips all the bits (0s to 1s and 1s to 0s) in the binary representation to get the complement.

**Approach**
1. Convert the input integer `n` to its binary representation using the `bin()` function.
2. Remove the '0b' prefix from the binary string using indexing `[2:]`.
3. Initialize an empty string `curr` to store the complement.
4. Iterate through each character `b` in the binary string.
5. If `b` is '1', append '0' to `curr`.
6. If `b` is '0', append '1' to `curr`.
7. Convert the `curr` string back to an integer using `int()` with base 2.

**Time Complexity**
O(log n) - The time complexity is logarithmic because we are iterating through the binary representation of `n`, which has a length of log n.

**Space Complexity**
O(log n) - The space complexity is also logarithmic because we are storing the binary representation and the complement in strings, which have a length of log n.

**Key Insight**
The key insight is that we can get the complement of a binary number by simply flipping all its bits. This is because the binary representation of a number is essentially a sequence of bits (0s and 1s), and flipping these bits is equivalent to changing the number's value.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 26.33%) |
| 📅 Solved | 2026-03-12 |
| 💻 Language | Python |