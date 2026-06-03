# 1653. Minimum Deletions to Make String Balanced


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/)


## 📝 Problem Description

You are given a string `s` consisting only of characters `'a'` and `'b'`​​​​.

You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] = 'b'` and `s[j]= 'a'`.

Return *the **minimum** number of deletions needed to make *`s`* **balanced***.

 

Example 1:**

```

**Input:** s = "aababbab"
**Output:** 2
**Explanation:** You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

```

Example 2:**

```

**Input:** s = "bbaaaaabb"
**Output:** 2
**Explanation:** The only solution is to delete the first two characters.

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is `'a'` or `'b'`​​.

## 🧠 Solution Explanation

**Intuition**
The problem asks for the minimum number of deletions needed to make the string balanced. A balanced string has no pairs of 'b' followed by 'a'. The solution uses a simple dynamic programming approach, keeping track of the minimum number of deletions required up to each position in the string.

**Approach**
1. Initialize variables `b` to count the number of 'b's seen so far and `min_del` to store the minimum number of deletions required.
2. Iterate through the string `s`. For each character:
   - If the character is 'b', increment `b`.
   - If the character is 'a', update `min_del` to be the minimum of its current value and `b` (the number of 'b's seen so far) plus 1.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we are iterating through the string once.

**Space Complexity**
O(1), as we are using a constant amount of space to store the variables `b` and `min_del`.

**Key Insight**
The key insight is that the minimum number of deletions required to balance the string up to a certain position is the minimum of the current minimum number of deletions and the number of 'b's seen so far plus 1. This is because we can either delete the current 'a' and keep the previous 'b's, or delete the previous 'b's and keep the current 'a'.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 141 ms (Beats 88.98%) |
| 💾 Memory | 20.1 MB (Beats 74.15%) |
| 📅 Solved | 2026-02-07 |
| 💻 Language | Python |