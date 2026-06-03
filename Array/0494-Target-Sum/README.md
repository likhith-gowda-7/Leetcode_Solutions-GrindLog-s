# 494. Target Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/target-sum/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

	- For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

 

Example 1:**

```

**Input:** nums = [1,1,1,1,1], target = 3
**Output:** 5
**Explanation:** There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

```

Example 2:**

```

**Input:** nums = [1], target = 1
**Output:** 1

```

 

**Constraints:**

	- `1 <= nums.length <= 20`

	- `0 <= nums[i] <= 1000`

	- `0 <= sum(nums[i]) <= 1000`

	- `-1000 <= target <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming to count the number of ways to assign symbols to the integers in the array such that the expression evaluates to the target. The idea is to build up a table `dp` where `dp[i]` represents the number of ways to reach a sum of `i` using the given integers.

**Approach**
1. Calculate the total sum of the integers in the array.
2. If the target is greater than the total sum or if the difference between the total sum and the target is odd, return 0 because it's impossible to reach the target.
3. Calculate the target sum as `(total - target) // 2`, because we can add or subtract each integer to reach the target.
4. Initialize a table `dp` of size `target + 1` with all elements set to 0, except `dp[0]` which is set to 1 (there is one way to reach a sum of 0 by not using any integers).
5. Iterate over each integer in the array, and for each integer, iterate over the table `dp` in reverse order (from `target` to `num - 1`).
6. For each element `s` in the table, add the number of ways to reach a sum of `s - num` (i.e., `dp[s - num]`) to the current element `dp[s]`.

**Time Complexity**
O(n * target), where n is the length of the array and target is the target sum. This is because we iterate over each integer in the array and over the table `dp` in reverse order.

**Space Complexity**
O(target), because we need to store the table `dp` of size `target + 1`.

**Key Insight**
The key insight is to use dynamic programming to build up a table `dp` that represents the number of ways to reach each possible sum. By iterating over the table in reverse order, we can avoid redundant calculations and achieve a more efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 19 ms (Beats 88.85%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-12-03 |
| 💻 Language | Python |