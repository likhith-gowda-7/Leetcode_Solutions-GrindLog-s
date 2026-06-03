# 717. 1-bit and 2-bit Characters


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/1-bit-and-2-bit-characters/)


## 📝 Problem Description

We have two special characters:

	- The first character can be represented by one bit `0`.

	- The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit character.

 

Example 1:**

```

**Input:** bits = [1,0,0]
**Output:** true
**Explanation:** The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

```

Example 2:**

```

**Input:** bits = [1,1,1,0]
**Output:** false
**Explanation:** The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

```

 

**Constraints:**

	- `1 <= bits.length <= 1000`

	- `bits[i]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the binary array and keeping track of whether the current character is a one-bit character or not. If a one-bit character is encountered, it sets a flag to indicate that the last character must be a one-bit character. If a two-bit character is encountered, it skips the next character and continues checking.

**Approach**
1. Initialize a flag `one_bit` to `True` to indicate that the last character is a one-bit character.
2. Iterate through the binary array starting from the second character (`i=1`).
3. If the current character is `1`, set `one_bit` to `False` and skip the next character by incrementing `i` by `2`.
4. If the current character is `0`, set `one_bit` to `True` and increment `i` by `1`.
5. After iterating through the entire array, return `True` if the last character is a one-bit character (`i==n or one_bit`).

**Time Complexity**
O(n), where n is the length of the binary array. This is because we only iterate through the array once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the flag `one_bit`.

**Key Insight**
The key insight is to recognize that a two-bit character must be followed by another two-bit character, while a one-bit character can be followed by either a one-bit or a two-bit character. By keeping track of this information, we can determine whether the last character is a one-bit character or not.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-11-18 |
| 💻 Language | Python |