# 1888. Minimum Number of Flips to Make the Binary String Alternating


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/)


## 📝 Problem Description

You are given a binary string `s`. You are allowed to perform two types of operations on the string in any sequence:

	- **Type-1: Remove** the character at the start of the string `s` and **append** it to the end of the string.

	- **Type-2: Pick** any character in `s` and **flip** its value, i.e., if its value is `'0'` it becomes `'1'` and vice-versa.

Return *the **minimum** number of **type-2** operations you need to perform* *such that *`s` *becomes **alternating**.*

The string is called **alternating** if no two adjacent characters are equal.

	- For example, the strings `"010"` and `"1010"` are alternating, while the string `"0100"` is not.

 

Example 1:**

```

**Input:** s = "111000"
**Output:** 2
**Explanation**: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".

```

Example 2:**

```

**Input:** s = "010"
**Output:** 0
**Explanation**: The string is already alternating.

```

Example 3:**

```

**Input:** s = "1110"
**Output:** 1
**Explanation**: Use the second operation on the second element to make s = "1010".

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is either `'0'` or `'1'`.

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining two variables `flip1` and `flip2` to track the minimum number of flips required to make the string alternating from left to right and right to left respectively. It iterates through the string twice, first from left to right and then from right to left, and updates the minimum number of flips.

**Approach**
1. Initialize variables `flip1` and `flip2` to 0, and `ops` to a list of strings containing "0" and "1".
2. Iterate through the string from left to right, updating `flip1` and `flip2` based on whether the current character matches the expected character in the `ops` list.
3. After the first iteration, initialize `curr` to 1 and `Found` to False. If the length of the string is odd, set `curr` to 0 and `Found` to True.
4. Iterate through the string from right to left, updating `flip1` and `flip2` based on whether the current character matches the expected character in the `ops` list. If `Found` is True, toggle `curr` after each iteration.
5. Update the minimum number of flips `mini` with the minimum of `flip1` and `flip2` after each iteration.
6. Return the minimum number of flips `mini`.

**Time Complexity**
O(n), where n is the length of the string. This is because the solution iterates through the string twice, resulting in a linear time complexity.

**Space Complexity**
O(1), since the solution uses a constant amount of space to store the variables `flip1`, `flip2`, `ops`, `curr`, and `Found`.

**Key Insight**
The key insight is that we can make the string alternating by considering two cases: making the string alternating from left to right and from right to left. By iterating through the string twice and updating the minimum number of flips, we can find the minimum number of type-2 operations required to make the string alternating.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 231 ms (Beats 85.59%) |
| 💾 Memory | 19.9 MB (Beats 61.69%) |
| 📅 Solved | 2026-03-07 |
| 💻 Language | Python |