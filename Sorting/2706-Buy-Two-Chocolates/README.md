> 📌 **Cross-listed:** Primary location is [Array/2706-Buy-Two-Chocolates](../../Array/2706-Buy-Two-Chocolates). This problem also appears under: **Array**, **Greedy**, **Sorting**

# 2706. Buy Two Chocolates


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/buy-two-chocolates/)


## 📝 Problem Description

You are given an integer array `prices` representing the prices of various chocolates in a store. You are also given a single integer `money`, which represents your initial amount of money.

You must buy **exactly** two chocolates in such a way that you still have some **non-negative** leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

Return *the amount of money you will have leftover after buying the two chocolates*. If there is no way for you to buy two chocolates without ending up in debt, return `money`. Note that the leftover must be non-negative.

 

Example 1:**

```

**Input:** prices = [1,2,2], money = 3
**Output:** 0
**Explanation:** Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.

```

Example 2:**

```

**Input:** prices = [3,2,3], money = 3
**Output:** 3
**Explanation:** You cannot buy 2 chocolates without going in debt, so we return 3.

```

 

**Constraints:**

	- `2 <= prices.length <= 50`

	- `1 <= prices[i] <= 100`

	- `1 <= money <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by first finding the two smallest prices in the `prices` array. This is because we want to minimize the sum of the prices of the two chocolates we buy. We then subtract this sum from the initial `money` to get the leftover amount. If the leftover amount is negative, it means we cannot buy two chocolates without going into debt, so we return the initial `money`.

**Approach**
1. Use the `nsmallest` function from the `heapq` module to find the two smallest prices in the `prices` array.
2. Calculate the sum of these two smallest prices and subtract it from the initial `money` to get the leftover amount.
3. If the leftover amount is negative, return the initial `money`; otherwise, return the leftover amount.

**Time Complexity**
O(n log n) due to the `nsmallest` function, which uses a heap to find the k smallest elements in the array. The heap operations (insertion and extraction) take O(log n) time, and we perform these operations n times.

**Space Complexity**
O(n) for the heap used by the `nsmallest` function, where n is the number of elements in the `prices` array.

**Key Insight**
The key insight is that we can find the optimal solution by simply buying the two cheapest chocolates, as this will minimize the sum of their prices. This is a classic example of a greedy algorithm, where we make the locally optimal choice at each step (buying the cheapest chocolates) in the hope that it will lead to a globally optimal solution (minimizing the sum of the prices).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-02-15 |
| 💻 Language | Python |