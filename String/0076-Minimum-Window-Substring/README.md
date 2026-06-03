> 📌 **Cross-listed:** Primary location is [Hash Table/0076-Minimum-Window-Substring](../../Hash-Table/0076-Minimum-Window-Substring). This problem also appears under: **Hash Table**, **String**, **Sliding Window**

# 76. Minimum Window Substring


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-window-substring/)


## 📝 Problem Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window*** ***substring**** of *`s`* such that every character in *`t`* (**including duplicates**) is included in the window*. If there is no such substring, return *the empty string *`""`.

The testcases will be generated such that the answer is **unique**.

 

Example 1:**

```

**Input:** s = "ADOBECODEBANC", t = "ABC"
**Output:** "BANC"
**Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

```

Example 2:**

```

**Input:** s = "a", t = "a"
**Output:** "a"
**Explanation:** The entire string s is the minimum window.

```

Example 3:**

```

**Input:** s = "a", t = "aa"
**Output:** ""
**Explanation:** Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

```

 

**Constraints:**

	- `m == s.length`

	- `n == t.length`

	- `1 <= m, n <= 10^5`

	- `s` and `t` consist of uppercase and lowercase English letters.

 

**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to find the minimum window substring in string `s` that contains all characters from string `t`. The key insight is to maintain two frequency counters, `h1` and `h2`, to track the characters in `t` and the current window in `s`, respectively. By expanding the window to the right and contracting it from the left, we can efficiently find the minimum window.

**Approach**
1. Initialize two frequency counters, `h1` and `h2`, to store the characters in `t` and the current window in `s`, respectively.
2. Expand the window to the right by incrementing the frequency of the current character in `h2`. If the frequency of the current character in `h2` matches the frequency in `h1`, increment the `have` counter.
3. When the window contains all characters from `t` (i.e., `have == needed`), contract the window from the left by decrementing the frequency of the leftmost character in `h2`. If the frequency of the leftmost character in `h2` is less than the frequency in `h1`, decrement the `have` counter.
4. Update the minimum window length and the corresponding start and end indices if the current window is smaller than the previous minimum window.
5. Repeat steps 2-4 until the window contains all characters from `t` or the end of the string `s` is reached.

**Time Complexity**
O(m + n), where m and n are the lengths of strings `s` and `t`, respectively. The time complexity is linear because we only iterate through the strings `s` and `t` once.

**Space Complexity**
O(n), where n is the length of string `t`. We need to store the frequency of each character in `t` in the `h1` counter.

**Key Insight**
The key insight is to use two frequency counters, `h1` and `h2`, to efficiently track the characters in `t` and the current window in `s`. By expanding and contracting the window, we can find the minimum window substring in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 75 ms (Beats 49.73%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-03-21 |
| 💻 Language | Python |