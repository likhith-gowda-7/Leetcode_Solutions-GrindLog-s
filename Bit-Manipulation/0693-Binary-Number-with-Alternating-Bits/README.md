# 693. Binary Number with Alternating Bits


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-number-with-alternating-bits/)


## 📝 Problem Description

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:**

```

**Input:** n = 5
**Output:** true
**Explanation:** The binary representation of 5 is: 101

```

Example 2:**

```

**Input:** n = 7
**Output:** false
**Explanation:** The binary representation of 7 is: 111.
```

Example 3:**

```

**Input:** n = 11
**Output:** false
**Explanation:** The binary representation of 11 is: 1011.
```

 

**Constraints:**

	- `1 <= n <= 2^31 - 1`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to determine if a given positive integer has alternating bits, meaning that two adjacent bits will always have different values. We can achieve this by converting the integer to its binary representation and checking for alternating bits.

**Approach**
1. Convert the input integer `n` to its binary representation using the `bin()` function and remove the '0b' prefix.
2. Initialize a loop starting from the second bit (index 1) to the end of the binary string.
3. Inside the loop, check if the current bit is the same as the previous bit. If they are the same, return `False`.
4. If the loop completes without finding any identical adjacent bits, return `True`.

**Time Complexity**
O(log n), where n is the input integer. This is because we are converting the integer to its binary representation, which has a length of log n (base 2). We then iterate over this binary string, which takes O(log n) time.

**Space Complexity**
O(log n), where n is the input integer. This is because we are storing the binary representation of the integer, which has a length of log n (base 2).

**Key Insight**
The key insight here is that we can solve this problem by simply iterating over the binary representation of the integer and checking for alternating bits. This approach is efficient because it avoids unnecessary calculations and directly checks for the required condition.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 9.61%) |
| 📅 Solved | 2026-02-18 |
| 💻 Language | Python |