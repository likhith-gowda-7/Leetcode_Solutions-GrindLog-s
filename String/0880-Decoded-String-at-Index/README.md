# 880. Decoded String at Index


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/decoded-string-at-index/)


## 📝 Problem Description

You are given an encoded string `s`. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

	- If the character read is a letter, that letter is written onto the tape.

	- If the character read is a digit `d`, the entire current tape is repeatedly written `d - 1` more times in total.

Given an integer `k`, return *the *`k^th`* letter (**1-indexed)** in the decoded string*.

 

Example 1:**

```

**Input:** s = "leet2code3", k = 10
**Output:** "o"
**Explanation:** The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10^th letter in the string is "o".

```

Example 2:**

```

**Input:** s = "ha22", k = 5
**Output:** "h"
**Explanation:** The decoded string is "hahahaha".
The 5^th letter is "h".

```

Example 3:**

```

**Input:** s = "a2345678999999999999999", k = 1
**Output:** "a"
**Explanation:** The decoded string is "a" repeated 8301530446056247680 times.
The 1^st letter is "a".

```

 

**Constraints:**

	- `2 <= s.length <= 100`

	- `s` consists of lowercase English letters and digits `2` through `9`.

	- `s` starts with a letter.

	- `1 <= k <= 10^9`

	- It is guaranteed that `k` is less than or equal to the length of the decoded string.

	- The decoded string is guaranteed to have less than `2^63` letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pass approach to calculate the total length of the decoded string and then find the kth letter. The first pass calculates the total length by processing the string from left to right, and the second pass finds the kth letter by processing the string from right to left.

**Approach**
1. Initialize a variable `total` to 0 to store the total length of the decoded string.
2. Iterate through the input string `s` from left to right. If the current character is a digit, multiply the `total` by the digit value. If the current character is a letter, increment the `total` by 1.
3. After the first pass, `total` stores the total length of the decoded string.
4. Iterate through the input string `s` from right to left. For each character, calculate the new `total` by dividing the previous `total` by the digit value if the character is a digit, or decrementing the `total` by 1 if the character is a letter.
5. If the current character is a letter and `k` is 0, return the letter as the kth letter. Otherwise, update `k` by taking the modulus of `k` with the new `total`.

**Time Complexity**
O(n), where n is the length of the input string `s`. The first pass iterates through the string once, and the second pass also iterates through the string once.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the `total` variable and the input string `s`.

**Key Insight**
The key insight is to use the modulo operation to efficiently find the kth letter by reducing the `total` length after each iteration. This approach avoids the need to store the entire decoded string, making it space-efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-02-20 |
| 💻 Language | Python |