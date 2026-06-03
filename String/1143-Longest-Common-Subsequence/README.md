# 1143. Longest Common Subsequence


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-common-subsequence/)


## 📝 Problem Description

Given two strings `text1` and `text2`, return *the length of their longest **common subsequence**. *If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

	- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

 

Example 1:**

```

**Input:** text1 = "abcde", text2 = "ace" 
**Output:** 3  
**Explanation:** The longest common subsequence is "ace" and its length is 3.

```

Example 2:**

```

**Input:** text1 = "abc", text2 = "abc"
**Output:** 3
**Explanation:** The longest common subsequence is "abc" and its length is 3.

```

Example 3:**

```

**Input:** text1 = "abc", text2 = "def"
**Output:** 0
**Explanation:** There is no such common subsequence, so the result is 0.

```

 

**Constraints:**

	- `1 <= text1.length, text2.length <= 1000`

	- `text1` and `text2` consist of only lowercase English characters.

## 🧠 Solution Explanation

**Intuition**
The problem asks for the length of the longest common subsequence between two strings. The key insight is that we can use dynamic programming to build up a table of lengths of common subsequences between prefixes of the two strings.

**Approach**
1. Initialize a 2D table `dp` with dimensions `(n1+1) x (n2+1)`, where `n1` and `n2` are the lengths of the two input strings. The extra row and column are for handling base cases effectively.
2. Iterate over the characters of the first string from right to left (`i` ranges from `n1-1` to `0`).
3. For each character in the first string, iterate over the characters of the second string from right to left (`j` ranges from `n2-1` to `0`).
4. If the current characters in both strings match, update the length of the common subsequence by adding 1 to the length of the common subsequence without the current characters.
5. If the current characters do not match, update the length of the common subsequence by taking the maximum of the length of the common subsequence without the current character in the second string and the length of the common subsequence without the current character in the first string.
6. Return the length of the common subsequence for the entire first string.

**Time Complexity**
O(n1 * n2), where n1 and n2 are the lengths of the two input strings. This is because we are iterating over the characters of both strings once.

**Space Complexity**
O(n1 * n2), where n1 and n2 are the lengths of the two input strings. This is because we are using a 2D table of size (n1+1) x (n2+1) to store the lengths of common subsequences.

**Key Insight**
The key insight is that we can use dynamic programming to build up a table of lengths of common subsequences between prefixes of the two strings. This allows us to avoid recomputing the length of the common subsequence for each prefix, resulting in a more efficient algorithm.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 241 ms (Beats 94.53%) |
| 💾 Memory | 19.4 MB (Beats 88.66%) |
| 📅 Solved | 2026-01-12 |
| 💻 Language | Python |