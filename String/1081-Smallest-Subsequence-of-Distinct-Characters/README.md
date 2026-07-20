# 1081. Smallest Subsequence of Distinct Characters


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)


## 📝 Problem Description

Given a string `s`, return *the **lexicographically smallest* *subsequence** of* `s` *that contains all the distinct characters of* `s` *exactly once*.

 

Example 1:**

```

**Input:** s = "bcabc"
**Output:** "abc"

```

Example 2:**

```

**Input:** s = "cbacdcbc"
**Output:** "acdb"

```

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase English letters.

 

**Note:** This question is the same as 316: [https://leetcode.com/problems/remove-duplicate-letters/](https://leetcode.com/problems/remove-duplicate-letters/)

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach with the help of a stack to find the lexicographically smallest subsequence of distinct characters. It iterates through the string, maintaining a count of each character and a set of seen characters. The key insight is to always choose the smallest character that has not been seen yet and is not smaller than the top of the stack.

**Approach**
1. Create a hash map `h1` to store the count of each character in the string.
2. Initialize an empty set `seen` to keep track of characters that have been seen.
3. Initialize an empty stack to store the characters of the subsequence.
4. Iterate through the string `s`. For each character `val`:
   1. Decrement the count of `val` in `h1`.
   2. If `val` has not been seen before:
      1. While the stack is not empty and the top of the stack is greater than `val` and the count of the top of the stack is greater than 0:
         1. Pop the top of the stack and remove it from the `seen` set.
      2. Push `val` onto the stack and add it to the `seen` set.
5. Return the subsequence as a string by joining the characters in the stack.

**Time Complexity**
O(n), where n is the length of the string. This is because we are iterating through the string once.

**Space Complexity**
O(n), where n is the length of the string. This is because in the worst case, we might need to store all characters in the stack and the `seen` set.

**Key Insight**
The key insight is to always choose the smallest character that has not been seen yet and is not smaller than the top of the stack. This ensures that the subsequence is lexicographically smallest and contains all distinct characters exactly once.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 12.05%) |
| 📅 Solved | 2026-07-19 |
| 💻 Language | Python |