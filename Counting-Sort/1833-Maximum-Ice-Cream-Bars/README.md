> 📌 **Cross-listed:** Primary location is [Array/1833-Maximum-Ice-Cream-Bars](../../Array/1833-Maximum-Ice-Cream-Bars). This problem also appears under: **Array**, **Greedy**, **Sorting**, **Counting Sort**

# 1833. Maximum Ice Cream Bars


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Counting Sort](https://img.shields.io/badge/Counting%20Sort-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/)


## 📝 Problem Description

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are `n` ice cream bars. You are given an array `costs` of length `n`, where `costs[i]` is the price of the `i^th` ice cream bar in coins. The boy initially has `coins` coins to spend, and he wants to buy as many ice cream bars as possible. 

**Note:** The boy can buy the ice cream bars in any order.

Return *the **maximum** number of ice cream bars the boy can buy with *`coins`* coins.*

You must solve the problem by counting sort.

 

Example 1:**

```

**Input:** costs = [1,3,2,4,1], coins = 7
**Output:** 4
**Explanation: **The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

```

Example 2:**

```

**Input:** costs = [10,6,8,7,7,8], coins = 5
**Output:** 0
**Explanation: **The boy cannot afford any of the ice cream bars.

```

Example 3:**

```

**Input:** costs = [1,6,3,1,2,5], coins = 20
**Output:** 6
**Explanation: **The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

```

 

**Constraints:**

	- `costs.length == n`

	- `1 <= n <= 10^5`

	- `1 <= costs[i] <= 10^5`

	- `1 <= coins <= 10^8`

## 🧠 Solution Explanation

**Intuition**
The solution works by sorting the costs array in ascending order and then iterating through it, buying as many ice cream bars as possible without exceeding the available coins. This greedy approach ensures that we maximize the number of ice cream bars bought.

**Approach**
1. Sort the `costs` array in ascending order using the `sort()` method.
2. Initialize a variable `taken` to keep track of the number of ice cream bars bought.
3. Iterate through the sorted `costs` array.
4. For each cost, check if we have enough coins to buy the ice cream bar. If we do, increment `taken` and subtract the cost from the available coins.
5. If we don't have enough coins, break out of the loop.
6. Return the total number of ice cream bars bought (`taken`).

**Time Complexity**
O(n log n) due to the sorting step, where n is the number of ice cream bars. The subsequent iteration through the sorted array takes O(n) time, but the sorting dominates the overall time complexity.

**Space Complexity**
O(1) since we only use a constant amount of space to store the `taken` variable and the loop index, regardless of the input size.

**Key Insight**
The key insight is that by sorting the costs array, we can apply a greedy strategy to maximize the number of ice cream bars bought. By always choosing the cheapest ice cream bar available, we ensure that we spend the least amount of coins possible, allowing us to buy more ice cream bars.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 83 ms (Beats 57.98%) |
| 💾 Memory | 32 MB (Beats 44.03%) |
| 📅 Solved | 2026-06-21 |
| 💻 Language | Python |