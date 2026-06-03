# 414. Third Maximum Number


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/third-maximum-number/)


## 📝 Problem Description

Given an integer array `nums`, return *the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number*.

 

Example 1:**

```

**Input:** nums = [3,2,1]
**Output:** 1
**Explanation:**
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

```

Example 2:**

```

**Input:** nums = [1,2]
**Output:** 2
**Explanation:**
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

```

Example 3:**

```

**Input:** nums = [2,2,3,1]
**Output:** 1
**Explanation:**
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-2^31 <= nums[i] <= 2^31 - 1`

 

**Follow up:** Can you find an `O(n)` solution?

## 🧠 Solution Explanation

## Intuition
This approach works by first removing duplicates from the input array, then sorting the unique numbers in ascending order. The third maximum number can be found by checking if there are at least three unique numbers, and if so, returning the third last number in the sorted list. If there are less than three unique numbers, the maximum number is returned instead.

## Approach
1. Convert the input list to a set to remove duplicates, then convert it back to a list.
2. Sort the list of unique numbers in ascending order.
3. Check if the length of the sorted list is less than 3.
4. If the length is less than 3, return the last number in the list (the maximum number).
5. If the length is 3 or more, return the third last number in the list (the third maximum number).

## Time Complexity
The time complexity is O(n log n) due to the sorting operation, where n is the number of unique elements in the input array. The set conversion and list indexing operations take linear time, but are dominated by the sorting operation.

## Space Complexity
The space complexity is O(n) because we are storing the unique elements from the input array in a set and then converting it back to a list. In the worst case, if all elements in the input array are unique, the space used will be proportional to the size of the input array.

## Key Insight
The key insight here is to remove duplicates before sorting, which simplifies the problem and allows us to find the third maximum number in a straightforward manner. By checking the length of the sorted list, we can handle cases where the third maximum number does not exist and return the maximum number instead.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.1 MB (Beats 99.98%) |
| 📅 Solved | 2025-01-31 |
| 💻 Language | Python |