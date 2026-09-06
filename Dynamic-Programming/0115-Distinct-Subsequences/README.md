> 📌 **Cross-listed:** Primary location is [String/0115-Distinct-Subsequences](../../String/0115-Distinct-Subsequences). This problem also appears under: **String**, **Dynamic Programming**

# 115. Distinct Subsequences


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/distinct-subsequences/)


## 📝 Problem Description

Given two strings s and t, return *the number of distinct* ***subsequences**** of *s* which equals *t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:**

```

**Input:** s = "rabbbit", t = "rabbit"
**Output:** 3
**Explanation:**
As shown below, there are 3 ways you can generate "rabbit" from s.
`**rabb**b**it**`
`**ra**b**bbit**`
`**rab**b**bit**`

```

Example 2:**

```

**Input:** s = "babgbag", t = "bag"
**Output:** 5
**Explanation:**
As shown below, there are 5 ways you can generate "bag" from s.
`**ba**b**g**bag`
`**ba**bgba**g**`
`**b**abgb**ag**`
`ba**b**gb**ag**`
`babg**bag**`
```

 

**Constraints:**

	- `1 <= s.length, t.length <= 1000`

	- `s` and `t` consist of English letters.

## 🧠 Solution Explanation

**Intuition**
This solution uses a recursive approach with memoization to count the distinct subsequences of string `s` that equal string `t`. The key insight is to break down the problem into smaller subproblems and store the results to avoid redundant calculations.

**Approach**
1. Initialize a memoization dictionary `memo` to store the results of subproblems.
2. Define a recursive function `recursive` that takes two indices `ind_s` and `ind_t` as input.
3. If the subproblem is already solved (i.e., `(ind_s, ind_t)` is in `memo`), return the stored result.
4. If `ind_t` reaches the end of string `t`, return 1 (since we've found a valid subsequence).
5. If `ind_s` exceeds the length of string `s` or if the remaining characters in `s` are not enough to form the remaining characters in `t`, return 0.
6. If the current characters in `s` and `t` match, recursively call `recursive` with `ind_s+1` and `ind_t+1` and add the result to the count.
7. Recursively call `recursive` with `ind_s+1` and `ind_t` to consider the case where the current characters in `s` and `t` do not match.
8. Store the result in `memo` and return it.

**Time Complexity**
The time complexity is O(len(s) * len(t)), where len(s) and len(t) are the lengths of strings `s` and `t`, respectively. This is because each subproblem is solved at most twice (once for matching characters and once for non-matching characters), and there are a total of len(s) * len(t) subproblems.

**Space Complexity**
The space complexity is O(len(s) * len(t)), which is the maximum size of the memoization dictionary. This is because each subproblem is stored in the dictionary, and there are a total of len(s) * len(t) subproblems.

**Key Insight**
The key insight is to use memoization to avoid redundant calculations and store the results of subproblems. This allows us to break down the problem into smaller subproblems and solve them efficiently, resulting in a time complexity of O(len(s) * len(t)).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 712 ms (Beats 20.03%) |
| 💾 Memory | 234.1 MB (Beats 8.65%) |
| 📅 Solved | 2026-09-06 |
| 💻 Language | Python |