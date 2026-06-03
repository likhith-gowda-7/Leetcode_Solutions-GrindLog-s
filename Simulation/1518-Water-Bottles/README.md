> 📌 **Cross-listed:** Primary location is [Math/1518-Water-Bottles](../../Math/1518-Water-Bottles). This problem also appears under: **Math**, **Simulation**

# 1518. Water Bottles


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/water-bottles/)


## 📝 Problem Description

There are `numBottles` water bottles that are initially full of water. You can exchange `numExchange` empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers `numBottles` and `numExchange`, return *the **maximum** number of water bottles you can drink*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2020/07/01/sample_1_1875.png)
```

**Input:** numBottles = 9, numExchange = 3
**Output:** 13
**Explanation:** You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

```

Example 2:**

![](https://assets.leetcode.com/uploads/2020/07/01/sample_2_1875.png)
```

**Input:** numBottles = 15, numExchange = 4
**Output:** 19
**Explanation:** You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.

```

 

**Constraints:**

	- `1 <= numBottles <= 100`

	- `2 <= numExchange <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by simulating the process of exchanging empty bottles for full ones and drinking the full bottles. The key insight is that the number of new full bottles obtained from exchanging empty bottles is dependent on the number of empty bottles available, which in turn depends on the number of full bottles that have been drunk.

**Approach**
1. Initialize the result (res) to the initial number of full bottles (numBottles).
2. Enter a loop that continues until there are not enough bottles to exchange for a new full bottle.
3. Inside the loop:
   1. Calculate the number of new full bottles that can be obtained by exchanging the current number of empty bottles (numBottles) with the exchange rate (numExchange).
   2. Calculate the number of extra empty bottles left after exchanging the current number of empty bottles.
   3. Add the number of new full bottles to the result.
   4. Update the number of bottles (numBottles) to the sum of the new full bottles and the extra empty bottles.
4. Return the result.

**Time Complexity**
O(n), where n is the number of iterations of the loop. In the worst case, the loop runs until numBottles is less than numExchange, which occurs when numBottles is 1. Therefore, the time complexity is linear.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the variables res, numBottles, new_bottles, and extra_empty_bottles.

**Key Insight**
The key insight is that the number of new full bottles obtained from exchanging empty bottles is dependent on the number of empty bottles available, which in turn depends on the number of full bottles that have been drunk. This insight allows us to simulate the process of exchanging and drinking bottles in a simple and efficient manner.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-10-01 |
| 💻 Language | Python |