# 238. Product of Array Except Self


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)


## 📝 Problem Description

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

 

Example 1:**

```
**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]

```
Example 2:**

```
**Input:** nums = [-1,1,0,-3,3]
**Output:** [0,0,9,0,0]

```

 

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `-30 <= nums[i] <= 30`

	- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

 

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

## 🧠 Solution Explanation

### Intuition
The solution works by utilizing the concept of prefix and postfix products to calculate the product of all elements except the current one. This approach allows us to avoid using division and achieve a time complexity of O(n). By calculating the prefix and postfix products separately, we can then combine them to obtain the final result.

### Approach
1. Initialize an array `res` with the same length as the input array `nums`, filled with ones.
2. Calculate the prefix product for each element in `nums` and store it in the corresponding index in `res`.
3. Calculate the postfix product for each element in `nums` in reverse order and multiply it with the corresponding prefix product stored in `res`.
4. Return the `res` array, which now contains the product of all elements except the current one for each index.

### Time Complexity
The time complexity is O(n), where n is the length of the input array `nums`. This is because we are making two separate passes through the array: one for calculating the prefix products and another for calculating the postfix products.

### Space Complexity
The space complexity is O(1), excluding the output array. This is because we are only using a constant amount of space to store the prefix and postfix products, and the output array is not included in the space complexity calculation.

### Key Insight
The key insight behind this solution is the realization that the product of all elements except the current one can be calculated by multiplying the prefix product (product of all elements before the current one) with the postfix product (product of all elements after the current one). This allows us to avoid using division and achieve an efficient solution with a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 17 ms (Beats 82.45%) |
| 💾 Memory | 22.8 MB (Beats 100%) |
| 📅 Solved | 2024-12-13 |
| 💻 Language | Python |