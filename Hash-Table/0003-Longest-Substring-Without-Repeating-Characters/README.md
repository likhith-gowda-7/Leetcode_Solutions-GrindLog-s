# 3. Longest Substring Without Repeating Characters


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)


## 📝 Problem Description

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

 

Example 1:**

```

**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

```

Example 2:**

```

**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.

```

Example 3:**

```

**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

**Constraints:**

	- `0 <= s.length <= 5 * 10^4`

	- `s` consists of English letters, digits, symbols and spaces.

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with a set to keep track of unique characters in the current substring. By expanding the window to the right and shrinking it from the left when a duplicate is found, we can efficiently find the longest substring without repeating characters.

**Approach**
1. Initialize an empty set `check` to store unique characters in the current substring, and two pointers `l` and `r` to represent the left and right boundaries of the window.
2. Iterate through the string `s` with the right pointer `r`.
3. When a duplicate character is found in the set `check`, remove characters from the left of the window by incrementing `l` and removing the corresponding character from the set until the duplicate is removed.
4. Add the current character at the right pointer `r` to the set `check`.
5. Update the maximum length `maxi` if the current window size (`r - l + 1`) is larger.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because each character is visited at most twice: once when it's added to the set, and once when it's removed.

**Space Complexity**
O(min(n, m)), where m is the size of the character set. In the worst case, the set `check` stores all unique characters in the string `s`.

**Key Insight**
The key insight is to use a set to efficiently check for duplicates and to shrink the window from the left when a duplicate is found, allowing us to find the longest substring without repeating characters in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 91.86%) |
| 💾 Memory | 13.1 MB (Beats 44.4%) |
| 📅 Solved | 2025-03-09 |
| 💻 Language | Python |