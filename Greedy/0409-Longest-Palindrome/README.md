> 📌 **Cross-listed:** Primary location is [Hash Table/0409-Longest-Palindrome](../../Hash-Table/0409-Longest-Palindrome). This problem also appears under: **Hash Table**, **String**, **Greedy**

# 409. Longest Palindrome


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-palindrome/)


## 📝 Problem Description

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest palindrome** that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.

 

Example 1:**

```

**Input:** s = "abccccdd"
**Output:** 7
**Explanation:** One longest palindrome that can be built is "dccaccd", whose length is 7.

```

Example 2:**

```

**Input:** s = "a"
**Output:** 1
**Explanation:** The longest palindrome that can be built is "a", whose length is 1.

```

 

**Constraints:**

	- `1 <= s.length <= 2000`

	- `s` consists of lowercase **and/or** uppercase English letters only.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table (implemented as a set in Python) to count the frequency of each character in the string. Since a palindrome can have at most one character that appears an odd number of times, we can count the number of pairs of characters and add 1 if there is a character that appears an odd number of times.

**Approach**
1. Initialize an empty set `pair` to store the characters that appear an even number of times.
2. Iterate through the string `s`. For each character `i`:
   1. If `i` is already in `pair`, it means we have found a pair of `i`. Remove `i` from `pair` and increment `max_len` by 2.
   2. If `i` is not in `pair`, add it to `pair`.
3. If `pair` is not empty after iterating through the string, it means there is a character that appears an odd number of times. Add 1 to `max_len`.
4. Return `max_len`.

**Time Complexity**
O(n), where n is the length of the string `s`. We only need to iterate through the string once to count the frequency of each character.

**Space Complexity**
O(n), where n is the length of the string `s`. In the worst case, all characters in the string appear an even number of times, and we need to store all of them in the set `pair`.

**Key Insight**
The key insight is that a palindrome can have at most one character that appears an odd number of times. By counting the frequency of each character and storing the characters that appear an even number of times in a set, we can efficiently calculate the length of the longest palindrome that can be built with the given letters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-02-12 |
| 💻 Language | Python |