# 242. Valid Anagram


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/valid-anagram/)


## 📝 Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

 

**Constraints:**

	- `1 <= s.length, t.length <= 5 * 10^4`

	- `s` and `t` consist of lowercase English letters.

 

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## 🧠 Solution Explanation

**Intuition**
The solution works by comparing the frequency of each character in both strings. If the two strings are anagrams, they must contain the same characters with the same frequency. This approach takes advantage of the fact that anagrams can be transformed into each other by rearranging their characters.

**Approach**
1. Check if the lengths of the two strings are equal. If not, return False immediately, as anagrams must have the same number of characters.
2. Create two empty dictionaries, `h1` and `h2`, to store the frequency of each character in the first and second strings, respectively.
3. Iterate over the characters in the first string and update the frequency of each character in `h1`.
4. Iterate over the characters in the second string and update the frequency of each character in `h2`.
5. Compare the two dictionaries, `h1` and `h2`. If they are equal, return True; otherwise, return False.

**Time Complexity**
O(n + m), where n and m are the lengths of the two strings. This is because we iterate over each character in both strings once.

**Space Complexity**
O(n + m), where n and m are the lengths of the two strings. This is because in the worst case, we need to store all characters in the dictionaries.

**Key Insight**
The key insight is that anagrams can be compared by counting the frequency of each character, rather than comparing the characters themselves. This approach is efficient and scalable, even for large strings.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 91.19%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-01-17 |
| 💻 Language | Python |