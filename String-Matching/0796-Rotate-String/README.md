> 📌 **Cross-listed:** Primary location is [String/0796-Rotate-String](../../String/0796-Rotate-String). This problem also appears under: **String**, **String Matching**

# 796. Rotate String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![String Matching](https://img.shields.io/badge/String%20Matching-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotate-string/)


## 📝 Problem Description

Given two strings `s` and `goal`, return `true` *if and only if* `s` *can become* `goal` *after some number of **shifts** on* `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

	- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

 

Example 1:**

```
**Input:** s = "abcde", goal = "cdeab"
**Output:** true

```
Example 2:**

```
**Input:** s = "abcde", goal = "abced"
**Output:** false

```

 

**Constraints:**

	- `1 <= s.length, goal.length <= 100`

	- `s` and `goal` consist of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by essentially "rotating" the string `s` to all possible positions and checking if `goal` is a substring of the rotated string. This is possible because a string can be rotated to match another string if and only if the two strings have the same length.

**Approach**
1. First, we check if the lengths of `s` and `goal` are equal. If not, we immediately return `False` because a string cannot be rotated to match another string of a different length.
2. We then concatenate `s` with itself. This is because we can rotate `s` to all possible positions by taking substrings of the concatenated string.
3. We check if `goal` is a substring of the concatenated string. If it is, we return `True` because `goal` can be obtained by rotating `s`.
4. If `goal` is not a substring of the concatenated string, we return `False`.

**Time Complexity**
O(n^2), where n is the length of `s`. This is because we are checking if `goal` is a substring of the concatenated string, which takes O(n^2) time in the worst case.

**Space Complexity**
O(n), where n is the length of `s`. This is because we are concatenating `s` with itself, which takes O(n) space.

**Key Insight**
The key insight is that a string can be rotated to match another string if and only if the two strings have the same length. This allows us to "rotate" the string by taking substrings of the concatenated string, making the problem much easier to solve.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 17.72%) |
| 📅 Solved | 2026-05-03 |
| 💻 Language | Python |