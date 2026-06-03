> 📌 **Cross-listed:** Primary location is [Math/0070-Climbing-Stairs](../../Math/0070-Climbing-Stairs). This problem also appears under: **Math**, **Dynamic Programming**, **Memoization**

# 70. Climbing Stairs


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Memoization](https://img.shields.io/badge/Memoization-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/climbing-stairs/)


## 📝 Problem Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

 

Example 1:**

```

**Input:** n = 2
**Output:** 2
**Explanation:** There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

Example 2:**

```

**Input:** n = 3
**Output:** 3
**Explanation:** There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

 

**Constraints:**

	- `1 <= n <= 45`

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using dynamic programming because the solution to each step depends only on the previous two steps. We can store the number of ways to reach each step and use it to calculate the number of ways to reach the next step.

**Approach**
1. Initialize two variables, `two_step_back` and `one_step_back`, to 1, representing the number of ways to reach the first two steps (1 and 2 steps respectively).
2. Iterate from the third step to the `n`-th step.
3. For each step, calculate the number of ways to reach it by adding the number of ways to reach the previous step (`one_step_back`) and the number of ways to reach the step before that (`two_step_back`).
4. Update `two_step_back` and `one_step_back` with the new values.
5. After iterating through all steps, return `one_step_back`, which represents the number of ways to reach the top.

**Time Complexity**
O(n), where n is the number of steps. This is because we are iterating through each step once.

**Space Complexity**
O(1), because we are using a constant amount of space to store `two_step_back` and `one_step_back`, regardless of the input size.

**Key Insight**
The key insight is that the number of ways to reach each step depends only on the previous two steps, allowing us to use a simple iterative approach with dynamic programming to solve the problem efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-12-15 |
| 💻 Language | Python |