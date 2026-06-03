# 1800. Maximum Ascending Subarray Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-ascending-subarray-sum/)


## 📝 Problem Description

Given an array of positive integers `nums`, return the **maximum** possible sum of an strictly increasing subarray in* *`nums`.

A subarray is defined as a contiguous sequence of numbers in an array.

 

Example 1:**

```

**Input:** nums = [10,20,30,5,10,50]
**Output:** 65
**Explanation: **[5,10,50] is the ascending subarray with the maximum sum of 65.

```

Example 2:**

```

**Input:** nums = [10,20,30,40,50]
**Output:** 150
**Explanation: **[10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

```

Example 3:**

```

**Input:** nums = [12,17,15,13,10,11,12]
**Output:** 33
**Explanation: **[10,11,12] is the ascending subarray with the maximum sum of 33.

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a running sum of the current ascending subarray and updating it whenever a smaller number is encountered. This approach is based on the observation that a strictly increasing subarray can only be extended by adding the next number if it is larger than the previous one.

**Approach**
1. Initialize `maxi` and `curr` to the first number in the array, which is the starting point of the ascending subarray.
2. Iterate through the array starting from the second number.
3. For each number, check if it is larger than the previous one. If it is, add it to the current sum `curr`.
4. If the current number is not larger than the previous one, reset the current sum `curr` to the current number.
5. Update `maxi` to be the maximum of the current maximum sum `maxi` and the current sum `curr`.
6. Return `maxi` as the maximum possible sum of an ascending subarray.

**Time Complexity**
O(n), where n is the length of the array. This is because we are iterating through the array once.

**Space Complexity**
O(1), as we are using a constant amount of space to store the `maxi` and `curr` variables.

**Key Insight**
The key insight is that we only need to keep track of the current ascending subarray and the maximum sum seen so far, which allows us to solve the problem in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-04 |
| 💻 Language | Python |