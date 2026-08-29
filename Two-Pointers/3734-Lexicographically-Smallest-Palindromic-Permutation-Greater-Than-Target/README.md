# 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/)


## 📝 Problem Description

You are given two strings `s` and `target`, each of length `n`, consisting of lowercase English letters.

Return the **lexicographically smallest string** that is **both** a **palindromic permutation** of `s` and **strictly** greater than `target`. If no such permutation exists, return an empty string.

 

Example 1:**

**Input:** s = "baba", target = "abba"

**Output:** "baab"

**Explanation:**

	- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.

	- The lexicographically smallest permutation that is strictly greater than `target` is `"baab"`.

Example 2:**

**Input:** s = "baba", target = "bbaa"

**Output:** ""

**Explanation:**

	- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.

	- None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

Example 3:**

**Input:** s = "abc", target = "abb"

**Output:** ""

**Explanation:**

`s` has no palindromic permutations. Therefore, the answer is `""`.

Example 4:**

**Input:** s = "aac", target = "abb"

**Output:** "aca"

**Explanation:**

	- The only palindromic permutation of `s` is `"aca"`.

	- `"aca"` is strictly greater than `target`. Therefore, the answer is `"aca"`.

 

**Constraints:**

	- `1 <= n == s.length == target.length <= 300`

	- `s` and `target` consist of only lowercase English letters.

## 🧠 Solution Explanation

**Intuition**  
A palindrome is fixed once its left half and (if odd) middle character are chosen.  
If we can guarantee that the *largest* palindrome that can be built from the remaining letters still exceeds `target`, then any smaller completion will also be > `target`.  
Thus we can greedily pick the smallest possible character for each position of the left half, checking this feasibility condition.

**Approach**  
1. Count frequencies of `s`.  
2. Identify at most one odd‑count letter → it becomes the middle (`mid`).  
   Reduce all counts by half (each will appear that many times in the left half).  
   If more than one odd count exists → no palindrome → return `""`.  
3. For each of the `n/2` positions of the left half:  
   a. Try letters `'a'` to `'z'` in order.  
   b. Temporarily decrement its count and append it to the current prefix.  
   c. Call `isPossible`:  
      - Build the *largest* palindrome from the remaining counts (descending order).  
      - If this palindrome > `target`, return it; otherwise return `""`.  
   d. If `isPossible` succeeds, lock the letter in the prefix, record the returned palindrome as a candidate, and break to the next position.  
   e. If no letter works, return `""`.  
4. After all positions are fixed, return the smallest candidate found.

**Time Complexity**  
For each of the `n/2` positions we try up to 26 letters, and each feasibility check builds a string of length `n`.  
Thus `O((n/2) * 26 * n) = O(n²)` time.  
(26 is a constant, so the algorithm

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 687 ms (Beats 5.8%) |
| 💾 Memory | 19.5 MB (Beats 47.83%) |
| 📅 Solved | 2026-08-28 |
| 💻 Language | Python |