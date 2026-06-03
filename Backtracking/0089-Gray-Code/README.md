> 📌 **Cross-listed:** Primary location is [Math/0089-Gray-Code](../../Math/0089-Gray-Code). This problem also appears under: **Math**, **Backtracking**, **Bit Manipulation**

# 89. Gray Code


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/gray-code/)


## 📝 Problem Description

An **n-bit gray code sequence** is a sequence of `2^n` integers where:

	- Every integer is in the **inclusive** range `[0, 2^n - 1]`,

	- The first integer is `0`,

	- An integer appears **no more than once** in the sequence,

	- The binary representation of every pair of **adjacent** integers differs by **exactly one bit**, and

	- The binary representation of the **first** and **last** integers differs by **exactly one bit**.

Given an integer `n`, return *any valid **n-bit gray code sequence***.

 

Example 1:**

```

**Input:** n = 2
**Output:** [0,1,3,2]
**Explanation:**
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit

```

Example 2:**

```

**Input:** n = 1
**Output:** [0,1]

```

 

**Constraints:**

	- `1 <= n <= 16`

## 🧠 Solution Explanation

**Intuition**
The solution utilizes the property of gray code sequences, where each integer differs from its adjacent integer by exactly one bit. This can be achieved by performing a bitwise XOR operation between the integer and its right-shifted version, effectively flipping the bits from the rightmost position to the left.

**Approach**
1. Initialize an empty list `res` to store the gray code sequence.
2. Iterate over the range of integers from 0 to 2^n - 1.
3. For each integer `i`, perform a bitwise XOR operation between `i` and its right-shifted version `i >> 1`.
4. Append the result of the XOR operation to the `res` list.
5. Return the `res` list containing the gray code sequence.

**Time Complexity**
O(2^n) - The time complexity is linear with respect to the number of integers in the sequence, as we are iterating over the range of integers from 0 to 2^n - 1.

**Space Complexity**
O(2^n) - The space complexity is also linear with respect to the number of integers in the sequence, as we are storing the gray code sequence in the `res` list.

**Key Insight**
The key insight behind this solution is the property of gray code sequences, where each integer differs from its adjacent integer by exactly one bit. By performing a bitwise XOR operation between the integer and its right-shifted version, we can effectively flip the bits from the rightmost position to the left, resulting in a valid gray code sequence.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 5 ms (Beats 83.55%) |
| 💾 Memory | 21.1 MB (Beats 100%) |
| 📅 Solved | 2025-07-31 |
| 💻 Language | Python |