> 📌 **Cross-listed:** Primary location is [Array/3379-Transformed-Array](../../Array/3379-Transformed-Array). This problem also appears under: **Array**, **Simulation**

# 3379. Transformed Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/transformed-array/)


## 📝 Problem Description

You are given an integer array `nums` that represents a circular array. Your task is to create a new array `result` of the **same** size, following these rules:

For each index `i` (where `0 <= i < nums.length`), perform the following **independent** actions:

	- If `nums[i] > 0`: Start at index `i` and move `nums[i]` steps to the **right** in the circular array. Set `result[i]` to the value at the index where you land.

	- If `nums[i] < 0`: Start at index `i` and move `abs(nums[i])` steps to the **left** in the circular array. Set `result[i]` to the value at the index where you land.

	- If `nums[i] == 0`: Set `result[i]` to `nums[i]`.

Return the new array `result`.

**Note:** Since `nums` is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.

 

Example 1:**

**Input:** nums = [3,-2,1,1]

**Output:** [1,1,1,3]

**Explanation:**

	- For `nums[0]` that is equal to 3, If we move 3 steps to right, we reach `nums[3]`. So `result[0]` should be 1.

	- For `nums[1]` that is equal to -2, If we move 2 steps to left, we reach `nums[3]`. So `result[1]` should be 1.

	- For `nums[2]` that is equal to 1, If we move 1 step to right, we reach `nums[3]`. So `result[2]` should be 1.

	- For `nums[3]` that is equal to 1, If we move 1 step to right, we reach `nums[0]`. So `result[3]` should be 3.

Example 2:**

**Input:** nums = [-1,4,-1]

**Output:** [-1,-1,4]

**Explanation:**

	- For `nums[0]` that is equal to -1, If we move 1 step to left, we reach `nums[2]`. So `result[0]` should be -1.

	- For `nums[1]` that is equal to 4, If we move 4 steps to right, we reach `nums[2]`. So `result[1]` should be -1.

	- For `nums[2]` that is equal to -1, If we move 1 step to left, we reach `nums[1]`. So `result[2]` should be 4.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by directly calculating the new index for each element in the array based on the given rules. By using the modulo operator, we can handle the circular nature of the array.

**Approach**
1. For each index `i` in the array, calculate the new index by adding `nums[i]` to `i` and taking the result modulo the length of the array.
2. This effectively moves the index `i` to the right by `nums[i]` steps if `nums[i]` is positive, or to the left by `abs(nums[i])` steps if `nums[i]` is negative.
3. If `nums[i]` is zero, the index remains unchanged.
4. The resulting new index is used to access the corresponding value in the original array.

**Time Complexity**
O(n), where n is the length of the array. This is because we are iterating over each element in the array once.

**Space Complexity**
O(1), excluding the space required for the output array. We are only using a constant amount of space to store the current index and the length of the array.

**Key Insight**
The key insight is that we can directly calculate the new index for each element by using the modulo operator, which allows us to handle the circular nature of the array in a single step. This simplifies the solution and makes it more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 59 ms (Beats 77.27%) |
| 💾 Memory | 19.3 MB (Beats 50.62%) |
| 📅 Solved | 2026-02-05 |
| 💻 Language | Python |