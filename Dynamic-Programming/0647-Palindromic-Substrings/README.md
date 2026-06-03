> 📌 **Cross-listed:** Primary location is [Two Pointers/0647-Palindromic-Substrings](../../Two-Pointers/0647-Palindromic-Substrings). This problem also appears under: **Two Pointers**, **String**, **Dynamic Programming**

# 647. Palindromic Substrings


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/palindromic-substrings/)


## 📝 Problem Description

Given a string `s`, return *the number of **palindromic substrings** in it*.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

 

Example 1:**

```

**Input:** s = "abc"
**Output:** 3
**Explanation:** Three palindromic strings: "a", "b", "c".

```

Example 2:**

```

**Input:** s = "aaa"
**Output:** 6
**Explanation:** Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

```

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a dynamic programming approach to count the number of palindromic substrings in the given string. It iterates over the string, expanding outwards from each character to check for palindromes of increasing lengths.

**Approach**
1. Initialize a counter `total` to store the number of palindromic substrings.
2. Define a helper function `check(l, r)` that checks if the substring from index `l` to `r` is a palindrome.
3. Iterate over the string, and for each character, call `check(i, i)` to check for single-character palindromes and `check(i, i+1)` to check for two-character palindromes.
4. In the `check` function, use two pointers `l` and `r` to expand outwards from the center of the substring, incrementing the `total` counter for each palindrome found.

**Time Complexity**
O(n^2), where n is the length of the string. This is because in the worst case, we need to check all substrings of the string, which results in a quadratic number of operations.

**Space Complexity**
O(1), as we only use a constant amount of space to store the `total` counter and the `check` function's variables.

**Key Insight**
The key insight is that we can use a single function `check` to handle both single-character and two-character palindromes, and then use a simple loop to iterate over the string and call `check` for each character. This simplifies the code and makes it more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 115 ms (Beats 80.47%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-10-28 |
| 💻 Language | Python |