> 📌 **Cross-listed:** Primary location is [Array/0268-Missing-Number](../../Array/0268-Missing-Number). This problem also appears under: **Array**, **Hash Table**, **Math**, **Binary Search**, **Bit Manipulation**, **Sorting**

# 268. Missing Number


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/missing-number/)


## 📝 Problem Description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*

 

Example 1:**

**Input:** nums = [3,0,1]

**Output:** 2

**Explanation:**

`n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

Example 2:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

`n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in `nums`.

Example 3:**

**Input:** nums = [9,6,4,2,3,5,7,0,1]

**Output:** 8

**Explanation:**

`n = 9` since there are 9 numbers, so all numbers are in the range `[0,9]`. 8 is the missing number in the range since it does not appear in `nums`.

 

 

 

 

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 10^4`

	- `0 <= nums[i] <= n`

	- All the numbers of `nums` are **unique**.

 

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

## 🧠 Solution Explanation

## Intuition
The solution works by first converting the input list into a set for efficient lookups. It then iterates over the range from 0 to the maximum value in the set to find the missing number. If the iteration completes without finding a missing number, it means the missing number is the next integer after the maximum value.

## Approach
1. Convert the input list `nums` into a set for O(1) lookup times.
2. Find the maximum value `maxi` in the set.
3. Iterate over the range from 0 to `maxi` (inclusive) and check if each number is in the set.
4. If a number is not in the set, return it as the missing number.
5. If the loop completes without finding a missing number, return `maxi + 1` as the missing number.

## Time Complexity
O(n), where n is the number of elements in the input list, because we perform a constant amount of work for each element in the list (converting to a set and iterating over the range).

## Space Complexity
O(n), where n is the number of elements in the input list, because we store all elements in a set.

## Key Insight
The key insight is to use a set for efficient lookups, allowing us to check for the presence of each number in the range in constant time. This approach simplifies the problem and makes it easy to find the missing number in a single pass.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 100%) |
| 📅 Solved | 2025-01-30 |
| 💻 Language | Python |