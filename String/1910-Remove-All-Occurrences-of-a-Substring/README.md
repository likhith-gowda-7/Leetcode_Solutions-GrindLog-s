# 1910. Remove All Occurrences of a Substring


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/)


## 📝 Problem Description

Given two strings `s` and `part`, perform the following operation on `s` until **all** occurrences of the substring `part` are removed:

	- Find the **leftmost** occurrence of the substring `part` and **remove** it from `s`.

Return `s`* after removing all occurrences of *`part`.

A **substring** is a contiguous sequence of characters in a string.

 

Example 1:**

```

**Input:** s = "daabcbaabcbc", part = "abc"
**Output:** "dab"
**Explanation**: The following operations are done:
- s = "da**abc**baabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "daba**abc**bc", remove "abc" starting at index 4, so s = "dababc".
- s = "dab**abc**", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".

```

Example 2:**

```

**Input:** s = "axxxxyyyyb", part = "xy"
**Output:** "ab"
**Explanation**: The following operations are done:
- s = "axxx**xy**yyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axx**xy**yyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "ax**xy**yb", remove "xy" starting at index 2 so s = "axyb".
- s = "a**xy**b", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".

```

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `1 <= part.length <= 1000`

	- `s`​​​​​​ and `part` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to simulate the removal of the substring `part` from the string `s`. It continuously appends characters from `s` to the stack and checks if the last `len(part)` characters match `part`. If they do, it removes these characters from the stack.

**Approach**
1. Initialize an empty stack to store characters from `s`.
2. Iterate over each character `s[i]` in `s`.
3. Append `s[i]` to the stack.
4. If the stack has at least `len(part)` characters, check if the last `len(part)` characters match `part`.
5. If they match, remove the last `len(part)` characters from the stack.
6. After iterating over all characters in `s`, return the remaining characters in the stack as a string.

**Time Complexity**
O(n * m), where n is the length of `s` and m is the length of `part`. This is because in the worst case, we might need to iterate over all characters in `s` and check all possible substrings of length `m`.

**Space Complexity**
O(n), where n is the length of `s`. This is because in the worst case, we might need to store all characters from `s` in the stack.

**Key Insight**
The key insight is to use a stack to simulate the removal of the substring `part` from the string `s`. By continuously checking if the last `len(part)` characters match `part`, we can efficiently remove all occurrences of `part` from `s`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 20.76%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-11 |
| 💻 Language | Python |