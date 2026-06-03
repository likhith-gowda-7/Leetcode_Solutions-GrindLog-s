> 📌 **Cross-listed:** Primary location is [Math/2928-Distribute-Candies-Among-Children-I](../../Math/2928-Distribute-Candies-Among-Children-I). This problem also appears under: **Math**, **Combinatorics**, **Enumeration**

# 2928. Distribute Candies Among Children I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Combinatorics](https://img.shields.io/badge/Combinatorics-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/distribute-candies-among-children-i/)


## 📝 Problem Description

You are given two positive integers `n` and `limit`.

Return *the **total number** of ways to distribute *`n` *candies among *`3`* children such that no child gets more than *`limit`* candies.*

 

Example 1:**

```

**Input:** n = 5, limit = 2
**Output:** 3
**Explanation:** There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

```

Example 2:**

```

**Input:** n = 3, limit = 3
**Output:** 10
**Explanation:** There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).

```

 

**Constraints:**

	- `1 <= n <= 50`

	- `1 <= limit <= 50`

## 🧠 Solution Explanation

**Intuition**
The problem asks for the total number of ways to distribute `n` candies among 3 children such that no child gets more than `limit` candies. This can be approached by considering all possible combinations of candies for each child, ensuring that the total number of candies is `n` and no child exceeds the `limit`.

**Approach**
1. Initialize a variable `mini` to be the minimum of `n` and `limit`, which represents the maximum number of candies a child can receive.
2. Initialize a variable `count` to 0, which will store the total number of ways to distribute the candies.
3. Iterate over all possible combinations of candies for the first two children, ranging from 0 to `mini` (inclusive).
4. For each combination, calculate the number of candies the third child should receive by subtracting the sum of the first two children's candies from `n`.
5. Check if the third child's candies are within the valid range (0 to `limit`) and if the total number of candies is equal to `n`. If both conditions are met, increment the `count` by 1.
6. Return the total count of valid distributions.

**Time Complexity**
O(mini^3), where `mini` is the minimum of `n` and `limit`. This is because we have two nested loops iterating over `mini+1` possibilities each, and a constant-time operation inside the loop.

**Space Complexity**
O(1), as we only use a constant amount of space to store the variables `mini`, `count`, and the loop indices.

**Key Insight**
The key to this solution is to recognize that we can iterate over all possible combinations of candies for the first two children, and then calculate the number of candies the third child should receive. By checking if the third child's candies are within the valid range and if the total number of candies is equal to `n`, we can efficiently count the total number of valid distributions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 67.51%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-06-01 |
| 💻 Language | Python |