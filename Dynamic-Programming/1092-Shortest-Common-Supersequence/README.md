> 📌 **Cross-listed:** Primary location is [String/1092-Shortest-Common-Supersequence](../../String/1092-Shortest-Common-Supersequence). This problem also appears under: **String**, **Dynamic Programming**

# 1092. Shortest Common Supersequence 


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/shortest-common-supersequence/)


## 📝 Problem Description

Given two strings `str1` and `str2`, return *the shortest string that has both *`str1`* and *`str2`* as **subsequences***. If there are multiple valid strings, return **any** of them.

A string `s` is a **subsequence** of string `t` if deleting some number of characters from `t` (possibly `0`) results in the string `s`.

 

Example 1:**

```

**Input:** str1 = "abac", str2 = "cab"
**Output:** "cabac"
**Explanation:** 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

```

Example 2:**

```

**Input:** str1 = "aaaaaaaa", str2 = "aaaaaaaa"
**Output:** "aaaaaaaa"

```

 

**Constraints:**

	- `1 <= str1.length, str2.length <= 1000`

	- `str1` and `str2` consist of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to find the shortest string that has both `str1` and `str2` as subsequences. This can be achieved by finding the longest common subsequence (LCS) of `str1` and `str2` and appending the remaining characters from both strings. The key insight is that the LCS can be used to construct the shortest common supersequence.

**Approach**
1. Create a 2D table `dp` to store the LCS of `str1` and `str2`.
2. Initialize the first row and column of `dp` with the characters of `str1` and `str2` respectively.
3. Iterate through `str1` and `str2` from left to right, and for each pair of characters, check if they are equal. If they are, append the character to the LCS.
4. If the characters are not equal, choose the LCS from the previous row or column based on the length.
5. After filling the `dp` table, extract the LCS from the last cell.
6. Initialize two pointers `i` and `j` to the end of `str1` and `str2` respectively.
7. Iterate through the LCS from left to right, and for each character, append the corresponding characters from `str1` and `str2` to the result.
8. Finally, append the remaining characters from `str1` and `str2` to the result.

**Time Complexity**
O(n1 * n2), where n1 and n2 are the lengths of `str1` and `str2` respectively. This is because we are iterating through both strings once to fill the `dp` table, and then again to construct the result.

**Space Complexity**
O(n1 * n2), where n1 and n2 are the lengths of `str1` and `str2` respectively. This is because we are using a 2D table `dp` to store the LCS.

**Key Insight**
The key insight is that the LCS of `str1` and `str2` can be used to construct the shortest common supersequence. By appending the remaining characters from both strings to the LCS, we can obtain the shortest string that has both `str1` and `str2` as subsequences.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 399 ms (Beats 36.33%) |
| 💾 Memory | 21.4 MB (Beats 98.78%) |
| 📅 Solved | 2026-02-11 |
| 💻 Language | Python |