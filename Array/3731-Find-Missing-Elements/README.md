# 3731. Find Missing Elements


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-missing-elements/)


## 📝 Problem Description

You are given an integer array `nums` consisting of **unique** integers.

Originally, `nums` contained **every integer** within a certain range. However, some integers might have gone **missing** from the array.

The **smallest** and **largest** integers of the original range are still present in `nums`.

Return a **sorted** list of all the missing integers in this range. If no integers are missing, return an **empty** list.

 

Example 1:**

**Input:** nums = [1,4,2,5]

**Output:** [3]

**Explanation:**

The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. Among these, only 3 is missing.

Example 2:**

**Input:** nums = [7,8,6,9]

**Output:** []

**Explanation:**

The smallest integer is 6 and the largest is 9, so the full range is `[6,7,8,9]`. All integers are already present, so no integer is missing.

Example 3:**

**Input:** nums = [5,1]

**Output:** [2,3,4]

**Explanation:**

The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. The missing integers are 2, 3, and 4.

 

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating through the sorted array and checking for missing integers. It keeps track of the current expected integer and compares it with the actual integer in the array. If they don't match, it means the current integer is missing, so it's added to the result list.

**Approach**
1. First, sort the input array `nums` in ascending order.
2. Initialize an empty list `res` to store the missing integers.
3. Initialize `i` to 0, which will be used as the index to traverse the sorted array.
4. Initialize `curr` to the first element of the sorted array, which is the smallest integer.
5. Iterate through the sorted array using a while loop. In each iteration:
   - Check if `curr` is not equal to the `i-th` element of the sorted array `nums`.
   - If they don't match, it means `curr` is missing, so add it to the result list `res`.
   - Otherwise, increment `i` to move to the next element in the array.
   - Increment `curr` by 1 to move to the next expected integer.
6. Return the result list `res` containing the missing integers.

**Time Complexity**
The time complexity of this solution is O(n log n) due to the sorting operation, where n is the length of the input array `nums`. The subsequent while loop runs in O(n) time, but it's dominated by the sorting operation.

**Space Complexity**
The space complexity of this solution is O(n) for storing the result list `res` in the worst case, where all integers are missing.

**Key Insight**
The key insight here is that we can take advantage of the fact that the input array `nums` contains all unique integers within a certain range. By sorting the array, we can easily identify the missing integers by comparing the expected integer with the actual integer in the array. This approach allows us to find the missing integers in a single pass through the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.1 MB (Beats 86.89%) |
| 📅 Solved | 2026-08-04 |
| 💻 Language | Python |