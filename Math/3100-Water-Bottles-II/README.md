# 3100. Water Bottles II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/water-bottles-ii/)


## 📝 Problem Description

You are given two integers `numBottles` and `numExchange`.

`numBottles` represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

	- Drink any number of full water bottles turning them into empty bottles.

	- Exchange `numExchange` empty bottles with one full water bottle. Then, increase `numExchange` by one.

Note that you cannot exchange multiple batches of empty bottles for the same value of `numExchange`. For example, if `numBottles == 3` and `numExchange == 1`, you cannot exchange `3` empty water bottles for `3` full bottles.

Return *the **maximum** number of water bottles you can drink*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2024/01/28/exampleone1.png)
```

**Input:** numBottles = 13, numExchange = 6
**Output:** 15
**Explanation:** The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2024/01/28/example231.png)
```

**Input:** numBottles = 10, numExchange = 3
**Output:** 13
**Explanation:** The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.

```

 

**Constraints:**

	- `1 <= numBottles <= 100 `

	- `1 <= numExchange <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by simulating the process of exchanging empty bottles for full ones, always maximizing the number of water bottles drunk. The key insight is that we can always drink all the full bottles we already have, so we start with the initial number of bottles as the result.

**Approach**
1. Initialize the result (`res`) to the initial number of bottles (`numBottles`).
2. While there are enough bottles to exchange (`numBottles >= numExchange`):
   1. Drink `numExchange` bottles by subtracting it from `numBottles`.
   2. Increment the result (`res`) by 1, since we can drink one more bottle.
   3. Increment `numBottles` by 1, since we get one full bottle from exchanging `numExchange` empty bottles.
   4. Increment `numExchange` by 1, since we can exchange one more empty bottle for a full one in the next iteration.
3. Return the result (`res`).

**Time Complexity**
O(n), where n is the number of iterations of the while loop. In the worst case, we exchange all bottles, and the number of iterations is equal to the initial number of bottles.

**Space Complexity**
O(1), since we only use a constant amount of space to store the result, `numBottles`, `numExchange`, and the loop variables.

**Key Insight**
The key insight is that we can always drink all the full bottles we already have, so we start with the initial number of bottles as the result. This simplifies the problem and allows us to focus on exchanging empty bottles for full ones.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 45 ms (Beats 57.14%) |
| 💾 Memory | 17.5 MB (Beats 100%) |
| 📅 Solved | 2025-10-02 |
| 💻 Language | Python |