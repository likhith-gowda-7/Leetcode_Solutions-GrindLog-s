# 567. Permutation in String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/permutation-in-string/)


## 📝 Problem Description

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

 

Example 1:**

```

**Input:** s1 = "ab", s2 = "eidbaooo"
**Output:** true
**Explanation:** s2 contains one permutation of s1 ("ba").

```

Example 2:**

```

**Input:** s1 = "ab", s2 = "eidboaoo"
**Output:** false

```

 

**Constraints:**

	- `1 <= s1.length, s2.length <= 10^4`

	- `s1` and `s2` consist of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by first comparing the frequency of characters in `s1` and `s2` within the first `len(s1)` characters of `s2`. If they match, it means `s1` is a permutation of the substring in `s2`. Then, it uses a sliding window approach to compare the frequency of characters in `s1` and `s2` as it moves the window to the right.

**Approach**
1. Initialize two arrays `c1` and `c2` to store the frequency of characters in `s1` and `s2` respectively.
2. Compare the frequency of characters in `s1` and `s2` within the first `len(s1)` characters of `s2`. If they match, return `True`.
3. If the frequency of characters in `s1` and `s2` do not match, move the window to the right by incrementing `r` and decrementing `l`.
4. Update the frequency of characters in `c2` by adding the character at `r` and subtracting the character at `l`.
5. Repeat step 3 until the end of `s2` is reached.

**Time Complexity**
O(n), where n is the length of `s2`. This is because we are scanning `s2` once and using a constant amount of time to update the frequency of characters in `c2`.

**Space Complexity**
O(1), because the size of `c1` and `c2` is constant (26 for lowercase English letters).

**Key Insight**
The key insight is that if the frequency of characters in `s1` and `s2` match at any point, it means `s1` is a permutation of the substring in `s2`. This is because the frequency of characters in a string is a unique identifier of the string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 18 ms (Beats 93.84%) |
| 💾 Memory | 12.9 MB (Beats 17.1%) |
| 📅 Solved | 2025-04-02 |
| 💻 Language | Python |