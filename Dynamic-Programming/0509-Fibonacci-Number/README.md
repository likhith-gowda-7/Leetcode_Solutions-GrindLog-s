> 📌 **Cross-listed:** Primary location is [Math/0509-Fibonacci-Number](../../Math/0509-Fibonacci-Number). This problem also appears under: **Math**, **Dynamic Programming**, **Recursion**, **Memoization**

# 509. Fibonacci Number


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple) ![Memoization](https://img.shields.io/badge/Memoization-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/fibonacci-number/)


## 📝 Problem Description

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

```

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

```

Given `n`, calculate `F(n)`.

 

Example 1:**

```

**Input:** n = 2
**Output:** 1
**Explanation:** F(2) = F(1) + F(0) = 1 + 0 = 1.

```

Example 2:**

```

**Input:** n = 3
**Output:** 2
**Explanation:** F(3) = F(2) + F(1) = 1 + 1 = 2.

```

Example 3:**

```

**Input:** n = 4
**Output:** 3
**Explanation:** F(4) = F(3) + F(2) = 2 + 1 = 3.

```

 

**Constraints:**

	- `0 <= n <= 30`

## 🧠 Solution Explanation

**Intuition**
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. This problem asks us to calculate the nth Fibonacci number efficiently. We can use dynamic programming to store and reuse previously computed values, avoiding redundant calculations.

**Approach**
1. Handle the base cases where n is less than 2, returning n directly.
2. Initialize two variables a and b to store the last two Fibonacci numbers (0 and 1).
3. Iterate from n = 2 to n (inclusive) using a for loop.
4. In each iteration, update a and b to the next two Fibonacci numbers by swapping their values and adding a to b.
5. After the loop, return the last calculated Fibonacci number b.

**Time Complexity**
O(n) - The loop runs n-1 times, and each iteration performs a constant amount of work.

**Space Complexity**
O(1) - We only use a constant amount of space to store the last two Fibonacci numbers, regardless of the input size.

**Key Insight**
The key insight is that we only need to keep track of the last two Fibonacci numbers to calculate the next one. This allows us to optimize the space complexity to O(1) and still achieve a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 27 ms (Beats 99.9%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-10-11 |
| 💻 Language | Python |