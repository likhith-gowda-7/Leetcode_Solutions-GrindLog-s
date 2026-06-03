> 📌 **Cross-listed:** Primary location is [String/0072-Edit-Distance](../../String/0072-Edit-Distance). This problem also appears under: **String**, **Dynamic Programming**

# 72. Edit Distance


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/edit-distance/)


## 📝 Problem Description

Given two strings `word1` and `word2`, return *the minimum number of operations required to convert `word1` to `word2`*.

You have the following three operations permitted on a word:

	- Insert a character

	- Delete a character

	- Replace a character

 

Example 1:**

```

**Input:** word1 = "horse", word2 = "ros"
**Output:** 3
**Explanation:** 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

```

Example 2:**

```

**Input:** word1 = "intention", word2 = "execution"
**Output:** 5
**Explanation:** 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

```

 

**Constraints:**

	- `0 <= word1.length, word2.length <= 500`

	- `word1` and `word2` consist of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming to build a 2D table where each cell represents the minimum edit distance between the substrings of `word1` and `word2` up to that point. The key insight is that the minimum edit distance between two strings is the minimum of the edit distances between the substrings without the last characters, plus 1 for the operation required to align the last characters.

**Approach**
1. Initialize a 1D table `dp` of size `n2+1` to store the minimum edit distances between `word1` and the substrings of `word2`.
2. For each character in `word1`, create a new 1D table `curr` of size `n2+1` to store the minimum edit distances between the current substring of `word1` and the substrings of `word2`.
3. For each character in `word2`, calculate the minimum edit distance by considering the minimum of the edit distances between the substrings without the last characters, plus 1 for the operation required to align the last characters.
4. Update the `dp` table with the `curr` table.
5. Repeat steps 2-4 until all characters in `word1` have been processed.
6. The minimum edit distance is stored in the last cell of the `dp` table.

**Time Complexity**
O(n1 \* n2), where n1 and n2 are the lengths of `word1` and `word2`, respectively. This is because we need to iterate over all characters in both strings to fill up the 2D table.

**Space Complexity**
O(n2), where n2 is the length of `word2`. This is because we need to store the minimum edit distances between `word1` and the substrings of `word2` up to the current point.

**Key Insight**
The key insight is that the minimum edit distance between two strings is the minimum of the edit distances between the substrings without the last characters, plus 1 for the operation required to align the last characters. This allows us to build up the 2D table efficiently using dynamic programming.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 44 ms (Beats 68.11%) |
| 💾 Memory | 19.4 MB (Beats 90.24%) |
| 📅 Solved | 2026-02-20 |
| 💻 Language | Python |