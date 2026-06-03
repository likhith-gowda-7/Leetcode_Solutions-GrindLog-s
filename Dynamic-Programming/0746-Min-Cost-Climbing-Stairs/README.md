> 📌 **Cross-listed:** Primary location is [Array/0746-Min-Cost-Climbing-Stairs](../../Array/0746-Min-Cost-Climbing-Stairs). This problem also appears under: **Array**, **Dynamic Programming**

# 746. Min Cost Climbing Stairs


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)


## 📝 Problem Description

You are given an integer array `cost` where `cost[i]` is the cost of `i^th` step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return *the minimum cost to reach the top of the floor*.

 

Example 1:**

```

**Input:** cost = [10,15,20]
**Output:** 15
**Explanation:** You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

```

Example 2:**

```

**Input:** cost = [1,100,1,1,1,100,1,1,100,1]
**Output:** 6
**Explanation:** You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

```

 

**Constraints:**

	- `2 <= cost.length <= 1000`

	- `0 <= cost[i] <= 999`

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using dynamic programming, where we maintain two variables `prev1` and `prev2` to store the minimum cost to reach the previous two steps. We can choose to climb one or two steps, and the minimum cost to reach the current step is the minimum cost to reach the previous two steps plus the cost of the current step.

**Approach**
1. Initialize `n` as the length of the `cost` array.
2. Initialize `prev1` and `prev2` as the cost of the first two steps.
3. Iterate from the third step to the last step.
4. In each iteration, update `prev1` and `prev2` by setting `prev1` to `prev2` and `prev2` to the minimum cost to reach the current step, which is the cost of the current step plus the minimum of `prev1` and `prev2`.
5. After the iteration, return the minimum of `prev1` and `prev2`, which is the minimum cost to reach the top of the floor.

**Time Complexity**
O(n), where n is the length of the `cost` array, because we only need to iterate through the array once.

**Space Complexity**
O(1), because we only use a constant amount of space to store `prev1` and `prev2`, regardless of the size of the input array.

**Key Insight**
The key insight is that we can break down the problem into smaller subproblems and solve them recursively, but in this case, we can use dynamic programming to store the solutions to the subproblems and avoid redundant computation.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-10-12 |
| 💻 Language | Python |