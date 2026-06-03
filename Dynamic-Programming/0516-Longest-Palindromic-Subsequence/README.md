> 📌 **Cross-listed:** Primary location is [String/0516-Longest-Palindromic-Subsequence](../../String/0516-Longest-Palindromic-Subsequence). This problem also appears under: **String**, **Dynamic Programming**

# 516. Longest Palindromic Subsequence


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence/)


## 📝 Problem Description

Given a string `s`, find *the longest palindromic **subsequence**'s length in* `s`.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:**

```

**Input:** s = "bbbab"
**Output:** 4
**Explanation:** One possible longest palindromic subsequence is "bbbb".

```

Example 2:**

```

**Input:** s = "cbbd"
**Output:** 2
**Explanation:** One possible longest palindromic subsequence is "bb".

```

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists only of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The problem can be solved by treating the input string as one sequence and its reverse as another sequence. The longest palindromic subsequence's length is equivalent to the length of the longest common subsequence between the two sequences. This is because a palindromic subsequence must appear in both the original string and its reverse.

**Approach**
1. Create two sequences: `text1` as the input string `s` and `text2` as the reverse of `s`.
2. Initialize a dynamic programming (DP) table `dp` of size `n+1`, where `n` is the length of `s`.
3. Iterate over `text1` from right to left (i.e., from index `n-1` to `0`).
4. For each character in `text1`, iterate over `text2` from right to left (i.e., from index `n-1` to `0`).
5. If the current characters in `text1` and `text2` match, update the DP value at the current index `j` to be `1` plus the maximum DP value at the previous index `j-1`.
6. If the current characters do not match, update the DP value at the current index `j` to be the maximum of the DP value at the current index `j` and the DP value at the next index `j+1`.
7. After iterating over all characters in `text1`, the DP value at index `0` represents the length of the longest palindromic subsequence.

**Time Complexity**
O(n^2), where n is the length of the input string `s`. This is because we have two nested loops that iterate over the characters in `text1` and `text2`.

**Space Complexity**
O(n), where n is the length of the input string `s`. This is because we need to store the DP table of size `n+1`.

**Key Insight**
The key insight is to recognize that the longest palindromic subsequence problem can be reduced to finding the length of the longest common subsequence between the input string and its reverse. This allows us to use dynamic programming to efficiently compute the solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 688 ms (Beats 65.87%) |
| 💾 Memory | 19.4 MB (Beats 92.6%) |
| 📅 Solved | 2026-01-22 |
| 💻 Language | Python |