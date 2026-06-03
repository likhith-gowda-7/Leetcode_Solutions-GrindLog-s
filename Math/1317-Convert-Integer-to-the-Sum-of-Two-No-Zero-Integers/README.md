# 1317. Convert Integer to the Sum of Two No-Zero Integers


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)


## 📝 Problem Description

**No-Zero integer** is a positive integer that **does not contain any `0`** in its decimal representation.

Given an integer `n`, return *a list of two integers* `[a, b]` *where*:

	- `a` and `b` are **No-Zero integers**.

	- `a + b = n`

The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

Example 1:**

```

**Input:** n = 2
**Output:** [1,1]
**Explanation:** Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.

```

Example 2:**

```

**Input:** n = 11
**Output:** [2,9]
**Explanation:** Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.

```

 

**Constraints:**

	- `2 <= n <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through all possible pairs of numbers that sum up to `n`. It checks each pair to ensure that neither number contains any zeros in its decimal representation. The first pair that meets this condition is returned as the result.

**Approach**
1. Define a helper function `zero_check(num)` that checks if a given number `num` contains any zeros in its decimal representation.
2. Iterate through all numbers from 1 to `n-1` (inclusive) to find the first pair of numbers that sum up to `n`.
3. For each number `num1` in the iteration, calculate `num2` as `n - num1`.
4. Check if both `num1` and `num2` do not contain any zeros using the `zero_check(num)` function.
5. If both numbers pass the zero check, return the pair `[num1, num2]`.

**Time Complexity**
O(n) - The solution iterates through all numbers from 1 to `n-1`, resulting in a linear time complexity.

**Space Complexity**
O(1) - The solution uses a constant amount of space to store the helper function and variables, resulting in a constant space complexity.

**Key Insight**
The key insight is to use a helper function to check for zeros, which simplifies the main logic and makes the solution more efficient. By iterating through all possible pairs and checking for zeros, the solution ensures that it finds the first pair that meets the condition, making it a straightforward and effective solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-09-08 |
| 💻 Language | Python |