> 📌 **Cross-listed:** Primary location is [Array/1967-Number-of-Strings-That-Appear-as-Substrings-in-Word](../../Array/1967-Number-of-Strings-That-Appear-as-Substrings-in-Word). This problem also appears under: **Array**, **String**

# 1967. Number of Strings That Appear as Substrings in Word


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)


## 📝 Problem Description

Given an array of strings `patterns` and a string `word`, return *the **number** of strings in *`patterns`* that exist as a **substring** in *`word`.

A **substring** is a contiguous sequence of characters within a string.

 

Example 1:**

```

**Input:** patterns = ["a","abc","bc","d"], word = "abc"
**Output:** 3
**Explanation:**
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

```

Example 2:**

```

**Input:** patterns = ["a","b","c"], word = "aaaaabbbbb"
**Output:** 2
**Explanation:**
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.

```

Example 3:**

```

**Input:** patterns = ["a","a","a"], word = "ab"
**Output:** 3
**Explanation:** Each of the patterns appears as a substring in word "ab".

```

 

**Constraints:**

	- `1 <= patterns.length <= 100`

	- `1 <= patterns[i].length <= 100`

	- `1 <= word.length <= 100`

	- `patterns[i]` and `word` consist of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The problem requires counting the number of strings in the `patterns` array that exist as substrings within the `word` string. A key insight is that we can use a simple string search approach to achieve this efficiently.

**Approach**
1. Initialize a counter `res` to 0, which will store the total count of strings found in `word`.
2. Iterate through each string `val` in the `patterns` array.
3. For each `val`, check if it exists as a substring within `word` using the `in` operator.
4. If `val` is found as a substring, increment the `res` counter by 1.
5. After iterating through all strings in `patterns`, return the total count `res`.

**Time Complexity**
O(n * m), where n is the length of the `patterns` array and m is the length of the `word` string. This is because for each string in `patterns`, we perform a linear search within `word` using the `in` operator, which has a time complexity of O(m).

**Space Complexity**
O(1), as we only use a constant amount of space to store the counter `res` and do not allocate any additional space that scales with the input size.

**Key Insight**
The key insight is that the `in` operator in Python uses a linear search algorithm under the hood, which makes it suitable for this problem. This approach is efficient because it allows us to take advantage of the built-in string search functionality in Python, avoiding the need for more complex algorithms like KMP or Rabin-Karp.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 19.87%) |
| 📅 Solved | 2026-06-29 |
| 💻 Language | Python |