# 680. Valid Palindrome II


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/valid-palindrome-ii/)


## 📝 Problem Description

Given a string `s`, return `true` *if the *`s`* can be palindrome after deleting **at most one** character from it*.

 

Example 1:**

```

**Input:** s = "aba"
**Output:** true

```

Example 2:**

```

**Input:** s = "abca"
**Output:** true
**Explanation:** You could delete the character 'c'.

```

Example 3:**

```

**Input:** s = "abc"
**Output:** false

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The approach to this problem is to use two pointers, one at the start and one at the end of the string, and move them towards each other. If we encounter a mismatch, we create two new strings by deleting the character at the left or right pointer and check if either of them is a palindrome.

**Approach**
1. Initialize two pointers, `l` at the start and `r` at the end of the string.
2. While `l` is less than `r`, check if the characters at the current positions of `l` and `r` are equal.
3. If they are not equal, create two new strings by deleting the character at `l` or `r` and check if either of them is a palindrome by comparing it with its reverse.
4. If either of the new strings is a palindrome, return `True`.
5. If neither of the new strings is a palindrome, return `False`.
6. If the characters at the current positions of `l` and `r` are equal, move `l` to the right and `r` to the left.
7. If `l` is no longer less than `r`, return `True` because the string is a palindrome.

**Time Complexity**
O(n), where n is the length of the string. This is because in the worst case, we might have to create two new strings and check if they are palindromes, which takes O(n) time.

**Space Complexity**
O(n), where n is the length of the string. This is because in the worst case, we might have to create two new strings, each of which takes O(n) space.

**Key Insight**
The key insight here is that we can delete at most one character from the string and still have it be a palindrome. This means that if we encounter a mismatch, we can create two new strings by deleting the character at the left or right pointer and check if either of them is a palindrome. This approach allows us to solve the problem in O(n) time and O(n) space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 35 ms (Beats 81.42%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-03 |
| 💻 Language | Python |