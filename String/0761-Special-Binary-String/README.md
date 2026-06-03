# 761. Special Binary String


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/special-binary-string/)


## 📝 Problem Description

**Special binary strings** are binary strings with the following two properties:

	- The number of `0`'s is equal to the number of `1`'s.

	- Every prefix of the binary string has at least as many `1`'s as `0`'s.

You are given a **special binary** string `s`.

A move consists of choosing two consecutive, non-empty, special substrings of `s`, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

Return *the lexicographically largest resulting string possible after applying the mentioned operations on the string*.

 

Example 1:**

```

**Input:** s = "11011000"
**Output:** "11100100"
**Explanation:** The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

```

Example 2:**

```

**Input:** s = "10"
**Output:** "10"

```

 

**Constraints:**

	- `1 <= s.length <= 50`

	- `s[i]` is either `'0'` or `'1'`.

	- `s` is a special binary string.

## 🧠 Solution Explanation

**Intuition**
The solution works by recursively finding all special substrings within the input string, sorting them lexicographically in descending order, and then concatenating them to form the lexicographically largest resulting string. The key insight is that the lexicographically largest string can be obtained by sorting the special substrings and then concatenating them.

**Approach**
1. Initialize an empty list `ans` to store the special substrings.
2. Initialize a counter `cnt` to keep track of the difference between the number of `1`s and `0`s in the current substring.
3. Initialize two pointers `i` and `j` to the start of the string.
4. Iterate through the string using pointer `i`. If the current character is `1`, increment `cnt`, otherwise decrement `cnt`.
5. When `cnt` becomes `0`, it means we have found a special substring. Append this substring to `ans` by recursively calling `makeLargestSpecial` on the substring between `j + 1` and `i`, and then append `'1'` and `'0'` to the result.
6. Reset `j` to `i + 1` to start searching for the next special substring.
7. After iterating through the entire string, sort `ans` in descending order and join the substrings to form the final result.

**Time Complexity**
O(n log n), where n is the length of the input string. This is because we need to sort the special substrings, which takes O(n log n) time.

**Space Complexity**
O(n), where n is the length of the input string. This is because we need to store the special substrings in the `ans` list, which can have up to n substrings.

**Key Insight**
The key insight is that the lexicographically largest string can be obtained by sorting the special substrings and then concatenating them. This is because the special substrings are already lexicographically largest within themselves, and sorting them allows us to concatenate them in the correct order to form the final result.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 20.57%) |
| 📅 Solved | 2026-02-28 |
| 💻 Language | Python |