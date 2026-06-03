> 📌 **Cross-listed:** Primary location is [Array/2144-Minimum-Cost-of-Buying-Candies-With-Discount](../../Array/2144-Minimum-Cost-of-Buying-Candies-With-Discount). This problem also appears under: **Array**, **Greedy**, **Sorting**

# 2144. Minimum Cost of Buying Candies With Discount


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/)


## 📝 Problem Description

A shop is selling candies at a discount. For **every two** candies sold, the shop gives a **third** candy for **free**.

The customer can choose **any** candy to take away for free as long as the cost of the chosen candy is less than or equal to the **minimum** cost of the two candies bought.

	- For example, if there are `4` candies with costs `1`, `2`, `3`, and `4`, and the customer buys candies with costs `2` and `3`, they can take the candy with cost `1` for free, but not the candy with cost `4`.

Given a **0-indexed** integer array `cost`, where `cost[i]` denotes the cost of the `i^th` candy, return *the **minimum cost** of buying **all** the candies*.

 

Example 1:**

```

**Input:** cost = [1,2,3]
**Output:** 5
**Explanation:** We buy the candies with costs 2 and 3, and take the candy with cost 1 for free.
The total cost of buying all candies is 2 + 3 = 5. This is the **only** way we can buy the candies.
Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free.
The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.

```

Example 2:**

```

**Input:** cost = [6,5,7,9,2,2]
**Output:** 23
**Explanation:** The way in which we can get the minimum cost is described below:
- Buy candies with costs 9 and 7
- Take the candy with cost 6 for free
- We buy candies with costs 5 and 2
- Take the last remaining candy with cost 2 for free
Hence, the minimum cost to buy all candies is 9 + 7 + 5 + 2 = 23.

```

Example 3:**

```

**Input:** cost = [5,5]
**Output:** 10
**Explanation:** Since there are only 2 candies, we buy both of them. There is not a third candy we can take for free.
Hence, the minimum cost to buy all candies is 5 + 5 = 10.

```

 

**Constraints:**

	- `1 <= cost.length <= 100`

	- `1 <= cost[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution takes advantage of the discount policy, where for every two candies sold, a third candy is given for free. It sorts the candies in descending order of cost and then iterates through them, buying two candies at a time and taking the cheapest one for free.

**Approach**
1. Sort the candies in descending order of cost using `cost.sort(reverse=True)`.
2. Initialize variables `total_cost` to keep track of the total cost and `buyed` to keep track of the number of candies bought.
3. Iterate through the sorted candies. For each candy:
   - If `buyed` is 2, reset it to 0 and skip this candy.
   - Add the current candy's cost to `total_cost`.
   - Increment `buyed` by 1.
4. Return `total_cost` as the minimum cost of buying all candies.

**Time Complexity**
O(n log n) due to the sorting operation, where n is the number of candies. The subsequent iteration through the sorted array takes O(n) time, but it's dominated by the sorting step.

**Space Complexity**
O(1) (excluding the input array) since we only use a constant amount of space to store the `total_cost` and `buyed` variables.

**Key Insight**
The key insight is that by sorting the candies in descending order, we can always choose the cheapest candy to take for free, ensuring the minimum cost. This greedy approach takes advantage of the discount policy and leads to an efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 48.06%) |
| 📅 Solved | 2026-06-01 |
| 💻 Language | Python |