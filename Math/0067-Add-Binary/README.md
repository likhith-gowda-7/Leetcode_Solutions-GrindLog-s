# 67. Add Binary


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/add-binary/)


## 📝 Problem Description

Given two binary strings `a` and `b`, return *their sum as a binary string*.

 

Example 1:**

```
**Input:** a = "11", b = "1"
**Output:** "100"

```
Example 2:**

```
**Input:** a = "1010", b = "1011"
**Output:** "10101"

```

 

**Constraints:**

	- `1 <= a.length, b.length <= 10^4`

	- `a` and `b` consist only of `'0'` or `'1'` characters.

	- Each string does not contain leading zeros except for the zero itself.

## 🧠 Solution Explanation

**Intuition**
The solution works by simulating the process of adding two binary numbers manually, digit by digit, while keeping track of any carry-over values. This approach leverages the fact that binary addition is similar to decimal addition, but with a simpler carry-over mechanism.

**Approach**
1. Initialize variables to store the carry-over value and the lengths of the input binary strings `a` and `b`.
2. Iterate through the input strings from right to left (i.e., from least significant bit to most significant bit).
3. For each iteration, calculate the total value of the current bits in `a` and `b`, plus any carry-over value.
4. Append the least significant bit of the total value to the result string.
5. Update the carry-over value to be the most significant bit of the total value.
6. Repeat steps 3-5 until all bits in both input strings have been processed.
7. If there is a remaining carry-over value after the iteration, append it to the result string.

**Time Complexity**
O(max(n1, n2)), where n1 and n2 are the lengths of the input binary strings `a` and `b`. This is because we iterate through the input strings once, and the number of iterations is proportional to the length of the longer string.

**Space Complexity**
O(max(n1, n2)), where n1 and n2 are the lengths of the input binary strings `a` and `b`. This is because we need to store the result string, which can be at most as long as the longer input string.

**Key Insight**
The key insight is that binary addition can be simulated by iterating through the input strings from right to left, calculating the total value of each pair of bits, and updating the carry-over value accordingly. This approach avoids the need for explicit loops or recursive function calls, making it efficient and easy to implement.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 16.76%) |
| 📅 Solved | 2026-02-15 |
| 💻 Language | Python |