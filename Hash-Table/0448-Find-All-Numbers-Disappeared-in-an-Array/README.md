> 📌 **Cross-listed:** Primary location is [Array/0448-Find-All-Numbers-Disappeared-in-an-Array](../../Array/0448-Find-All-Numbers-Disappeared-in-an-Array). This problem also appears under: **Array**, **Hash Table**

# 448. Find All Numbers Disappeared in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)


## 📝 Problem Description

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return *an array of all the integers in the range* `[1, n]` *that do not appear in* `nums`.

 

Example 1:**

```
**Input:** nums = [4,3,2,7,8,2,3,1]
**Output:** [5,6]

```
Example 2:**

```
**Input:** nums = [1,1]
**Output:** [2]

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 10^5`

	- `1 <= nums[i] <= n`

 

**Follow up:** Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.

## 🧠 Solution Explanation

## Intuition
This approach works by first converting the input list into a set for efficient lookups, then iterating over the range of possible numbers to find the ones that are missing from the set. The use of a set allows for constant-time membership checks, making the overall solution efficient. By iterating over the range of possible numbers, we can ensure that we don't miss any numbers that should be in the output.

## Approach
1. Convert the input list `nums` into a set to remove duplicates and enable fast lookups.
2. Initialize an empty list `res` to store the disappeared numbers.
3. Iterate over the range of possible numbers from 1 to `n` (inclusive).
4. For each number `i` in the range, check if it is not in the set `nums`.
5. If `i` is not in the set, append it to the `res` list.

## Time Complexity
The time complexity is O(n), where n is the length of the input list. This is because we perform a constant amount of work for each number in the input list (converting to a set and iterating over the range).

## Space Complexity
The space complexity is O(n), where n is the length of the input list. This is because in the worst case, we need to store all numbers in the set, and the output list can also contain up to n numbers.

## Key Insight
The key insight here is to use a set to store the input numbers, allowing for efficient membership checks and enabling us to find the missing numbers in linear time. However, this approach does not meet the follow-up requirement of using no extra space, as it uses a set to store the input numbers.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 23 ms (Beats 78.02%) |
| 💾 Memory | 31.5 MB (Beats 18.77%) |
| 📅 Solved | 2025-11-14 |
| 💻 Language | Python |