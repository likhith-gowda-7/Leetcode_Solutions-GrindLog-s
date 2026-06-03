> 📌 **Cross-listed:** Primary location is [String/0712-Minimum-ASCII-Delete-Sum-for-Two-Strings](../../String/0712-Minimum-ASCII-Delete-Sum-for-Two-Strings). This problem also appears under: **String**, **Dynamic Programming**

# 712. Minimum ASCII Delete Sum for Two Strings


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)


## 📝 Problem Description

Given two strings `s1` and `s2`, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

 

Example 1:**

```

**Input:** s1 = "sea", s2 = "eat"
**Output:** 231
**Explanation:** Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

```

Example 2:**

```

**Input:** s1 = "delete", s2 = "leet"
**Output:** 403
**Explanation:** Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

```

 

**Constraints:**

	- `1 <= s1.length, s2.length <= 1000`

	- `s1` and `s2` consist of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
This problem can be solved using dynamic programming by building a 2D table where each cell represents the minimum ASCII sum of deleted characters to make two substrings equal. The key insight is that we can either delete a character from the first string and add its ASCII value to the sum, or delete a character from the second string and add its ASCII value to the sum.

**Approach**
1. Initialize a 2D table `dp` with dimensions `(n1+1) x (n2+1)`, where `n1` and `n2` are the lengths of the two input strings. Fill the first row and first column with the ASCII values of the characters in the first and second strings, respectively.
2. Iterate over the 2D table, starting from the second row and second column. For each cell `dp[i][j]`, check if the characters at positions `i-1` and `j-1` are equal. If they are, set `dp[i][j]` to `dp[i-1][j-1]`, meaning that no characters need to be deleted.
3. If the characters are not equal, calculate the minimum ASCII sum of deleted characters by considering two options: deleting a character from the first string and adding its ASCII value to the sum, or deleting a character from the second string and adding its ASCII value to the sum. Choose the minimum of these two options and store it in `dp[i][j]`.
4. After filling the 2D table, return the value in the bottom-right cell, which represents the minimum ASCII sum of deleted characters to make the two input strings equal.

**Time Complexity**
O(n1 * n2), where n1 and n2 are the lengths of the two input strings. This is because we need to fill a 2D table with dimensions (n1+1) x (n2+1), and each cell requires a constant amount of time to compute.

**Space Complexity**
O(n1 * n2), which is the size of the 2D table. We need to store the ASCII values of the characters in the first and second strings, as well as the minimum ASCII sum of deleted characters for each cell.

**Key Insight**
The key insight is that we can use dynamic programming to build a 2D table where each cell represents the minimum ASCII sum of deleted characters to make two substrings equal. By considering two options for each cell (deleting a character from the first string or deleting a character from the second string), we can find the minimum ASCII sum of deleted characters to make the two input strings equal.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 273 ms (Beats 42.97%) |
| 💾 Memory | 23.8 MB (Beats 32.23%) |
| 📅 Solved | 2026-01-10 |
| 💻 Language | Python |