> 📌 **Cross-listed:** Primary location is [Hash Table/3720-Lexicographically-Smallest-Permutation-Greater-Than-Target](../../Hash-Table/3720-Lexicographically-Smallest-Permutation-Greater-Than-Target). This problem also appears under: **Hash Table**, **String**, **Greedy**, **Counting**, **Enumeration**

# 3720. Lexicographically Smallest Permutation Greater Than Target


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/)


## 📝 Problem Description

You are given two strings `s` and `target`, both having length `n`, consisting of lowercase English letters.

Return the **lexicographically smallest permutation** of `s` that is **strictly** greater than `target`. If no permutation of `s` is lexicographically strictly greater than `target`, return an empty string.

A string `a` is **lexicographically strictly greater **than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`.

 

Example 1:**

**Input:** s = "abc", target = "bba"

**Output:** "bca"

**Explanation:**

	- The permutations of `s` (in lexicographical order) are `"abc"`, `"acb"`, `"bac"`, `"bca"`, `"cab"`, and `"cba"`.

	- The lexicographically smallest permutation that is strictly greater than `target` is `"bca"`.

Example 2:**

**Input:** s = "leet", target = "code"

**Output:** "eelt"

**Explanation:**

	- The permutations of `s` (in lexicographical order) are `"eelt"`, `"eetl"`, `"elet"`, `"elte"`, `"etel"`, `"etle"`, `"leet"`, `"lete"`, `"ltee"`, `"teel"`, `"tele"`, and `"tlee"`.

	- The lexicographically smallest permutation that is strictly greater than `target` is `"eelt"`.

Example 3:**

**Input:** s = "baba", target = "bbaa"

**Output:** ""

**Explanation:**

	- The permutations of `s` (in lexicographical order) are `"aabb"`, `"abab"`, `"abba"`, `"baab"`, `"baba"`, and `"bbaa"`.

	- None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

 

**Constraints:**

	- `1 <= s.length == target.length <= 300`

	- `s` and `target` consist of only lowercase English letters.

## 🧠 Solution Explanation

**Intuition**  
To beat `target` lexicographically we can keep the prefix of `target` unchanged until a position where we can place a larger letter from `s`. After that position the rest of the string must be the smallest possible, i.e., sorted ascending.  

**Approach**  
1. Count occurrences of each letter in `s` (`cnt[26]`).  
2. Subtract the counts of `target` to know which letters are “available” after trying to match the whole target.  
3. Scan `target` from right to left.  
   * Re‑add the letter at position `i` to `cnt` (since we are abandoning that exact match).  
   * If any count becomes negative, the prefix `target[:i]` cannot be formed – skip.  
   * Otherwise, look for the smallest letter `c > target[i]` that still has a positive count.  
   * If found, decrement its count, build the answer:  
     - prefix `target[:i]`  
     - the chosen larger letter `c`  
     - all remaining letters in ascending order (by iterating `cnt`).  
   * Return this string immediately.  
4. If no position yields a larger letter, return `""`.  

**Time Complexity**  
The outer loop runs `n` times; inside we scan at most 26 letters to find `c` and again 26 to append the tail.  
`O(n * 26) = O(n)` time.  

**Space Complexity**  
Only the 26‑element count array and the output string are used.  
`O(1)` auxiliary space (output excluded).  

**Key Insight**  
The first place where we can replace a target character with a larger one determines the entire answer; after that, the minimal suffix is simply the sorted remaining letters. This greedy choice guarantees the lexicographically smallest permutation that is still greater than `target`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 53.06%) |
| 💾 Memory | 19.5 MB (Beats 31.62%) |
| 📅 Solved | 2026-08-27 |
| 💻 Language | Python |