> 📌 **Cross-listed:** Primary location is [String/0583-Delete-Operation-for-Two-Strings](../../String/0583-Delete-Operation-for-Two-Strings). This problem also appears under: **String**, **Dynamic Programming**

# 583. Delete Operation for Two Strings


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/delete-operation-for-two-strings/)


## 📝 Problem Description

Given two strings `word1` and `word2`, return *the minimum number of **steps** required to make* `word1` *and* `word2` *the same*.

In one **step**, you can delete exactly one character in either string.

 

Example 1:**

```

**Input:** word1 = "sea", word2 = "eat"
**Output:** 2
**Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

```

Example 2:**

```

**Input:** word1 = "leetcode", word2 = "etco"
**Output:** 4

```

 

**Constraints:**

	- `1 <= word1.length, word2.length <= 500`

	- `word1` and `word2` consist of only lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using dynamic programming by building a 2D table where each cell represents the minimum number of operations required to make the substrings up to the current indices in `word1` and `word2` the same. The key insight is that we can either delete a character from `word1` or `word2` or keep the characters the same if they match.

**Approach**
1. Initialize a 2D table `dp` with dimensions `(n1+1) x (n2+1)` where `n1` and `n2` are the lengths of `word1` and `word2` respectively.
2. Iterate over the characters in `word1` from left to right and `word2` from left to right.
3. For each pair of characters, if they match, the minimum number of operations is 1 plus the minimum number of operations for the substrings without these characters.
4. If the characters do not match, the minimum number of operations is the maximum of the minimum number of operations for the substrings without the current character in `word1` or `word2`.
5. Update the `dp` table with the minimum number of operations for each pair of characters.
6. The minimum number of operations to make `word1` and `word2` the same is the sum of the number of characters in `word1` and `word2` minus the minimum number of operations for the entire strings.

**Time Complexity**
O(n1 * n2) where n1 and n2 are the lengths of `word1` and `word2` respectively. This is because we are iterating over each pair of characters in the strings.

**Space Complexity**
O(n2) where n2 is the length of `word2`. This is because we are storing the minimum number of operations for each substring of `word2`.

**Key Insight**
The key insight is that we can use dynamic programming to build a table of minimum number of operations for each pair of substrings, and then use this table to find the minimum number of operations for the entire strings. This approach allows us to avoid recomputing the minimum number of operations for each pair of substrings, resulting in a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 60 ms (Beats 94.78%) |
| 💾 Memory | 19.3 MB (Beats 95.98%) |
| 📅 Solved | 2026-02-08 |
| 💻 Language | Python |