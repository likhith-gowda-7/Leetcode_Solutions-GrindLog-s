> 📌 **Cross-listed:** Primary location is [Array/3300-Minimum-Element-After-Replacement-With-Digit-Sum](../../Array/3300-Minimum-Element-After-Replacement-With-Digit-Sum). This problem also appears under: **Array**, **Math**

# 3300. Minimum Element After Replacement With Digit Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/)


## 📝 Problem Description

You are given an integer array `nums`.

You replace each element in `nums` with the **sum** of its digits.

Return the **minimum** element in `nums` after all replacements.

 

Example 1:**

**Input:** nums = [10,12,13,14]

**Output:** 1

**Explanation:**

`nums` becomes `[1, 3, 4, 5]` after all replacements, with minimum element 1.

Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** 1

**Explanation:**

`nums` becomes `[1, 2, 3, 4]` after all replacements, with minimum element 1.

Example 3:**

**Input:** nums = [999,19,199]

**Output:** 10

**Explanation:**

`nums` becomes `[27, 10, 19]` after all replacements, with minimum element 10.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through each number in the input array, replacing it with the sum of its digits, and keeping track of the minimum element seen so far. This approach takes advantage of the fact that the minimum element after replacement is the minimum of the sum of digits of all elements.

**Approach**
1. Initialize `mini` to the first element of the input array `nums`.
2. Iterate through each element `num` in `nums`.
3. For each `num`, calculate the sum of its digits by repeatedly taking the remainder when divided by 10 (to get the last digit) and adding it to a running total `curr`.
4. Update `mini` to be the minimum of its current value and `curr`.
5. After iterating through all elements, return `mini` as the minimum element after replacement.

**Time Complexity**
O(n * k), where n is the length of the input array and k is the maximum number of digits in any element. This is because we iterate through each element once, and for each element, we perform a constant amount of work to calculate the sum of its digits.

**Space Complexity**
O(1), excluding the space required for the input array. We only use a constant amount of space to store the `mini` variable and the `curr` variable.

**Key Insight**
The key insight is that the minimum element after replacement is the minimum of the sum of digits of all elements. This allows us to simply iterate through each element, calculate the sum of its digits, and keep track of the minimum seen so far.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 76.62%) |
| 💾 Memory | 19.3 MB (Beats 68.05%) |
| 📅 Solved | 2026-05-29 |
| 💻 Language | Python |