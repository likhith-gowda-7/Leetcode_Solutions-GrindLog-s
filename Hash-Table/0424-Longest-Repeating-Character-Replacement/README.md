# 424. Longest Repeating Character Replacement


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)


## 📝 Problem Description

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return *the length of the longest substring containing the same letter you can get after performing the above operations*.

 

Example 1:**

```

**Input:** s = "ABAB", k = 2
**Output:** 4
**Explanation:** Replace the two 'A's with two 'B's or vice versa.

```

Example 2:**

```

**Input:** s = "AABABBA", k = 1
**Output:** 4
**Explanation:** Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of only uppercase English letters.

	- `0 <= k <= s.length`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to find the longest substring with the same letter that can be obtained by replacing at most `k` characters. The key insight is to maintain a frequency count of characters within the window and adjust the window size based on the maximum frequency.

**Approach**
1. Initialize two pointers `l` and `r` to the start of the string, and variables `res` to store the maximum length, `check` as a dictionary to store character frequencies, and `max_freq` to store the maximum frequency.
2. Iterate through the string using the `r` pointer, updating the frequency count of the current character in `check` and the maximum frequency `max_freq`.
3. If the window size (`r - l + 1`) minus the maximum frequency `max_freq` exceeds `k`, it means we need to replace more than `k` characters to maintain the same letter in the window. In this case, move the `l` pointer to the right, decrementing the frequency count of the character at `l` in `check`.
4. Update the maximum length `res` if the current window size (`r - l + 1`) is greater than `res`.
5. Return the maximum length `res` after iterating through the entire string.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we are iterating through the string once using the `r` pointer.

**Space Complexity**
O(min(n, m)), where m is the size of the character set (26 for uppercase English letters). This is because we are storing the frequency count of characters in the `check` dictionary, which can have at most `m` keys.

**Key Insight**
The key to this solution is to maintain a balance between the window size and the maximum frequency of characters within the window. By adjusting the window size based on the maximum frequency, we can efficiently find the longest substring with the same letter that can be obtained by replacing at most `k` characters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 87 ms (Beats 50.99%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-04-02 |
| 💻 Language | Python |