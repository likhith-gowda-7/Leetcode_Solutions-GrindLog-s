> 📌 **Cross-listed:** Primary location is [Bit Manipulation/2749-Minimum-Operations-to-Make-the-Integer-Zero](../../Bit-Manipulation/2749-Minimum-Operations-to-Make-the-Integer-Zero). This problem also appears under: **Bit Manipulation**, **Brainteaser**, **Enumeration**

# 2749. Minimum Operations to Make the Integer Zero


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Brainteaser](https://img.shields.io/badge/Brainteaser-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/)


## 📝 Problem Description

You are given two integers `num1` and `num2`.

In one operation, you can choose integer `i` in the range `[0, 60]` and subtract `2^i + num2` from `num1`.

Return *the integer denoting the **minimum** number of operations needed to make* `num1` *equal to* `0`.

If it is impossible to make `num1` equal to `0`, return `-1`.

 

Example 1:**

```

**Input:** num1 = 3, num2 = -2
**Output:** 3
**Explanation:** We can make 3 equal to 0 with the following operations:
- We choose i = 2 and subtract 2^2 + (-2) from 3, 3 - (4 + (-2)) = 1.
- We choose i = 2 and subtract 2^2 + (-2) from 1, 1 - (4 + (-2)) = -1.
- We choose i = 0 and subtract 2^0 + (-2) from -1, (-1) - (1 + (-2)) = 0.
It can be proven, that 3 is the minimum number of operations that we need to perform.

```

Example 2:**

```

**Input:** num1 = 5, num2 = 7
**Output:** -1
**Explanation:** It can be proven, that it is impossible to make 5 equal to 0 with the given operation.

```

 

**Constraints:**

	- `1 <= num1 <= 10^9`

	- `-10^9 <= num2 <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by iteratively subtracting a power of 2 plus `num2` from `num1`, and checking if the remaining value can be made zero in the minimum number of operations. This approach is based on the fact that any number can be represented as a sum of powers of 2, and subtracting a power of 2 plus `num2` is equivalent to subtracting `num2` and adding a power of 2.

**Approach**
1. Initialize `k` to 1, which represents the minimum number of operations.
2. Calculate `x` as `num1 - (k * num2)`, which represents the remaining value after subtracting `k` powers of 2 plus `num2` from `num1`.
3. Check if `x` can be made zero in the minimum number of operations by checking if the number of bits set in `x` (i.e., `bin(x).count("1")`) is less than or equal to `k` and `k` is less than or equal to `x`. If this condition is true, return `k`.
4. If the condition is not true, increment `k` by 1 and repeat steps 2-3.
5. If `x` is still greater than or equal to 0 after the loop, return -1, indicating that it is impossible to make `num1` equal to 0.

**Time Complexity**
O(60), where 60 is the maximum possible value of `k`. This is because the loop runs at most 60 times, and each iteration takes constant time.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the variables `k` and `x`.

**Key Insight**
The key insight behind this solution is that any number can be represented as a sum of powers of 2, and subtracting a power of 2 plus `num2` is equivalent to subtracting `num2` and adding a power of 2. This allows us to iteratively subtract powers of 2 plus `num2` from `num1` and check if the remaining value can be made zero in the minimum number of operations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-09-05 |
| 💻 Language | Python |