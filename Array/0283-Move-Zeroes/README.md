# 283. Move Zeroes


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/move-zeroes/)


## 📝 Problem Description

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

 

Example 1:**

```
**Input:** nums = [0,1,0,3,12]
**Output:** [1,3,12,0,0]

```
Example 2:**

```
**Input:** nums = [0]
**Output:** [0]

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-2^31 <= nums[i] <= 2^31 - 1`

 

**Follow up:** Could you minimize the total number of operations done?

## 🧠 Solution Explanation

## Intuition
This approach works by maintaining two pointers, one for reading the array and one for writing non-zero elements. By doing so, we can efficiently move all non-zero elements to the front of the array while preserving their relative order. The zero elements will then be filled in at the end of the array.

## Approach
1. Initialize a pointer `i` to keep track of the position where the next non-zero element should be written.
2. Iterate through the array with pointer `j`, checking each element.
3. If a non-zero element is found, write it to the current position `i` and increment `i`.
4. After iterating through the entire array, fill in the remaining positions (from `i` to the end) with zeros.

## Time Complexity
The time complexity is O(n), where n is the length of the input array. This is because we make two passes through the array: one to move non-zero elements to the front and another to fill in the zeros at the end.

## Space Complexity
The space complexity is O(1), as we only use a constant amount of space to store the pointers `i` and `j`, regardless of the size of the input array.

## Key Insight
The key insight here is the use of two pointers to separate the concerns of reading and writing, allowing us to efficiently move non-zero elements to the front of the array while preserving their relative order, and then filling in the zeros at the end. This approach minimizes the total number of operations done, as required by the follow-up question.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 79.16%) |
| 💾 Memory | 13.6 MB (Beats 47.78%) |
| 📅 Solved | 2024-12-01 |
| 💻 Language | Python |