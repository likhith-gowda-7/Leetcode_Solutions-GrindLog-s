> 📌 **Cross-listed:** Primary location is [Array/0090-Subsets-II](../../Array/0090-Subsets-II). This problem also appears under: **Array**, **Backtracking**, **Bit Manipulation**

# 90. Subsets II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/subsets-ii/)


## 📝 Problem Description

Given an integer array `nums` that may contain duplicates, return *all possible* *subsets** (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

 

Example 1:**

```
**Input:** nums = [1,2,2]
**Output:** [[],[1],[1,2],[1,2,2],[2],[2,2]]

```
Example 2:**

```
**Input:** nums = [0]
**Output:** [[],[0]]

```

 

**Constraints:**

	- `1 <= nums.length <= 10`

	- `-10 <= nums[i] <= 10`

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing a backtracking approach to generate all possible subsets of the given array. To avoid duplicate subsets, the array is first sorted, and then a skipping mechanism is implemented to bypass duplicate elements. This ensures that each subset is unique and only appears once in the result.

## Approach
1. Sort the input array `nums` to group duplicate elements together.
2. Initialize an empty list `sol` to store the current subset and another list `res` to store all generated subsets.
3. Define a recursive function `backtrack` that takes an index `idx` as a parameter.
4. Within `backtrack`, if the index reaches the end of the array, append a copy of the current subset `sol` to the result list `res`.
5. Otherwise, add the current element to `sol`, recursively call `backtrack` with the next index, and then remove the last added element from `sol`.
6. To skip duplicate elements, increment the index `idx` until a different element is found or the end of the array is reached, and then recursively call `backtrack` with the updated index.

## Time Complexity
The time complexity is O(2^n * n), where n is the length of the input array. This is because in the worst case, we generate 2^n subsets (the power set), and for each subset, we perform a copy operation that takes O(n) time.

## Space Complexity
The space complexity is O(2^n * n), which is used to store the result list `res` containing all generated subsets. The recursion stack also uses O(n) space in the worst case, but this is dominated by the space required for the result list.

## Key Insight
The key insight here is the use of sorting and skipping duplicate elements to efficiently generate unique subsets. By sorting the array and skipping duplicates, we avoid generating duplicate subsets and ensure that the result only contains unique subsets.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-11-27 |
| 💻 Language | Python |