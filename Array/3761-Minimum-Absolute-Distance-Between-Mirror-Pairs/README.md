# 3761. Minimum Absolute Distance Between Mirror Pairs


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/)


## 📝 Problem Description

You are given an integer array `nums`.

A **mirror pair** is a pair of indices `(i, j)` such that:

	- `0 <= i < j < nums.length`, and

	- `reverse(nums[i]) == nums[j]`, where `reverse(x)` denotes the integer formed by reversing the digits of `x`. Leading zeros are omitted after reversing, for example `reverse(120) = 21`.

Return the **minimum** absolute distance between the indices of any mirror pair. The absolute distance between indices `i` and `j` is `abs(i - j)`.

If no mirror pair exists, return `-1`.

 

Example 1:**

**Input:** nums = [12,21,45,33,54]

**Output:** 1

**Explanation:**

The mirror pairs are:

	- (0, 1) since `reverse(nums[0]) = reverse(12) = 21 = nums[1]`, giving an absolute distance `abs(0 - 1) = 1`.

	- (2, 4) since `reverse(nums[2]) = reverse(45) = 54 = nums[4]`, giving an absolute distance `abs(2 - 4) = 2`.

The minimum absolute distance among all pairs is 1.

Example 2:**

**Input:** nums = [120,21]

**Output:** 1

**Explanation:**

There is only one mirror pair (0, 1) since `reverse(nums[0]) = reverse(120) = 21 = nums[1]`.

The minimum absolute distance is 1.

Example 3:**

**Input:** nums = [21,120]

**Output:** -1

**Explanation:**

There are no mirror pairs in the array.

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`​​​​​​​

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to store the indices of numbers that are reverses of each other. It iterates through the input array, checks for each number if its reverse is already in the hash table, and updates the minimum distance if a mirror pair is found.

**Approach**
1. Initialize an empty hash table `h1` to store the indices of numbers that are reverses of each other.
2. Iterate through the input array `nums` using `enumerate` to get both the index `i` and the value `val` of each element.
3. Convert the value `val` to a string `s` and reverse it to get the reversed string `int_rev`.
4. Remove leading zeros from the reversed string `int_rev` using `lstrip("0")`.
5. Check if the original string `s` is already in the hash table `h1`. If it is, update the minimum distance `min_idx` if the current distance `i - h1[s]` is smaller.
6. Store the index `i` in the hash table `h1` under the key `int_rev`.
7. After iterating through the entire array, return the minimum distance `min_idx` if it is not infinity, otherwise return -1.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we iterate through the array once to populate the hash table and then once more to find the minimum distance.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because in the worst case, we need to store all elements of the array in the hash table.

**Key Insight**
The key insight is to use a hash table to efficiently store and look up the indices of numbers that are reverses of each other. This allows us to find the minimum distance between mirror pairs in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 219 ms (Beats 59.48%) |
| 💾 Memory | 42.7 MB (Beats 13.37%) |
| 📅 Solved | 2026-04-17 |
| 💻 Language | Python |