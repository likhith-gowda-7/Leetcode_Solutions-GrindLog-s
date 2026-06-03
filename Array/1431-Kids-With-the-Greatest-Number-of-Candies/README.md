# 1431. Kids With the Greatest Number of Candies


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)


## 📝 Problem Description

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i^th` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return *a boolean array *`result`* of length *`n`*, where *`result[i]`* is *`true`* if, after giving the *`i^th`* kid all the *`extraCandies`*, they will have the **greatest** number of candies among all the kids**, or *`false`* otherwise*.

Note that **multiple** kids can have the **greatest** number of candies.

 

Example 1:**

```

**Input:** candies = [2,3,5,1,3], extraCandies = 3
**Output:** [true,true,true,false,true] 
**Explanation:** If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

```

Example 2:**

```

**Input:** candies = [4,2,1,1,2], extraCandies = 1
**Output:** [true,false,false,false,false] 
**Explanation:** There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

```

Example 3:**

```

**Input:** candies = [12,1,12], extraCandies = 10
**Output:** [true,false,true]

```

 

**Constraints:**

	- `n == candies.length`

	- `2 <= n <= 100`

	- `1 <= candies[i] <= 100`

	- `1 <= extraCandies <= 50`

## 🧠 Solution Explanation

**Intuition**
The solution iterates through each kid's candies and checks if giving them the extra candies would make them have the greatest number of candies among all kids. This is done by comparing the kid's candies plus the extra candies to the maximum number of candies any kid has.

**Approach**
1. Find the maximum number of candies any kid has.
2. Iterate through each kid's candies.
3. For each kid, check if giving them the extra candies would make them have the greatest number of candies (i.e., if their candies plus extra candies is greater than or equal to the maximum number of candies).
4. If it would, mark their candies as `True` in the result array; otherwise, mark it as `False`.
5. Return the result array.

**Time Complexity**
O(n), where n is the number of kids. This is because we only need to iterate through each kid's candies once.

**Space Complexity**
O(1), excluding the space needed for the input and output arrays. We only use a constant amount of space to store the maximum number of candies and the result array.

**Key Insight**
The key insight is that we only need to compare each kid's candies to the maximum number of candies, rather than comparing each kid's candies to every other kid's candies. This makes the solution efficient and scalable for large inputs.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 12.1 MB (Beats 99.96%) |
| 📅 Solved | 2024-12-05 |
| 💻 Language | Python |