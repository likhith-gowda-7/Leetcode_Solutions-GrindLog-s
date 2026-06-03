# 844. Backspace String Compare


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/backspace-string-compare/)


## 📝 Problem Description

Given two strings `s` and `t`, return `true` *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:**

```

**Input:** s = "ab#c", t = "ad#c"
**Output:** true
**Explanation:** Both s and t become "ac".

```

Example 2:**

```

**Input:** s = "ab##", t = "c#d#"
**Output:** true
**Explanation:** Both s and t become "".

```

Example 3:**

```

**Input:** s = "a#c", t = "b"
**Output:** false
**Explanation:** s becomes "c" while t becomes "b".

```

 

**Constraints:**

	- `1 <= s.length, t.length <= 200`

	- `s` and `t` only contain lowercase letters and `'#'` characters.

 

**Follow up:** Can you solve it in `O(n)` time and `O(1)` space?

## 🧠 Solution Explanation

**Intuition**
The solution uses a simple iterative approach to simulate the backspace operation on both input strings. It maintains a "skip" counter to track the number of backspaces encountered, effectively "undoing" the last character when a backspace is encountered.

**Approach**
1. Define a helper function `comp(s)` that takes a string `s` as input and returns the resulting string after applying backspace operations.
2. Initialize an empty string `res` to store the result and a "skip" counter `skip` to 0.
3. Iterate through each character `i` in the input string `s`.
4. If `i` is a backspace (`'#'`), decrement the "skip" counter. If `res` is not empty, remove the last character from `res` (i.e., "undo" the last character).
5. If `i` is not a backspace, append it to the result string `res`.
6. After processing the entire input string, return the resulting string `res`.
7. In the main function, call `comp(s)` and `comp(t)` to get the resulting strings for both input strings and compare them for equality.

**Time Complexity**
O(n + m), where n and m are the lengths of the input strings `s` and `t`, respectively. This is because we iterate through each character in both strings once.

**Space Complexity**
O(n + m), where n and m are the lengths of the input strings `s` and `t`, respectively. This is because we store the resulting strings in memory.

**Key Insight**
The key insight is to use a "skip" counter to efficiently "undo" characters when backspaces are encountered, avoiding the need to store the entire history of characters. This approach allows us to solve the problem in O(n + m) time and O(n + m) space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-01-28 |
| 💻 Language | Python |