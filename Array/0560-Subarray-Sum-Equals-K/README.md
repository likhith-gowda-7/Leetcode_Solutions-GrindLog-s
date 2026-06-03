# 560. Subarray Sum Equals K


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)


## 📝 Problem Description

Given an array of integers `nums` and an integer `k`, return *the total number of subarrays whose sum equals to* `k`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

 

Example 1:**

```
**Input:** nums = [1,1,1], k = 2
**Output:** 2

```
Example 2:**

```
**Input:** nums = [1,2,3], k = 3
**Output:** 2

```

 

**Constraints:**

	- `1 <= nums.length <= 2 * 10^4`

	- `-1000 <= nums[i] <= 1000`

	- `-10^7 <= k <= 10^7`

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to store the prefix sums of the array and their frequencies. It iterates through the array, updating the prefix sum and checking if the difference between the current prefix sum and the target sum `k` exists in the hash table. If it does, it increments the count by the frequency of that prefix sum. This approach works because the prefix sum of a subarray is equal to the sum of the elements in that subarray.

**Approach**
1. Initialize a hash table `h` with a key of 0 and a value of 1, representing the base case where the sum of an empty subarray is 0.
2. Initialize a variable `count` to 0, which will store the total number of subarrays with sum `k`.
3. Initialize a variable `pr` to 0, which will store the current prefix sum.
4. Iterate through the array `nums`:
   1. Add the current number to `pr` to update the prefix sum.
   2. Check if `pr - k` exists in the hash table `h`. If it does, increment `count` by the frequency of `pr - k`.
   3. Check if `pr` exists in the hash table `h`. If it does, increment the frequency of `pr` by 1. If not, add `pr` to the hash table with a frequency of 1.
5. Return `count` as the total number of subarrays with sum `k`.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we iterate through the array once, performing constant-time operations for each element.

**Space Complexity**
O(n), where n is the length of the array `nums`. This is because in the worst case, we store all prefix sums in the hash table.

**Key Insight**
The key insight is to use the prefix sum to efficiently count the number of subarrays with a given sum. By storing the prefix sums in a hash table, we can quickly look up the frequency of each prefix sum and update the count accordingly. This approach allows us to solve the problem in linear time and space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 18 ms (Beats 99.87%) |
| 💾 Memory | 20.3 MB (Beats 100%) |
| 📅 Solved | 2025-03-11 |
| 💻 Language | Python |