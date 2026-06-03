# 1957. Delete Characters to Make Fancy String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/delete-characters-to-make-fancy-string/)


## 📝 Problem Description

A **fancy string** is a string where no **three** **consecutive** characters are equal.

Given a string `s`, delete the **minimum** possible number of characters from `s` to make it **fancy**.

Return *the final string after the deletion*. It can be shown that the answer will always be **unique**.

 

Example 1:**

```

**Input:** s = "leeetcode"
**Output:** "leetcode"
**Explanation:**
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

```

Example 2:**

```

**Input:** s = "aaabaaaa"
**Output:** "aabaa"
**Explanation:**
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

```

Example 3:**

```

**Input:** s = "aab"
**Output:** "aab"
**Explanation:** No three consecutive characters are equal, so return "aab".

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists only of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the input string and keeping track of the current character and its consecutive count. If the current character is different from the previous one, it resets the count and adds the character to the result string. If the count is less than 3, it adds the character to the result string regardless of whether it's the same as the previous one.

**Approach**
1. Initialize variables `c` (consecutive count) to 1, `prev` (previous character) to the first character of the string, and `res` (result string) to the first character of the string.
2. Iterate through the string starting from the second character.
3. If the current character is different from the previous one, reset `c` to 1 and update `prev` to the current character.
4. If the current character is the same as the previous one, increment `c`.
5. If `c` is less than 3, add the current character to `res`.
6. After iterating through the entire string, return `res`.

**Time Complexity**
O(n), where n is the length of the input string. This is because we're iterating through the string once.

**Space Complexity**
O(n), where n is the length of the input string. This is because in the worst case, we might need to store the entire string in `res`.

**Key Insight**
The key insight is that we only need to keep track of the previous character and its consecutive count to determine whether to add the current character to the result string. This allows us to solve the problem efficiently with a single pass through the string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 199 ms (Beats 86.22%) |
| 💾 Memory | 19 MB (Beats 100%) |
| 📅 Solved | 2025-07-21 |
| 💻 Language | Python |