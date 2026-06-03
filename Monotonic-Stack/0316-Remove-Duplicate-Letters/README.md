> 📌 **Cross-listed:** Primary location is [String/0316-Remove-Duplicate-Letters](../../String/0316-Remove-Duplicate-Letters). This problem also appears under: **String**, **Stack**, **Greedy**, **Monotonic Stack**

# 316. Remove Duplicate Letters


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/remove-duplicate-letters/)


## 📝 Problem Description

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is **the smallest in lexicographical order** among all possible results.

 

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

	- `1 <= s.length <= 10^4`

	- `s` consists of lowercase English letters.

 

**Note:** This question is the same as 1081: [https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach with a stack to remove duplicate letters from the string. The key insight is to always choose the smallest letter that has not been seen before and can be appended to the stack without violating the condition of the smallest lexicographical order.

**Approach**
1. Create a frequency counter `occur` to store the count of each character in the string.
2. Initialize an empty stack `stack` and a set `seen` to keep track of the characters that have been seen.
3. Iterate through the string `s` from left to right.
4. For each character `s[i]`, decrement its count in the frequency counter `occur`.
5. If `s[i]` has not been seen before, pop characters from the stack that are larger than `s[i]` and have a count greater than 0, until the stack is empty or the top of the stack is smaller than or equal to `s[i]`.
6. Append `s[i]` to the stack and add it to the `seen` set.
7. Repeat steps 4-6 until the end of the string.
8. Return the string formed by the characters in the stack.

**Time Complexity**
O(n), where n is the length of the string, because each character is processed at most twice: once when it is encountered for the first time, and once when it is popped from the stack.

**Space Complexity**
O(n), where n is the length of the string, because in the worst case, all characters are stored in the stack.

**Key Insight**
The key insight is to use a stack to keep track of the characters that have been seen, and to always choose the smallest letter that has not been seen before and can be appended to the stack without violating the condition of the smallest lexicographical order. This ensures that the resulting string is the smallest in lexicographical order among all possible results.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 68.37%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-01 |
| 💻 Language | Python |