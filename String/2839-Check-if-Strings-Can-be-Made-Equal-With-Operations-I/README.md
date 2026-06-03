# 2839. Check if Strings Can be Made Equal With Operations I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/)


## 📝 Problem Description

You are given two strings `s1` and `s2`, both of length `4`, consisting of **lowercase** English letters.

You can apply the following operation on any of the two strings **any** number of times:

	- Choose any two indices `i` and `j` such that `j - i = 2`, then **swap** the two characters at those indices in the string.

Return `true`* if you can make the strings *`s1`* and *`s2`* equal, and *`false`* otherwise*.

 

Example 1:**

```

**Input:** s1 = "abcd", s2 = "cdab"
**Output:** true
**Explanation:** We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.

```

Example 2:**

```

**Input:** s1 = "abcd", s2 = "dacb"
**Output:** false
**Explanation:** It is not possible to make the two strings equal.

```

 

**Constraints:**

	- `s1.length == s2.length == 4`

	- `s1` and `s2` consist only of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution exploits the fact that the strings can be transformed into each other by swapping characters at indices that are 2 positions apart. This means that the first and third characters, as well as the second and fourth characters, must be equal in both strings.

**Approach**
1. Initialize a result array `res` with two elements, both set to 0.
2. Check if the first and third characters of `s1` and `s2` are equal, either directly or after swapping. If so, set `res[0] = 1`.
3. Check if the second and fourth characters of `s1` and `s2` are equal, either directly or after swapping. If so, set `res[1] = 1`.
4. Return `True` if the sum of `res` is 2, indicating that both pairs of characters are equal, and `False` otherwise.

**Time Complexity**
O(1) - The solution only involves a constant number of comparisons and assignments, regardless of the input size.

**Space Complexity**
O(1) - The solution uses a constant amount of space to store the `res` array.

**Key Insight**
The key insight is that the strings can only be transformed into each other by swapping characters at indices that are 2 positions apart. This means that the first and third characters, as well as the second and fourth characters, must be equal in both strings. The solution exploits this insight to check if the strings can be made equal.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 61.99%) |
| 📅 Solved | 2026-03-29 |
| 💻 Language | Python |