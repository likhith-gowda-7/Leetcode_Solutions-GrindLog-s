# 2000. Reverse Prefix of Word


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-prefix-of-word/)


## 📝 Problem Description

Given a **0-indexed** string `word` and a character `ch`, **reverse** the segment of `word` that starts at index `0` and ends at the index of the **first occurrence** of `ch` (**inclusive**). If the character `ch` does not exist in `word`, do nothing.

	- For example, if `word = "abcdefd"` and `ch = "d"`, then you should **reverse** the segment that starts at `0` and ends at `3` (**inclusive**). The resulting string will be `"dcbaefd"`.

Return *the resulting string*.

 

Example 1:**

```

**Input:** word = "abcdefd", ch = "d"
**Output:** "dcbaefd"
**Explanation:** The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

```

Example 2:**

```

**Input:** word = "xyxzxe", ch = "z"
**Output:** "zxyxxe"
**Explanation:** The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

```

Example 3:**

```

**Input:** word = "abcd", ch = "z"
**Output:** "abcd"
**Explanation:** "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

```

 

**Constraints:**

	- `1 <= word.length <= 250`

	- `word` consists of lowercase English letters.

	- `ch` is a lowercase English letter.

## 🧠 Solution Explanation

**Intuition**
The solution uses a stack to store the characters before the first occurrence of the given character `ch`. Once the character `ch` is found, it reverses the stack and appends the remaining characters from the string to form the resulting string.

**Approach**
1. Check if the character `ch` exists in the string `word`. If not, return the original string.
2. Initialize an empty stack and an empty result string `res`.
3. Iterate through the string `word` using a while loop.
4. If the current character matches `ch`, reverse the stack and append `ch` followed by the reversed stack to `res`. Break the loop.
5. If the current character does not match `ch`, push it onto the stack.
6. After the loop, append the remaining characters from `word` (if any) to `res` and return the result.

**Time Complexity**
O(n), where n is the length of the string `word`. This is because we iterate through the string once.

**Space Complexity**
O(n), where n is the length of the string `word`. This is because in the worst case, we might need to store all characters from the string in the stack.

**Key Insight**
The key insight is to use a stack to efficiently reverse the segment of the string before the first occurrence of the given character `ch`. This approach allows us to avoid modifying the original string and instead build the resulting string incrementally.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-01-26 |
| 💻 Language | Python |