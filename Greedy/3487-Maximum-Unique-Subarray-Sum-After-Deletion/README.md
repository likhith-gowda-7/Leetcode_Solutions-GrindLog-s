> 📌 **Cross-listed:** Primary location is [Array/3487-Maximum-Unique-Subarray-Sum-After-Deletion](../../Array/3487-Maximum-Unique-Subarray-Sum-After-Deletion). This problem also appears under: **Array**, **Hash Table**, **Greedy**

# 3487. Maximum Unique Subarray Sum After Deletion


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/)


## 📝 Problem Description

You are given an integer array `nums`.

You are allowed to delete any number of elements from `nums` without making it **empty**. After performing the deletions, select a subarray of `nums` such that:

	- All elements in the subarray are **unique**.

	- The sum of the elements in the subarray is **maximized**.

Return the **maximum sum** of such a subarray.

 

Example 1:**

**Input:** nums = [1,2,3,4,5]

**Output:** 15

**Explanation:**

Select the entire array without deleting any element to obtain the maximum sum.

Example 2:**

**Input:** nums = [1,1,0,1,1]

**Output:** 1

**Explanation:**

Delete the element `nums[0] == 1`, `nums[1] == 1`, `nums[2] == 0`, and `nums[3] == 1`. Select the entire array `[1]` to obtain the maximum sum.

Example 3:**

**Input:** nums = [1,2,-1,-2,1,0,-1]

**Output:** 3

**Explanation:**

Delete the elements `nums[2] == -1` and `nums[3] == -2`, and select the subarray `[2, 1]` from `[1, 2, 1, 0, -1]` to obtain the maximum sum.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a sliding window of unique numbers, where we keep adding numbers to the window as long as they are unique, and remove numbers from the window when they repeat. We keep track of the maximum sum of the window at any point.

**Approach**
1. First, we check if the maximum number in the array is non-positive. If it is, we return the maximum number as the maximum sum is then the maximum number itself.
2. We initialize an empty set `check` to store unique numbers and `curr_sum` to store the current sum of the window.
3. We iterate through the array. If a number is non-positive, we skip it.
4. If a number is already in the set `check`, we remove it from the set to ensure uniqueness.
5. We add the number to the set `check` and update `curr_sum` by adding the number.
6. We update `res` with the maximum of the current `res` and `curr_sum`.
7. Finally, we return `res` as the maximum sum.

**Time Complexity**
O(n), where n is the length of the array. We make a single pass through the array, and each operation (addition, removal, and lookup) in the set takes constant time.

**Space Complexity**
O(n), where n is the length of the array. In the worst case, we might need to store all numbers in the set `check`.

**Key Insight**
The key insight is to use a set to efficiently keep track of unique numbers in the window. By removing duplicates from the set, we can ensure that the window always contains unique numbers, which is a crucial property for finding the maximum sum.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-07-25 |
| 💻 Language | Python |