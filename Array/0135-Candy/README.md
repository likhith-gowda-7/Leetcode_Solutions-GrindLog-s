# 135. Candy


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/candy/)


## 📝 Problem Description

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

	- Each child must have at least one candy.

	- Children with a higher rating get more candies than their neighbors.

Return *the minimum number of candies you need to have to distribute the candies to the children*.

 

Example 1:**

```

**Input:** ratings = [1,0,2]
**Output:** 5
**Explanation:** You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

```

Example 2:**

```

**Input:** ratings = [1,2,2]
**Output:** 4
**Explanation:** You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

```

 

**Constraints:**

	- `n == ratings.length`

	- `1 <= n <= 2 * 10^4`

	- `0 <= ratings[i] <= 2 * 10^4`

## 🧠 Solution Explanation

## Intuition
The problem can be solved using a greedy approach by iterating through the ratings array twice. The first pass ensures that children with higher ratings than their left neighbor get more candies, and the second pass ensures that children with higher ratings than their right neighbor get more candies. This approach works because it satisfies the condition that children with higher ratings get more candies than their neighbors.

## Approach
1. Initialize an array `candy` with the same length as the `ratings` array, where each child is initially assigned one candy.
2. Iterate through the `ratings` array from left to right, and for each child, if their rating is higher than their left neighbor's rating, assign them one more candy than their left neighbor.
3. Iterate through the `ratings` array from right to left, and for each child, if their rating is higher than their right neighbor's rating, update their candy count to be the maximum of their current candy count and one more than their right neighbor's candy count.
4. Return the sum of the `candy` array, which represents the minimum number of candies needed.

## Time Complexity
The time complexity is O(n), where n is the number of children, because we are making two passes through the `ratings` array.

## Space Complexity
The space complexity is O(n), where n is the number of children, because we are using an additional array `candy` to store the candy count for each child.

## Key Insight
The key insight is to use two passes to ensure that the conditions are met from both the left and right neighbors, and to use the `max` function to update the candy count in the second pass to avoid overwriting previously assigned candies.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 15 ms (Beats 71.21%) |
| 💾 Memory | 21.4 MB (Beats 77.42%) |
| 📅 Solved | 2026-02-04 |
| 💻 Language | Python |