# 15. 3Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/3sum/)


## 📝 Problem Description

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:**

```

**Input:** nums = [-1,0,1,2,-1,-4]
**Output:** [[-1,-1,2],[-1,0,1]]
**Explanation:** 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

```

Example 2:**

```

**Input:** nums = [0,1,1]
**Output:** []
**Explanation:** The only possible triplet does not sum up to 0.

```

Example 3:**

```

**Input:** nums = [0,0,0]
**Output:** [[0,0,0]]
**Explanation:** The only possible triplet sums up to 0.

```

 

**Constraints:**

	- `3 <= nums.length <= 3000`

	- `-10^5 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

## Intuition
The solution works by first sorting the input array, which allows us to apply a two-pointer technique to find triplets that sum up to zero. By fixing one element and using two pointers to find the other two elements, we can efficiently search for valid triplets. The sorting step also helps us to skip duplicate triplets.

## Approach
1. Sort the input array in ascending order.
2. Iterate over the sorted array, fixing one element at a time.
3. For each fixed element, use two pointers (one starting from the next element and one from the end of the array) to find a pair of elements that sum up to the negation of the fixed element.
4. If the sum of the three elements is greater than zero, move the right pointer to the left to decrease the sum.
5. If the sum is less than zero, move the left pointer to the right to increase the sum.
6. If the sum is equal to zero, add the triplet to the result list and move both pointers.

## Time Complexity
The time complexity is O(n^2), where n is the length of the input array. This is because we have a nested loop structure, with the outer loop iterating over the array and the inner loop using the two-pointer technique.

## Space Complexity
The space complexity is O(n), where n is the length of the input array. This is because we need to store the result list, which can contain up to n/3 triplets in the worst case.

## Key Insight
The key insight behind this solution is the use of the two-pointer technique to efficiently search for valid triplets. By sorting the array and fixing one element at a time, we can reduce the problem to a simple two-pointer problem, which allows us to find all valid triplets in quadratic time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 627 ms (Beats 88.5%) |
| 💾 Memory | 18.2 MB (Beats 76.67%) |
| 📅 Solved | 2025-01-06 |
| 💻 Language | Python |