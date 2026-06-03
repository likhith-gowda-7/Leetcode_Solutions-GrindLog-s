> 📌 **Cross-listed:** Primary location is [Array/3652-Best-Time-to-Buy-and-Sell-Stock-using-Strategy](../../Array/3652-Best-Time-to-Buy-and-Sell-Stock-using-Strategy). This problem also appears under: **Array**, **Sliding Window**, **Prefix Sum**

# 3652. Best Time to Buy and Sell Stock using Strategy


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/)


## 📝 Problem Description

You are given two integer arrays `prices` and `strategy`, where:

	- `prices[i]` is the price of a given stock on the `i^th` day.

	- `strategy[i]` represents a trading action on the `i^th` day, where:
	
		- `-1` indicates buying one unit of the stock.

		- `0` indicates holding the stock.

		- `1` indicates selling one unit of the stock.

	
	

You are also given an **even** integer `k`, and may perform **at most one** modification to `strategy`. A modification consists of:

	- Selecting exactly `k` **consecutive** elements in `strategy`.

	- Set the **first** `k / 2` elements to `0` (hold).

	- Set the **last** `k / 2` elements to `1` (sell).

The **profit** is defined as the **sum** of `strategy[i] * prices[i]` across all days.

Return the **maximum** possible profit you can achieve.

**Note:** There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.

 

Example 1:**

**Input:** prices = [4,2,8], strategy = [-1,0,1], k = 2

**Output:** 10

**Explanation:**

	
		
			Modification
			Strategy
			Profit Calculation
			Profit
		
	
	
		
			Original
			[-1, 0, 1]
			(-1 &times; 4) + (0 &times; 2) + (1 &times; 8) = -4 + 0 + 8
			4
		
		
			Modify [0, 1]
			[0, 1, 1]
			(0 &times; 4) + (1 &times; 2) + (1 &times; 8) = 0 + 2 + 8
			10
		
		
			Modify [1, 2]
			[-1, 0, 1]
			(-1 &times; 4) + (0 &times; 2) + (1 &times; 8) = -4 + 0 + 8
			4
		
	

Thus, the maximum possible profit is 10, which is achieved by modifying the subarray `[0, 1]`​​​​​​​.

Example 2:**

**Input:** prices = [5,4,3], strategy = [1,1,0], k = 2

**Output:** 9

**Explanation:**

	
		
			Modification
			Strategy
			Profit Calculation
			Profit
		
	
	
		
			Original
			[1, 1, 0]
			(1 &times; 5) + (1 &times; 4) + (0 &times; 3) = 5 + 4 + 0
			9
		
		
			Modify [0, 1]
			[0, 1, 0]
			(0 &times; 5) + (1 &times; 4) + (0 &times; 3) = 0 + 4 + 0
			4
		
		
			Modify [1, 2]
			[1, 0, 1]
			(1 &times; 5) + (0 &times; 4) + (1 &times; 3) = 5 + 0 + 3
			8
		
	

Thus, the maximum possible profit is 9, which is achieved without any modification.

 

**Constraints:**

	- `2 <= prices.length == strategy.length <= 10^5`

	- `1 <= prices[i] <= 10^5`

	- `-1 <= strategy[i] <= 1`

	- `2 <= k <= prices.length`

	- `k` is even

## 🧠 Solution Explanation

**Intuition**
The solution calculates the maximum possible profit by considering all possible modifications to the `strategy` array. It uses a prefix sum approach to efficiently calculate the sum of profits for any given subarray. The key insight is to find the optimal subarray where the first half is modified to hold and the last half is modified to sell.

**Approach**
1. Calculate the prefix sum of profits and the base profit array.
2. Initialize variables to keep track of the current window and the maximum profit.
3. Iterate over the `strategy` array, considering each window of size `k`.
4. For each window, calculate the sum of profits for the first half and the last half.
5. Update the maximum profit if the current profit is higher.
6. Move the window to the right by incrementing the `l` variable.

**Time Complexity**
O(n), where n is the length of the `prices` array. This is because we need to iterate over the array once to calculate the prefix sum and once to consider all possible windows.

**Space Complexity**
O(n), where n is the length of the `prices` array. This is because we need to store the prefix sum and base profit arrays.

**Key Insight**
The key insight is to use the prefix sum to efficiently calculate the sum of profits for any given subarray. By doing so, we can avoid recalculating the sum for each subarray, which would result in a time complexity of O(n^2).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 292 ms (Beats 38.16%) |
| 💾 Memory | 33.9 MB (Beats 38.85%) |
| 📅 Solved | 2025-12-18 |
| 💻 Language | Python |