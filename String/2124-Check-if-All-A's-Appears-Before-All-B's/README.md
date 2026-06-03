# 2124. Check if All A's Appears Before All B's


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)


## 📝 Problem Description

Given a string `s` consisting of **only** the characters `'a'` and `'b'`, return `true` *if **every** *`'a'` *appears before **every** *`'b'`* in the string*. Otherwise, return `false`.

 

Example 1:**

```

**Input:** s = "aaabbb"
**Output:** true
**Explanation:**
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

```

Example 2:**

```

**Input:** s = "abab"
**Output:** false
**Explanation:**
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.

```

Example 3:**

```

**Input:** s = "bbb"
**Output:** true
**Explanation:**
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

```

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s[i]` is either `'a'` or `'b'`.

## 🧠 Solution Explanation

**Intuition**
This solution works by maintaining a counter for the number of 'b's encountered so far. If an 'a' is encountered after any 'b's have been seen, it immediately returns False, as this means 'b's have appeared before 'a's. If it iterates through the entire string without returning False, it returns True, indicating that all 'a's appear before all 'b's.

**Approach**
1. Initialize a counter `b` to 0, which will keep track of the number of 'b's encountered so far.
2. Iterate through each character `val` in the input string `s`.
3. If `val` is 'b', increment the counter `b`.
4. If `val` is 'a' and `b` is greater than 0, return False, as this means 'b's have appeared before 'a's.
5. If the iteration completes without returning False, return True.

**Time Complexity**
O(n), where n is the length of the input string `s`. This is because we make a single pass through the string, performing constant-time operations for each character.

**Space Complexity**
O(1), as we only use a constant amount of space to store the counter `b`, regardless of the size of the input string.

**Key Insight**
The key insight here is that we don't actually need to keep track of the indices of the 'a's and 'b's, but rather just the relative order in which they appear. By maintaining a counter for the number of 'b's seen so far, we can efficiently determine whether all 'a's appear before all 'b's.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 42.19%) |
| 📅 Solved | 2026-02-07 |
| 💻 Language | Python |