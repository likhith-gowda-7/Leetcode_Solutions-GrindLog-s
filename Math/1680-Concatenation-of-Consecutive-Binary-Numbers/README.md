# 1680. Concatenation of Consecutive Binary Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/)


## 📝 Problem Description

Given an integer `n`, return *the **decimal value** of the binary string formed by concatenating the binary representations of *`1`* to *`n`* in order, **modulo ***`10^9 + 7`.

 

Example 1:**

```

**Input:** n = 1
**Output:** 1
**Explanation: **"1" in binary corresponds to the decimal value 1. 

```

Example 2:**

```

**Input:** n = 3
**Output:** 27
**Explanation: **In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

```

Example 3:**

```

**Input:** n = 12
**Output:** 505379714
**Explanation**: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 10^9 + 7, the result is 505379714.

```

 

**Constraints:**

	- `1 <= n <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The problem requires us to find the decimal value of the binary string formed by concatenating the binary representations of numbers from 1 to `n` in order, modulo `10^9 + 7`. The key insight is to recognize that the number of digits in the binary representation of a number is equal to the number of bits required to represent it, which is equivalent to the number of times the number can be divided by 2 before reaching 1.

**Approach**
1. Initialize the modulo value `mod` as `10^9 + 7` and the result `res` to 0.
2. Initialize the number of digits `digits` to 0.
3. Iterate over the numbers from 1 to `n` (inclusive).
4. For each number, check if it is a power of 2 by using the bitwise AND operator (`&`) with the number minus 1. If the result is 0, it means the number is a power of 2, and we increment the number of digits `digits` by 1.
5. Shift the result `res` to the left by `digits` bits using the left shift operator (`<<`), add the current number `num` to the result, and take the modulo `mod` to prevent overflow.
6. Return the final result `res`.

**Time Complexity**
O(n log n) - The time complexity is dominated by the loop that iterates over the numbers from 1 to `n`. In the worst case, the number of digits `digits` can grow up to log n, resulting in a time complexity of O(n log n).

**Space Complexity**
O(1) - The space complexity is constant, as we only use a few variables to store the result, modulo value, and number of digits.

**Key Insight**
The key insight is to recognize that the number of digits in the binary representation of a number is equal to the number of bits required to represent it, which is equivalent to the number of times the number can be divided by 2 before reaching 1. This allows us to efficiently calculate the number of digits for each number and update the result accordingly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 695 ms (Beats 71.89%) |
| 💾 Memory | 19.2 MB (Beats 44.24%) |
| 📅 Solved | 2026-02-28 |
| 💻 Language | Python |