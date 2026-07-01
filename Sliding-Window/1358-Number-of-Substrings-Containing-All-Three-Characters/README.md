> 📌 **Cross-listed:** Primary location is [Hash Table/1358-Number-of-Substrings-Containing-All-Three-Characters](../../Hash-Table/1358-Number-of-Substrings-Containing-All-Three-Characters). This problem also appears under: **Hash Table**, **String**, **Sliding Window**

# 1358. Number of Substrings Containing All Three Characters


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)


## 📝 Problem Description

Given a string `s` consisting only of characters *a*, *b* and *c*.

Return the number of substrings containing **at least** one occurrence of all these characters *a*, *b* and *c*.

 

Example 1:**

```

**Input:** s = "abcabc"
**Output:** 10
**Explanation:** The substrings containing at least one occurrence of the characters *a*, *b* and *c are "*abc*", "*abca*", "*abcab*", "*abcabc*", "*bca*", "*bcab*", "*bcabc*", "*cab*", "*cabc*" *and* "*abc*" *(**again**)*. *

```

Example 2:**

```

**Input:** s = "aaacb"
**Output:** 3
**Explanation:** The substrings containing at least one occurrence of the characters *a*, *b* and *c are "*aaacb*", "*aacb*" *and* "*acb*".** *

```

Example 3:**

```

**Input:** s = "abc"
**Output:** 1

```

 

**Constraints:**

	- `3 <= s.length <= 5 x 10^4`

	- `s` only consists of *a*, *b* or *c *characters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with a hash table to efficiently count the number of substrings containing all three characters. By maintaining a window of characters that meet the condition, we can calculate the number of substrings that can be formed using the remaining characters outside the window.

**Approach**
1. Initialize variables to keep track of the window boundaries (`l` and `r`) and a hash table (`h`) to store the frequency of characters in the window.
2. Iterate over the string using the right pointer (`r`), incrementing the frequency of the current character in the hash table.
3. When the hash table contains three characters, calculate the number of substrings that can be formed using the remaining characters outside the window and add it to the result.
4. Move the left pointer (`l`) to the right, decrementing the frequency of the character at the left boundary and removing it from the hash table if its frequency becomes zero.
5. Repeat steps 2-4 until the right pointer reaches the end of the string.

**Time Complexity**
O(n), where n is the length of the string. This is because we iterate over the string once using the right pointer and move the left pointer at most n times.

**Space Complexity**
O(1), excluding the space needed for the output. The hash table stores at most three characters, which is a constant amount of space.

**Key Insight**
The key insight is that when the hash table contains three characters, we can calculate the number of substrings that can be formed using the remaining characters outside the window by multiplying the number of remaining characters by the number of substrings that can be formed using each character. This is because each character can be used to form a substring with the remaining characters, and we can choose any of the remaining characters to be the starting point of the substring.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 56 ms (Beats 94.06%) |
| 💾 Memory | 19.4 MB (Beats 48.32%) |
| 📅 Solved | 2026-06-30 |
| 💻 Language | Python |