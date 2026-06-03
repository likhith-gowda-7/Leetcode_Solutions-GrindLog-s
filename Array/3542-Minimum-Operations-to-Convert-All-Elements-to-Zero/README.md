# 3542. Minimum Operations to Convert All Elements to Zero


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/)


## 📝 Problem Description

You are given an array `nums` of size `n`, consisting of **non-negative** integers. Your task is to apply some (possibly zero) operations on the array so that **all** elements become 0.

In one operation, you can select a subarray `[i, j]` (where `0 <= i <= j < n`) and set all occurrences of the **minimum** **non-negative** integer in that subarray to 0.

Return the **minimum** number of operations required to make all elements in the array 0.

 

Example 1:**

**Input:** nums = [0,2]

**Output:** 1

**Explanation:**

	- Select the subarray `[1,1]` (which is `[2]`), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in `[0,0]`.

	- Thus, the minimum number of operations required is 1.

Example 2:**

**Input:** nums = [3,1,2,1]

**Output:** 3

**Explanation:**

	- Select subarray `[1,3]` (which is `[1,2,1]`), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in `[3,0,2,0]`.

	- Select subarray `[2,2]` (which is `[2]`), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in `[3,0,0,0]`.

	- Select subarray `[0,0]` (which is `[3]`), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in `[0,0,0,0]`.

	- Thus, the minimum number of operations required is 3.

Example 3:**

**Input:** nums = [1,2,1,2,1,2]

**Output:** 4

**Explanation:**

	- Select subarray `[0,5]` (which is `[1,2,1,2,1,2]`), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in `[0,2,0,2,0,2]`.

	- Select subarray `[1,1]` (which is `[2]`), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in `[0,0,0,2,0,2]`.

	- Select subarray `[3,3]` (which is `[2]`), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in `[0,0,0,0,0,2]`.

	- Select subarray `[5,5]` (which is `[2]`), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in `[0,0,0,0,0,0]`.

	- Thus, the minimum number of operations required is 4.

 

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `0 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The key insight behind this solution is to maintain a stack of non-decreasing numbers, where the top of the stack represents the smallest non-zero number that has not been set to zero yet. By continuously popping numbers from the stack that are greater than or equal to the current number, we can ensure that the stack always contains the smallest non-zero number that has not been set to zero.

**Approach**
1. Initialize a stack to store non-decreasing numbers and a counter `min_ops` to keep track of the minimum number of operations.
2. Iterate through the input array `nums`. For each number `num`, compare it with the top of the stack `stack[-1]`.
3. If the stack is not empty and the top of the stack is greater than or equal to `num`, pop the top of the stack if it is not equal to `num`. This ensures that the stack always contains the smallest non-zero number that has not been set to zero.
4. Push `num` onto the stack.
5. After iterating through the entire array, pop any remaining numbers from the stack and increment `min_ops` if the number is not zero.
6. Return `min_ops` as the minimum number of operations required.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we are iterating through the array once and performing constant-time operations for each element.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because in the worst case, we may need to store all elements of the array in the stack.

**Key Insight**
The key insight behind this solution is to maintain a stack of non-decreasing numbers, which allows us to efficiently keep track of the smallest non-zero number that has not been set to zero. By continuously popping numbers from the stack that are greater than or equal to the current number, we can ensure that the stack always contains the smallest non-zero number that has not been set to zero.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 200 ms (Beats 65.71%) |
| 💾 Memory | 30 MB (Beats 100%) |
| 📅 Solved | 2025-11-11 |
| 💻 Language | Python |