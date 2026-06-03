> 📌 **Cross-listed:** Primary location is [String/1312-Minimum-Insertion-Steps-to-Make-a-String-Palindrome](../../String/1312-Minimum-Insertion-Steps-to-Make-a-String-Palindrome). This problem also appears under: **String**, **Dynamic Programming**

# 1312. Minimum Insertion Steps to Make a String Palindrome


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)


## 📝 Problem Description

Given a string `s`. In one step you can insert any character at any index of the string.

Return *the minimum number of steps* to make `s` palindrome.

A **Palindrome String** is one that reads the same backward as well as forward.

 

Example 1:**

```

**Input:** s = "zzazz"
**Output:** 0
**Explanation:** The string "zzazz" is already palindrome we do not need any insertions.

```

Example 2:**

```

**Input:** s = "mbadm"
**Output:** 2
**Explanation:** String can be "mbdadbm" or "mdbabdm".

```

Example 3:**

```

**Input:** s = "leetcode"
**Output:** 5
**Explanation:** Inserting 5 characters the string becomes "leetcodocteel".

```

 

**Constraints:**

	- `1 <= s.length <= 500`

	- `s` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
This solution works by treating the input string as the first text and its reverse as the second text. It then uses dynamic programming to find the length of the longest common subsequence between the two texts, which is equivalent to the minimum number of insertions required to make the input string a palindrome.

**Approach**
1. Create two strings: `text1` is the input string and `text2` is the reverse of the input string.
2. Initialize a dynamic programming table `dp` of size `n2+1`, where `n2` is the length of `text2`.
3. Iterate over `text1` from left to right, and for each character, iterate over `text2` from left to right.
4. If the current characters in `text1` and `text2` are the same, update `dp[j]` to be `1 + prev`, where `prev` is the value of `dp[j-1]`.
5. If the current characters are different, update `dp[j]` to be the maximum of `temp` (the previous value of `dp[j]`) and `dp[j-1]`.
6. After filling the `dp` table, return `n1 - dp[-1]`, where `n1` is the length of `text1`.

**Time Complexity**
O(n1 * n2), where n1 and n2 are the lengths of `text1` and `text2`, respectively. This is because we are iterating over `text1` and `text2` in a nested loop.

**Space Complexity**
O(n2), where n2 is the length of `text2`. This is because we are using a dynamic programming table of size `n2+1`.

**Key Insight**
The key insight here is that the minimum number of insertions required to make a string a palindrome is equivalent to the length of the longest common subsequence between the string and its reverse. This is because we can always insert characters to make the string match the longest common subsequence, and the remaining characters will be the ones that need to be inserted to make the string a palindrome.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 350 ms (Beats 68.53%) |
| 💾 Memory | 19.4 MB (Beats 88.53%) |
| 📅 Solved | 2026-02-03 |
| 💻 Language | Python |