# 5. Longest Palindromic Substring


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)


## 📝 Problem Description

Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

 

Example 1:**

```

**Input:** s = "babad"
**Output:** "bab"
**Explanation:** "aba" is also a valid answer.

```

Example 2:**

```

**Input:** s = "cbbd"
**Output:** "bb"

```

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consist of only digits and English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer technique to expand around the center of a potential palindrome, considering both odd and even length palindromes. This approach leverages the fact that a palindrome can be formed by expanding around its center, and by considering both odd and even length palindromes, we can find the longest one.

**Approach**
1. Define a helper function `expand(l, r)` that takes two pointers `l` and `r` as input and expands around the center of a potential palindrome.
2. Initialize `res` as an empty string to store the longest palindrome found so far.
3. Iterate through the string `s` with a pointer `i`.
4. For each `i`, consider two types of palindromes:
	* Odd length palindrome: Call `expand(i, i)` to expand around the center of the palindrome.
	* Even length palindrome: Call `expand(i, i+1)` to expand around the center of the palindrome.
5. Update `res` with the longer palindrome found between the odd and even length palindromes.
6. Return `res` as the longest palindrome found.

**Time Complexity**
O(n^2), where n is the length of the string `s`. This is because in the worst case, we need to expand around each character in the string, resulting in a quadratic time complexity.

**Space Complexity**
O(1), as we only use a constant amount of space to store the pointers and the result.

**Key Insight**
The key insight is that a palindrome can be formed by expanding around its center, and by considering both odd and even length palindromes, we can find the longest one. This approach allows us to efficiently search for the longest palindrome in the string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 207 ms (Beats 93.15%) |
| 💾 Memory | 19.6 MB (Beats 15.83%) |
| 📅 Solved | 2026-01-25 |
| 💻 Language | Python |