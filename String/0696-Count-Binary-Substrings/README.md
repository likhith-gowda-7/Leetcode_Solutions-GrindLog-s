> 📌 **Cross-listed:** Primary location is [Two Pointers/0696-Count-Binary-Substrings](../../Two-Pointers/0696-Count-Binary-Substrings). This problem also appears under: **Two Pointers**, **String**

# 696. Count Binary Substrings


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-binary-substrings/)


## 📝 Problem Description

Given a binary string `s`, return the number of non-empty substrings that have the same number of `0`'s and `1`'s, and all the `0`'s and all the `1`'s in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:**

```

**Input:** s = "00110011"
**Output:** 6
**Explanation:** There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

```

Example 2:**

```

**Input:** s = "10101"
**Output:** 4
**Explanation:** There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is either `'0'` or `'1'`.

## 🧠 Solution Explanation

**Intuition**
The problem requires counting the number of non-empty substrings with equal consecutive 0's and 1's in a binary string. The key insight is to use a two-pointer approach, where we track the length of consecutive 0's and 1's. When we encounter a transition from one character to another, we add the minimum of the current and previous group lengths to the result.

**Approach**
1. Initialize variables `curr` (current group length) and `prev` (previous group length) to 1 and 0, respectively.
2. Initialize the result `res` to 0.
3. Iterate through the string `s` starting from the second character (index 1).
4. If the current character is different from the previous one, it means we've encountered a transition.
   - Add the minimum of `curr` and `prev` to the result `res`.
   - Update `prev` to `curr` and reset `curr` to 1.
5. If the current character is the same as the previous one, increment `curr`.
6. After the loop, add the minimum of `curr` and `prev` to the result `res` one last time.
7. Return the result `res`.

**Time Complexity**
O(n), where n is the length of the string `s`. We make a single pass through the string, and each operation takes constant time.

**Space Complexity**
O(1), as we only use a constant amount of space to store the variables `curr`, `prev`, and `res`.

**Key Insight**
The key to this solution is recognizing that when we encounter a transition from one character to another, we can add the minimum of the current and previous group lengths to the result. This is because the new group will start with a single character, and the previous group will be split into two smaller groups. By taking the minimum, we ensure that we count each group correctly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 51 ms (Beats 85.8%) |
| 💾 Memory | 19.7 MB (Beats 36.2%) |
| 📅 Solved | 2026-02-20 |
| 💻 Language | Python |