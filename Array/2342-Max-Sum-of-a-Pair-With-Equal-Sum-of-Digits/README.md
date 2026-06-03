# 2342. Max Sum of a Pair With Equal Sum of Digits


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/)


## 📝 Problem Description

You are given a **0-indexed** array `nums` consisting of **positive** integers. You can choose two indices `i` and `j`, such that `i != j`, and the sum of digits of the number `nums[i]` is equal to that of `nums[j]`.

Return the **maximum** value of* *`nums[i] + nums[j]`* *that you can obtain over all possible indices `i` and `j` that satisfy the conditions. If no such pair of indices exists, return -1.

 

Example 1:**

```

**Input:** nums = [18,43,36,13,7]
**Output:** 54
**Explanation:** The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

```

Example 2:**

```

**Input:** nums = [10,12,19,14]
**Output:** -1
**Explanation:** There are no two numbers that satisfy the conditions, so we return -1.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to store the maximum number seen so far for each possible sum of digits. It then iterates over the array, updating the hash table and keeping track of the maximum sum that can be obtained.

**Approach**

1. Define a helper function `summing` to calculate the sum of digits of a given number.
2. Initialize a hash table `h1` to store the maximum number seen so far for each possible sum of digits.
3. Iterate over the array `nums`:
   1. Calculate the sum of digits of the current number `n` using the `summing` function.
   2. Check if the sum of digits is already in the hash table `h1`. If it is, update the current maximum sum `curr` by adding the current number `n` to the maximum number stored in the hash table.
   3. Update the hash table `h1` with the current number `n` if it is greater than the maximum number stored for the same sum of digits.
   4. Update the maximum sum `maxi` with the current maximum sum `curr`.
4. If the maximum sum `maxi` is still 0 after iterating over the array, return -1. Otherwise, return the maximum sum `maxi`.

**Time Complexity**
O(n*m), where n is the length of the array `nums` and m is the maximum number of digits in any number in the array. This is because we are iterating over the array once and for each number, we are calculating the sum of its digits, which takes at most m operations.

**Space Complexity**
O(n*m), where n is the length of the array `nums` and m is the maximum number of digits in any number in the array. This is because we are storing the maximum number seen so far for each possible sum of digits in the hash table, which can take up to n*m space.

**Key Insight**
The key insight is to use a hash table to store the maximum number seen so far for each possible sum of digits, allowing us to efficiently find the maximum sum that can be obtained by adding two numbers with equal sum of digits.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 316 ms (Beats 53.79%) |
| 💾 Memory | 33.5 MB (Beats 40.3%) |
| 📅 Solved | 2025-02-12 |
| 💻 Language | Python |