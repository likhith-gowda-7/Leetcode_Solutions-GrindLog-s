> 📌 **Cross-listed:** Primary location is [Math/1071-Greatest-Common-Divisor-of-Strings](../../Math/1071-Greatest-Common-Divisor-of-Strings). This problem also appears under: **Math**, **String**

# 1071. Greatest Common Divisor of Strings


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/)


## 📝 Problem Description

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return *the largest string *`x`* such that *`x`* divides both *`str1`* and *`str2`.

 

Example 1:**

**Input:** str1 = "ABCABC", str2 = "ABC"

**Output:** "ABC"

Example 2:**

**Input:** str1 = "ABABAB", str2 = "ABAB"

**Output:** "AB"

Example 3:**

**Input:** str1 = "LEET", str2 = "CODE"

**Output:** ""

Example 4:**

**Input:** str1 = "AAAAAB", str2 = "AAA"

**Output:** ""​​​​​​​

 

**Constraints:**

	- `1 <= str1.length, str2.length <= 1000`

	- `str1` and `str2` consist of English uppercase letters.

## 🧠 Solution Explanation

**Intuition**
The solution leverages the mathematical property that the greatest common divisor (GCD) of two numbers is also the GCD of their sum and difference. In this context, the GCD of two strings is the largest string that divides both strings. The solution checks if the concatenation of the two strings is equal to the concatenation in reverse order, which implies that the strings are periodic and can be divided by a common substring.

**Approach**
1. Check if the concatenation of `str1` and `str2` is equal to the concatenation in reverse order (`str1+str2==str2+str1`). If true, it means `str1` and `str2` are periodic and can be divided by a common substring.
2. If the strings are periodic, calculate the GCD of their lengths using the `gcd` function from the math module.
3. Return the substring of `str1` with the length equal to the GCD, which is the largest string that divides both `str1` and `str2`.
4. If the strings are not periodic, return an empty string.

**Time Complexity**
O(1) - The time complexity is constant because the GCD calculation and string concatenation operations are performed only once.

**Space Complexity**
O(n) - The space complexity is linear because we need to store the concatenated strings, where n is the maximum length of the input strings.

**Key Insight**
The key insight is that if the concatenation of two strings is equal to the concatenation in reverse order, it implies that the strings are periodic and can be divided by a common substring. This property allows us to calculate the GCD of the string lengths and find the largest string that divides both strings.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.4 MB (Beats 100%) |
| 📅 Solved | 2024-12-05 |
| 💻 Language | Python |