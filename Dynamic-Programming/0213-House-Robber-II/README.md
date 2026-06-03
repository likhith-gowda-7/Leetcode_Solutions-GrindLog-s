> 📌 **Cross-listed:** Primary location is [Array/0213-House-Robber-II](../../Array/0213-House-Robber-II). This problem also appears under: **Array**, **Dynamic Programming**

# 213. House Robber II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/house-robber-ii/)


## 📝 Problem Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

 

Example 1:**

```

**Input:** nums = [2,3,2]
**Output:** 3
**Explanation:** You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

```

Example 2:**

```

**Input:** nums = [1,2,3,1]
**Output:** 4
**Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

```

Example 3:**

```

**Input:** nums = [1,2,3]
**Output:** 3

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 1000`

## 🧠 Solution Explanation

## Intuition
The House Robber II problem can be solved by breaking it down into two separate cases: one where we rob the first house and another where we don't. This is because the first and last houses are adjacent, so we can't rob both. By considering these two cases, we can find the maximum amount of money that can be robbed.

## Approach
1. Check if the number of houses is less than or equal to 2. If so, return the maximum amount of money in the houses.
2. Define a helper function `solve` that takes an array of house values as input.
3. Initialize two variables `n1` and `n2` to keep track of the maximum amount of money that can be robbed up to the current house.
4. Iterate through the array starting from the third house, updating `n1` and `n2` at each step.
5. Call the `solve` function twice: once with the array excluding the last house (`nums[:-1]`) and once with the array excluding the first house (`nums[1:]`).
6. Return the maximum amount of money that can be robbed from the two cases.

## Time Complexity
The time complexity is O(n), where n is the number of houses. This is because we make two passes through the array, each of which takes O(n) time.

## Space Complexity
The space complexity is O(1), excluding the space needed for the input array. This is because we only use a constant amount of space to store the variables `n1` and `n2`.

## Key Insight
The key insight is to recognize that the problem can be broken down into two separate cases, depending on whether we rob the first house or not. By considering these two cases separately, we can avoid the complexity of dealing with the circular arrangement of houses and find the maximum amount of money that can be robbed.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-10-14 |
| 💻 Language | Python |