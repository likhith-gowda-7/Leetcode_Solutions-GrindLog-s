> 📌 **Cross-listed:** Primary location is [String/3517-Smallest-Palindromic-Rearrangement-I](../../String/3517-Smallest-Palindromic-Rearrangement-I). This problem also appears under: **String**, **Sorting**, **Counting Sort**

# 3517. Smallest Palindromic Rearrangement I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Counting Sort](https://img.shields.io/badge/Counting%20Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-i/)


## 📝 Problem Description

You are given a **palindromic** string `s`.

Return the **lexicographically smallest** palindromic permutation of `s`.

 

Example 1:**

**Input:** s = "z"

**Output:** "z"

**Explanation:**

A string of only one character is already the lexicographically smallest palindrome.

Example 2:**

**Input:** s = "babab"

**Output:** "abbba"

**Explanation:**

Rearranging `"babab"` &rarr; `"abbba"` gives the smallest lexicographic palindrome.

Example 3:**

**Input:** s = "daccad"

**Output:** "acddca"

**Explanation:**

Rearranging `"daccad"` &rarr; `"acddca"` gives the smallest lexicographic palindrome.

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters.

	- `s` is guaranteed to be palindromic.

## 🧠 Solution Explanation

**Intuition**
The solution takes advantage of the fact that the input string `s` is guaranteed to be palindromic. This means that the first half of the string will be the same as the second half, but in reverse order. The goal is to find the lexicographically smallest palindromic permutation of `s`, which can be achieved by rearranging the characters in the string.

**Approach**
1. Count the frequency of each character in the string `s` using a `Counter` object.
2. Initialize an empty string `res` to store the first half of the palindromic permutation.
3. Iterate over all lowercase English letters (a-z).
4. For each letter `ch`, if its frequency in `s` is greater than 0, check if the frequency is odd.
5. If the frequency is odd, store `ch` as the middle character `mid`.
6. Append `ch` repeated `h1[ch]//2` times to `res`.
7. Finally, return the concatenated string `res+mid+res[::-1]`, which is the lexicographically smallest palindromic permutation of `s`.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we iterate over all characters in `s` once to count their frequencies, and then iterate over all lowercase English letters once to construct the palindromic permutation.

**Space Complexity**
O(1), excluding the space needed for the input string `s`. This is because we use a fixed amount of space to store the `Counter` object and the `res` string, regardless of the size of `s`.

**Key Insight**
The key insight is that the lexicographically smallest palindromic permutation of a palindromic string can be obtained by rearranging the characters in the string, with the middle character (if it exists) being the one with the smallest frequency. This allows us to construct the permutation in a single pass over the string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 161 ms (Beats 87.5%) |
| 💾 Memory | 21 MB (Beats 51.79%) |
| 📅 Solved | 2026-07-29 |
| 💻 Language | Python |