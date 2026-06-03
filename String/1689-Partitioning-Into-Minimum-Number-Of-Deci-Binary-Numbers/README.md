# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/)


## 📝 Problem Description

A decimal number is called **deci-binary** if each of its digits is either `0` or `1` without any leading zeros. For example, `101` and `1100` are **deci-binary**, while `112` and `3001` are not.

Given a string `n` that represents a positive decimal integer, return *the **minimum** number of positive **deci-binary** numbers needed so that they sum up to *`n`*.*

 

Example 1:**

```

**Input:** n = "32"
**Output:** 3
**Explanation:** 10 + 11 + 11 = 32

```

Example 2:**

```

**Input:** n = "82734"
**Output:** 8

```

Example 3:**

```

**Input:** n = "27346209830709182346"
**Output:** 9

```

 

**Constraints:**

	- `1 <= n.length <= 10^5`

	- `n` consists of only digits.

	- `n` does not contain any leading zeros and represents a positive integer.

## 🧠 Solution Explanation

**Intuition**
The problem asks for the minimum number of deci-binary numbers needed to sum up to a given decimal number. The key insight is that a deci-binary number can be represented as a binary number (with digits 0 or 1) without any leading zeros. This means we can simply find the maximum digit in the given decimal number, which represents the maximum value of a deci-binary number needed.

**Approach**
1. The `max` function is used to find the maximum digit in the given string `s`.
2. The `int` function is used to convert the maximum digit to an integer, since `max` returns a string.
3. The result is returned as the minimum number of deci-binary numbers needed.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because the `max` function needs to iterate through all characters in the string to find the maximum digit.

**Space Complexity**
O(1), since only a constant amount of space is used to store the maximum digit and the result.

**Key Insight**
The key insight is that the maximum digit in the given decimal number represents the maximum value of a deci-binary number needed. This is because a deci-binary number can be represented as a binary number (with digits 0 or 1) without any leading zeros, and the maximum digit in the given decimal number is the maximum value that can be represented by a deci-binary number.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 19 ms (Beats 67.86%) |
| 💾 Memory | 19.9 MB (Beats 72.06%) |
| 📅 Solved | 2026-03-01 |
| 💻 Language | Python |