# 394. Decode String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/decode-string/)


## 📝 Problem Description

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed `10^5`.

 

Example 1:**

```

**Input:** s = "3[a]2[bc]"
**Output:** "aaabcbc"

```

Example 2:**

```

**Input:** s = "3[a2[c]]"
**Output:** "accaccacc"

```

Example 3:**

```

**Input:** s = "2[abc]3[cd]ef"
**Output:** "abcabccdcdcdef"

```

 

**Constraints:**

	- `1 <= s.length <= 30`

	- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.

	- `s` is guaranteed to be **a valid** input.

	- All the integers in `s` are in the range `[1, 300]`.

## 🧠 Solution Explanation

**Intuition**
This solution works by using a stack to keep track of the characters and the repeat numbers. When it encounters a ']', it pops characters from the stack until it finds the corresponding '[', and then it pops the repeat number from the stack and multiplies it with the popped characters.

**Approach**
1. Initialize an empty stack `st` and an empty result string `res`.
2. Iterate over each character `i` in the input string `s`.
3. If `i` is ']', pop characters from the stack until it finds the corresponding '['.
4. Pop the repeat number from the stack and multiply it with the popped characters to get the repeated string.
5. Push the repeated string onto the stack.
6. If `i` is not ']', push it onto the stack.
7. After iterating over the entire string, join the characters in the stack to get the final result.

**Time Complexity**
O(n), where n is the length of the input string. This is because we are iterating over the string once.

**Space Complexity**
O(n), where n is the length of the input string. This is because in the worst case, we need to store all characters in the stack.

**Key Insight**
The key insight here is to use a stack to keep track of the characters and the repeat numbers. By popping characters from the stack when we encounter a ']', we can correctly repeat the characters according to the given encoding rule.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-02-17 |
| 💻 Language | Python |