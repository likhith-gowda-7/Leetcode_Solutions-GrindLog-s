# 166. Fraction to Recurring Decimal


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/fraction-to-recurring-decimal/)


## 📝 Problem Description

Given two integers representing the `numerator` and `denominator` of a fraction, return *the fraction in string format*.

If the fractional part is repeating, enclose the repeating part in parentheses

If multiple answers are possible, return **any of them**.

It is **guaranteed** that the length of the answer string is less than `10^4` for all the given inputs.

**Note** that if the fraction can be represented as a *finite length string*, you **must** return it.

 

Example 1:**

```

**Input:** numerator = 1, denominator = 2
**Output:** "0.5"

```

Example 2:**

```

**Input:** numerator = 2, denominator = 1
**Output:** "2"

```

Example 3:**

```

**Input:** numerator = 4, denominator = 333
**Output:** "0.(012)"

```

 

**Constraints:**

	- `-2^31 <= numerator, denominator <= 2^31 - 1`

	- `denominator != 0`

## 🧠 Solution Explanation

**Intuition**
This solution works by first handling the sign of the fraction and then performing long division to obtain the integer part of the result. To handle the decimal part, it uses a hash table to keep track of the remainders encountered during the division process. This allows it to identify when a repeating pattern is encountered and to format the result accordingly.

**Approach**
1. Check if either the numerator or denominator is zero, in which case the result is simply "0".
2. Determine the sign of the fraction and store it in the `minus` variable.
3. If the sign is negative, convert both the numerator and denominator to positive.
4. Initialize an empty result string `res` and a hash table `remainder_map` to store the remainders encountered during division.
5. Perform long division to obtain the integer part of the result and append it to `res`.
6. If the remainder is zero, break out of the loop.
7. If the remainder is already in `remainder_map`, it means a repeating pattern has been encountered, so break out of the loop.
8. Otherwise, append the remainder to `remainder_map` with its corresponding index in `res` and continue the loop.
9. If a repeating pattern is encountered, format the result by inserting parentheses around the repeating part.

**Time Complexity**
O(n), where n is the number of digits in the numerator or denominator. This is because each digit in the numerator or denominator is processed at most once during the division process.

**Space Complexity**
O(n), where n is the number of digits in the numerator or denominator. This is because in the worst case, the hash table `remainder_map` may store all the remainders encountered during the division process.

**Key Insight**
The key insight behind this solution is the use of a hash table to keep track of the remainders encountered during the division process. This allows it to identify when a repeating pattern is encountered and to format the result accordingly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-09-25 |
| 💻 Language | Python |