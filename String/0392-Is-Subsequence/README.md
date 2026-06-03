> 📌 **Cross-listed:** Primary location is [Two Pointers/0392-Is-Subsequence](../../Two-Pointers/0392-Is-Subsequence). This problem also appears under: **Two Pointers**, **String**, **Dynamic Programming**

# 392. Is Subsequence


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/is-subsequence/)


## 📝 Problem Description

Given two strings `s` and `t`, return `true`* if *`s`* is a **subsequence** of *`t`*, or *`false`* otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

 

Example 1:**

```
**Input:** s = "abc", t = "ahbgdc"
**Output:** true

```
Example 2:**

```
**Input:** s = "axc", t = "ahbgdc"
**Output:** false

```

 

**Constraints:**

	- `0 <= s.length <= 100`

	- `0 <= t.length <= 10^4`

	- `s` and `t` consist only of lowercase English letters.

 

**Follow up:** Suppose there are lots of incoming `s`, say `s_1, s_2, ..., s_k` where `k >= 10^9`, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer technique to traverse both strings `s` and `t` simultaneously. It checks if the characters at the current positions of both strings match, and if they do, it increments the pointer for string `s`. This approach ensures that we are considering the characters of string `s` in the correct order.

**Approach**
1. Initialize two pointers, `i` and `j`, to 0, which represent the current positions in strings `s` and `t`, respectively.
2. Enter a while loop that continues as long as both `i` is within the bounds of string `s` and `j` is within the bounds of string `t`.
3. Inside the loop, check if the characters at positions `i` and `j` in strings `s` and `t` are equal. If they are, increment `i` to move to the next character in string `s`.
4. Regardless of whether the characters match, increment `j` to move to the next character in string `t`.
5. After the loop, check if `i` has reached the end of string `s`. If it has, return `True`, indicating that string `s` is a subsequence of string `t`. Otherwise, return `False`.

**Time Complexity**
O(n + m), where n and m are the lengths of strings `s` and `t`, respectively. This is because we are traversing both strings once, and the number of operations is directly proportional to the lengths of the strings.

**Space Complexity**
O(1), as we are using a constant amount of space to store the pointers `i` and `j`, regardless of the input sizes.

**Key Insight**
The key insight is that we can use a two-pointer technique to traverse both strings simultaneously, checking for matches at each position. This approach allows us to efficiently determine if string `s` is a subsequence of string `t` by considering the characters in the correct order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-01-06 |
| 💻 Language | Python |