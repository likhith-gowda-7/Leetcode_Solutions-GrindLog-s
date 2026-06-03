# 1930. Unique Length-3 Palindromic Subsequences


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/)


## 📝 Problem Description

Given a string `s`, return *the number of **unique palindromes of length three** that are a **subsequence** of *`s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

	- For example, `"ace"` is a subsequence of `"abcde"`.

 

Example 1:**

```

**Input:** s = "aabca"
**Output:** 3
**Explanation:** The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

```

Example 2:**

```

**Input:** s = "adc"
**Output:** 0
**Explanation:** There are no palindromic subsequences of length 3 in "adc".

```

Example 3:**

```

**Input:** s = "bbcbaba"
**Output:** 4
**Explanation:** The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

```

 

**Constraints:**

	- `3 <= s.length <= 10^5`

	- `s` consists of only lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a simple yet efficient approach to count unique palindromic subsequences of length three in a given string. It iterates over each unique character in the string, finds its start and end indices, and then counts the unique middle elements between these indices.

**Approach**

1. Initialize a variable `res` to store the count of unique palindromic subsequences.
2. Iterate over each unique character `ch` in the string `s`. This is done using a set comprehension, which has a time complexity of O(26) = O(1) since there are only 26 unique characters in the English alphabet.
3. For each unique character `ch`, find its start index `start` and end index `end` in the string `s`. This is done using the `find` and `rfind` methods, which have a time complexity of O(N) each.
4. Create a set `middle_elements` of unique elements between the start and end indices (excluding the start and end indices themselves). This is done by slicing the string `s` from `start+1` to `end` and converting the result to a set.
5. Increment the `res` count by the size of the `middle_elements` set, which represents the number of unique palindromic subsequences of length three for the current character `ch`.
6. Return the final count `res`.

**Time Complexity**
The time complexity of the solution is O(N), where N is the length of the string `s`. This is because the `find` and `rfind` methods have a time complexity of O(N) each, and they are called for each unique character in the string.

**Space Complexity**
The space complexity of the solution is O(N), where N is the length of the string `s`. This is because the `middle_elements` set can store up to N elements in the worst case.

**Key Insight**
The key insight behind this solution is that a palindromic subsequence of length three can be formed by taking any character as the middle element and its two adjacent characters. By iterating over each unique character and counting the unique middle elements, we can efficiently count the total number of unique palindromic subsequences of length three in the string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 91 ms (Beats 68.04%) |
| 💾 Memory | 18.5 MB (Beats 100%) |
| 📅 Solved | 2025-11-22 |
| 💻 Language | Python |