> 📌 **Cross-listed:** Primary location is [String/3499-Maximize-Active-Section-with-Trade-I](../../String/3499-Maximize-Active-Section-with-Trade-I). This problem also appears under: **String**, **Enumeration**

# 3499. Maximize Active Section with Trade I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximize-active-section-with-trade-i/)


## 📝 Problem Description

You are given a binary string `s` of length `n`, where:

	- `'1'` represents an **active** section.

	- `'0'` represents an **inactive** section.

You can perform **at most one trade** to maximize the number of active sections in `s`. In a trade, you:

	- Convert a contiguous block of `'1'`s that is surrounded by `'0'`s to all `'0'`s.

	- Afterward, convert a contiguous block of `'0'`s that is surrounded by `'1'`s to all `'1'`s.

Return the **maximum** number of active sections in `s` after making the optimal trade.

**Note:** Treat `s` as if it is **augmented** with a `'1'` at both ends, forming `t = '1' + s + '1'`. The augmented `'1'`s **do not** contribute to the final count.

 

Example 1:**

**Input:** s = "01"

**Output:** 1

**Explanation:**

Because there is no block of `'1'`s surrounded by `'0'`s, no valid trade is possible. The maximum number of active sections is 1.

Example 2:**

**Input:** s = "0100"

**Output:** 4

**Explanation:**

	- String `"0100"` &rarr; Augmented to `"101001"`.

	- Choose `"0100"`, convert `"10**1**001"` &rarr; `"1**0000**1"` &rarr; `"1**1111**1"`.

	- The final string without augmentation is `"1111"`. The maximum number of active sections is 4.

Example 3:**

**Input:** s = "1000100"

**Output:** 7

**Explanation:**

	- String `"1000100"` &rarr; Augmented to `"110001001"`.

	- Choose `"000100"`, convert `"11000**1**001"` &rarr; `"11**000000**1"` &rarr; `"11**111111**1"`.

	- The final string without augmentation is `"1111111"`. The maximum number of active sections is 7.

Example 4:**

**Input:** s = "01010"

**Output:** 4

**Explanation:**

	- String `"01010"` &rarr; Augmented to `"1010101"`.

	- Choose `"010"`, convert `"10**1**0101"` &rarr; `"1**000**101"` &rarr; `"1**111**101"`.

	- The final string without augmentation is `"11110"`. The maximum number of active sections is 4.

 

**Constraints:**

	- `1 <= n == s.length <= 10^5`

	- `s[i]` is either `'0'` or `'1'`

## 🧠 Solution Explanation

**Intuition**
The solution works by first identifying all the contiguous blocks of zeros in the input string `s`. These blocks are then compared in pairs to find the maximum sum, which represents the maximum number of active sections that can be obtained by performing a trade. The remaining blocks of ones are also counted as they do not require a trade.

**Approach**
1. Initialize an empty list `seq` to store the lengths of contiguous blocks of zeros.
2. Initialize variables `zero_count` and `one_count` to keep track of the current block of zeros and ones, respectively.
3. Iterate through the input string `s`. If a zero is encountered, increment `zero_count`. If a one is encountered, check if `zero_count` is greater than 0. If it is, append `zero_count` to `seq` and reset `zero_count` to 0. Increment `one_count` regardless of the current character.
4. After iterating through the entire string, append any remaining `zero_count` to `seq`.
5. If `seq` has more than one element, iterate through it and compare each pair of adjacent elements. For each pair, calculate the sum and update the maximum sum `res` if necessary.
6. Return the maximum sum `res` plus the count of ones `one_count`.

**Time Complexity**
O(n), where n is the length of the input string `s`. This is because we iterate through the string twice: once to build the `seq` list and once to compare pairs of elements in `seq`.

**Space Complexity**
O(n), where n is the length of the input string `s`. This is because in the worst case, we may need to store all the blocks of zeros in the `seq` list.

**Key Insight**
The key insight is that by comparing pairs of adjacent blocks of zeros, we can find the maximum sum, which represents the maximum number of active sections that can be obtained by performing a trade. This is because the optimal trade will always involve converting a block of zeros to ones and vice versa, resulting in the maximum sum of active sections.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 463 ms (Beats 95.33%) |
| 💾 Memory | 21.1 MB (Beats 61.68%) |
| 📅 Solved | 2026-07-21 |
| 💻 Language | Python |