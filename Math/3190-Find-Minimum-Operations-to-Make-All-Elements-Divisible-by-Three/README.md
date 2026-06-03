> 📌 **Cross-listed:** Primary location is [Array/3190-Find-Minimum-Operations-to-Make-All-Elements-Divisible-by-Three](../../Array/3190-Find-Minimum-Operations-to-Make-All-Elements-Divisible-by-Three). This problem also appears under: **Array**, **Math**

# 3190. Find Minimum Operations to Make All Elements Divisible by Three


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/)


## 📝 Problem Description

You are given an integer array `nums`. In one operation, you can add or subtract 1 from **any** element of `nums`.

Return the **minimum** number of operations to make all elements of `nums` divisible by 3.

 

Example 1:**

**Input:** nums = [1,2,3,4]

**Output:** 3

**Explanation:**

All array elements can be made divisible by 3 using 3 operations:

	- Subtract 1 from 1.

	- Add 1 to 2.

	- Subtract 1 from 4.

Example 2:**

**Input:** nums = [3,6,9]

**Output:** 0

 

**Constraints:**

	- `1 <= nums.length <= 50`

	- `1 <= nums[i] <= 50`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through each number in the array and finding the minimum number of operations required to make it divisible by 3. The key insight is that we can make a number divisible by 3 by either subtracting or adding the difference between the number and its nearest multiple of 3.

**Approach**
1. Initialize a variable `res` to store the total minimum number of operations.
2. Iterate through each number `num` in the array `nums`.
3. Calculate the difference `diff` between `num` and its nearest multiple of 3.
4. If `diff` is not zero, calculate the minimum number of operations required to make `num` divisible by 3. This is done by finding the minimum between `3 - diff` and `diff - 0`.
5. Add the minimum number of operations to `res`.
6. Return `res` as the total minimum number of operations.

**Time Complexity**
O(n), where n is the number of elements in the array. This is because we are iterating through each element in the array once.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the variables `res`, `num`, and `diff`.

**Key Insight**
The key insight is that we can make a number divisible by 3 by either subtracting or adding the difference between the number and its nearest multiple of 3. This allows us to find the minimum number of operations required to make each number in the array divisible by 3.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-11-22 |
| 💻 Language | Python |