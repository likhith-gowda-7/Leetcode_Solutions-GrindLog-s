> 📌 **Cross-listed:** Primary location is [String/0940-Distinct-Subsequences-II](../../String/0940-Distinct-Subsequences-II). This problem also appears under: **String**, **Dynamic Programming**

# 940. Distinct Subsequences II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/distinct-subsequences-ii/)


## 📝 Problem Description

Given a string s, return *the number of **distinct non-empty subsequences** of* `s`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not.
 

Example 1:**

```

**Input:** s = "abc"
**Output:** 7
**Explanation:** The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

```

Example 2:**

```

**Input:** s = "aba"
**Output:** 6
**Explanation:** The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

```

Example 3:**

```

**Input:** s = "aaa"
**Output:** 3
**Explanation:** The 3 distinct subsequences are "a", "aa" and "aaa".

```

 

**Constraints:**

	- `1 <= s.length <= 2000`

	- `s` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**  
Each new character can be appended to every existing distinct subsequence, plus it can start a new subsequence by itself.  
If the same character appeared earlier, appending it to the subsequences that were created *before* its last occurrence would duplicate subsequences that already exist. Subtracting the contribution from the last occurrence removes those duplicates.

**Approach**  
1. `tot` = total number of distinct non‑empty subsequences seen so far.  
2. `dp[26]` stores, for each letter, the number of subsequences that were created when that letter last appeared.  
3. For each character `c` in `s`:  
   * `new = tot + 1 - dp[c]` – all previous subsequences plus the single‑letter subsequence, minus duplicates caused by the last `c`.  
   * Update `tot = (tot + new) % MOD`.  
   * Update `dp[c] = (dp[c] + new) % MOD` to record the new subsequences that end with `c`.  
4. Return `tot`.

**Time Complexity**  
`O(n)` – one pass over the string, constant work per character.

**Space Complexity**  
`O(1)` – only 26 integers for `dp` and a few scalars, independent of input size.

**Key Insight**  
Subtracting the previous contribution of the same character (`dp[c]`) exactly cancels the subsequences that would otherwise be counted twice, ensuring each distinct subsequence is counted once.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 89.58%) |
| 💾 Memory | 19.3 MB (Beats 46.35%) |
| 📅 Solved | 2026-09-07 |
| 💻 Language | Python |