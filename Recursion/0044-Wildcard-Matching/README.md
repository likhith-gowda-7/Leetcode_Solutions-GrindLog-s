> 📌 **Cross-listed:** Primary location is [String/0044-Wildcard-Matching](../../String/0044-Wildcard-Matching). This problem also appears under: **String**, **Dynamic Programming**, **Greedy**, **Recursion**

# 44. Wildcard Matching


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/wildcard-matching/)


## 📝 Problem Description

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'` where:

	- `'?'` Matches any single character.

	- `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).

 

Example 1:**

```

**Input:** s = "aa", p = "a"
**Output:** false
**Explanation:** "a" does not match the entire string "aa".

```

Example 2:**

```

**Input:** s = "aa", p = "*"
**Output:** true
**Explanation:** '*' matches any sequence.

```

Example 3:**

```

**Input:** s = "cb", p = "?a"
**Output:** false
**Explanation:** '?' matches 'c', but the second letter is 'a', which does not match 'b'.

```

 

**Constraints:**

	- `0 <= s.length, p.length <= 2000`

	- `s` contains only lowercase English letters.

	- `p` contains only lowercase English letters, `'?'` or `'*'`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a dynamic programming approach with a greedy strategy to match the input string `s` with the pattern `p`. It keeps track of the last matched character and the position of the last `*` in the pattern, which allows it to efficiently handle the `*` wildcard.

**Approach**
1. Initialize variables to keep track of the current positions in the string `s` and the pattern `p`, as well as the position of the last `*` and the number of matched characters.
2. Iterate through the string `s` and the pattern `p` simultaneously, checking for matches between characters or the `?` wildcard.
3. If a match is found, move to the next characters in both `s` and `p`.
4. If a `*` is encountered in `p`, update the position of the last `*` and the number of matched characters.
5. If a `*` is encountered after a non-match, move to the position of the last `*` and increment the number of matched characters.
6. If a non-match is found and there is no `*` in `p`, return False.
7. After iterating through the entire string `s`, check if there are any remaining `*`s in `p`. If there are, return False. Otherwise, return True.

**Time Complexity**
O(n*m), where n is the length of the string `s` and m is the length of the pattern `p`. This is because we are iterating through both `s` and `p` simultaneously.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the variables.

**Key Insight**
The key insight is to keep track of the position of the last `*` in the pattern, which allows us to efficiently handle the `*` wildcard and avoid unnecessary backtracking. This is made possible by the greedy strategy of moving to the position of the last `*` whenever a non-match is found.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 95.82%) |
| 💾 Memory | 19.4 MB (Beats 61.02%) |
| 📅 Solved | 2026-03-01 |
| 💻 Language | Python |