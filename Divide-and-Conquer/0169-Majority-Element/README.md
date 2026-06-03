> 📌 **Cross-listed:** Primary location is [Array/0169-Majority-Element](../../Array/0169-Majority-Element). This problem also appears under: **Array**, **Hash Table**, **Divide and Conquer**, **Sorting**, **Counting**

# 169. Majority Element


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/majority-element/)


## 📝 Problem Description

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `&lfloor;n / 2&rfloor;` times. You may assume that the majority element always exists in the array.

 

Example 1:**

```
**Input:** nums = [3,2,3]
**Output:** 3

```
Example 2:**

```
**Input:** nums = [2,2,1,1,1,2,2]
**Output:** 2

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5 * 10^4`

	- `-10^9 <= nums[i] <= 10^9`

	- The input is generated such that a majority element will exist in the array.

 

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## 🧠 Solution Explanation

## Intuition
The solution works by first sorting the input array, which groups identical elements together, making it easier to find the majority element. The majority element is the one that appears more than half of the array's length. By iterating through the sorted array, we can keep track of the current element's count and update the majority element if a higher count is found.

## Approach
1. Sort the input array `nums` in ascending order.
2. Initialize variables to keep track of the current element's count `curr`, the maximum count `mc`, and the majority element `ele`.
3. Iterate through the sorted array, starting from the second element (index 1).
4. If the current element is the same as the previous one, increment the current count `curr`.
5. If the current element is different from the previous one, reset the current count `curr` to 1.
6. If the current count `curr` is greater than the maximum count `mc`, update the maximum count `mc` and the majority element `ele`.
7. Return the majority element `ele` after iterating through the entire array.

## Time Complexity
The time complexity is O(n log n) due to the sorting operation, where n is the length of the input array. The subsequent iteration through the array takes O(n) time, but it is dominated by the sorting operation.

## Space Complexity
The space complexity is O(n) because the sorting operation in Python creates a new sorted list, which requires additional space proportional to the input size.

## Key Insight
The key insight is that sorting the array allows us to easily identify the majority element by keeping track of the current element's count and updating the maximum count as we iterate through the array. However, this solution does not meet the follow-up requirement of O(1) space complexity, and there are more efficient algorithms available, such as the Boyer-Moore Majority Vote algorithm, which can solve the problem in linear time and constant space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 100%) |
| 📅 Solved | 2025-01-05 |
| 💻 Language | Python |