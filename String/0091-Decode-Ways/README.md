# 91. Decode Ways


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/decode-ways/)


## 📝 Problem Description

You have intercepted a secret message encoded as a string of numbers. The message is **decoded** via the following mapping:

`"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'`

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

	- `"AAJF"` with the grouping `(1, 1, 10, 6)`

	- `"KJF"` with the grouping `(11, 10, 6)`

	- The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the **number of ways** to **decode** it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a **32-bit** integer.

 

Example 1:**

**Input:** s = "12"

**Output:** 2

**Explanation:**

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:**

**Input:** s = "226"

**Output:** 3

**Explanation:**

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:**

**Input:** s = "06"

**Output:** 0

**Explanation:**

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` contains only digits and may contain leading zero(s).

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming to count the number of ways to decode a string of digits. The idea is to break down the problem into smaller subproblems and store the results in a table to avoid redundant computation.

**Approach**
1. Initialize a dynamic programming table `dp` of size `n+1`, where `n` is the length of the input string `s`. The extra cell `dp[n]` is used to indicate that the last digit is a valid code.
2. Iterate from the end of the string to the beginning. For each cell `dp[i]`, check if the current digit `s[i]` is not zero. If it's not zero, there are two options:
   1. Take the current digit as a single number, which adds `dp[i+1]` to the count.
   2. Take the current two digits as a number, if it's less than or equal to 26, which adds `dp[i+2]` to the count.
3. Return the value of `dp[0]`, which represents the total number of ways to decode the entire string.

**Time Complexity**
O(n), where n is the length of the input string. This is because we only iterate through the string once, and each operation takes constant time.

**Space Complexity**
O(n), where n is the length of the input string. This is because we need to store the dynamic programming table of size n+1.

**Key Insight**
The key insight is to recognize that the problem can be broken down into smaller subproblems, and the solution can be constructed by combining the results of these subproblems. The dynamic programming table `dp` stores the number of ways to decode the substring ending at each position, which allows us to avoid redundant computation and solve the problem efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-10-31 |
| 💻 Language | Python |