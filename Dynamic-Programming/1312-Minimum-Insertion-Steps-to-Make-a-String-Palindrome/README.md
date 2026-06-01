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

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 350 ms (Beats 68.53%) |
| 💾 Memory | 19.4 MB (Beats 88.53%) |
| 📅 Solved | 2026-02-03 |
| 💻 Language | Python |