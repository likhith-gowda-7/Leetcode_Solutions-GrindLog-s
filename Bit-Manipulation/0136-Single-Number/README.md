> 📌 **Cross-listed:** Primary location is [Array/0136-Single-Number](../../Array/0136-Single-Number). This problem also appears under: **Array**, **Bit Manipulation**

# 136. Single Number


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/single-number/)


## 📝 Problem Description

Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:**

**Input:** nums = [2,2,1]

**Output:** 1

Example 2:**

**Input:** nums = [4,1,2,1,2]

**Output:** 4

Example 3:**

**Input:** nums = [1]

**Output:** 1

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

	- Each element in the array appears twice except for one element which appears only once.

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing the properties of bitwise XOR operation, which returns 1 if the two bits are different and 0 if they are the same. Since every element appears twice except for one, the XOR operation will cancel out the pairs and leave the single number. This approach takes advantage of the fact that XOR is commutative and associative.

## Approach
1. Initialize a variable `res` to 0, which will store the result of the XOR operation.
2. Iterate through each element `i` in the input array `nums`.
3. For each element, perform a bitwise XOR operation between `res` and `i`, and store the result back in `res`.
4. After iterating through all elements, `res` will hold the single number that appears only once.

## Time Complexity
The time complexity is O(n), where n is the number of elements in the input array, because we are iterating through the array once.

## Space Complexity
The space complexity is O(1), because we are using a constant amount of extra space to store the result, regardless of the size of the input array.

## Key Insight
The key insight is that the XOR operation has the property of `a ^ a = 0` and `a ^ 0 = a`, which allows us to cancel out the pairs and leave the single number, making this solution efficient and scalable.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 100%) |
| 📅 Solved | 2024-12-08 |
| 💻 Language | Python |