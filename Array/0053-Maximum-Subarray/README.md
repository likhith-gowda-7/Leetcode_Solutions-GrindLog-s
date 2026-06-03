# 53. Maximum Subarray


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-subarray/)


## 📝 Problem Description

Given an integer array `nums`, find the subarray with the largest sum, and return *its sum*.

 

Example 1:**

```

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6.

```

Example 2:**

```

**Input:** nums = [1]
**Output:** 1
**Explanation:** The subarray [1] has the largest sum 1.

```

Example 3:**

```

**Input:** nums = [5,4,-1,7,8]
**Output:** 23
**Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

 

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## 🧠 Solution Explanation

## Intuition
The solution works by iterating through the array and maintaining a running sum of the current subarray. It resets the running sum whenever it becomes negative, as a negative sum has no benefit in contributing to the maximum subarray sum. This approach ensures that all possible subarrays are considered, and the maximum sum is found.

## Approach
1. Initialize the answer (`ans`) with the first element of the array and the current sum (`curr`) to 0.
2. Iterate through the array, adding each element to the current sum (`curr`).
3. Update `curr` to be the maximum of its current value and the current element, effectively resetting `curr` if it becomes negative.
4. Update `ans` to be the maximum of its current value and `curr`.
5. Return `ans` as the maximum subarray sum.

## Time Complexity
The time complexity is O(n), where n is the number of elements in the array, as the solution involves a single pass through the array.

## Space Complexity
The space complexity is O(1), as the solution uses a constant amount of space to store the answer and the current sum, regardless of the size of the input array.

## Key Insight
The key insight behind this solution is the realization that a negative running sum has no benefit in contributing to the maximum subarray sum, so it can be safely reset to the current element. This allows the solution to efficiently consider all possible subarrays and find the maximum sum in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 31 ms (Beats 73.88%) |
| 💾 Memory | 31.3 MB (Beats 74.23%) |
| 📅 Solved | 2026-05-19 |
| 💻 Language | Python |