# 47. Permutations II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/permutations-ii/)


## 📝 Problem Description

Given a collection of numbers, `nums`, that might contain duplicates, return *all possible unique permutations **in any order**.*

 

Example 1:**

```

**Input:** nums = [1,1,2]
**Output:**
[[1,1,2],
 [1,2,1],
 [2,1,1]]

```

Example 2:**

```

**Input:** nums = [1,2,3]
**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```

 

**Constraints:**

	- `1 <= nums.length <= 8`

	- `-10 <= nums[i] <= 10`

## 🧠 Solution Explanation

## Intuition
This solution works by utilizing a backtracking approach to generate all unique permutations of the input array. The key to handling duplicates lies in sorting the array and skipping over identical elements that have not been used yet. This ensures that each permutation is unique and avoids unnecessary computation.

## Approach
1. Sort the input array `nums` to group identical elements together.
2. Initialize an empty result list `res`, a temporary solution list `sol`, and a boolean array `used` to track used elements.
3. Define a recursive `backtrack` function that:
   - Checks if the length of `sol` is equal to the length of `nums`, indicating a complete permutation.
   - Iterates over `nums`, skipping over identical elements that have not been used yet.
   - Marks the current element as used, adds it to `sol`, and recursively calls `backtrack`.
   - Backtracks by removing the last element from `sol` and marking it as unused.
4. Call the `backtrack` function and return the result list `res`.

## Time Complexity
The time complexity is O(N! / (k1! * k2! * ... * km!)), where N is the length of `nums` and k1, k2, ..., km are the frequencies of each distinct element. This is because there are N! permutations in total, but many of them are duplicates due to the presence of identical elements.

## Space Complexity
The space complexity is O(N), where N is the length of `nums`. This is because the maximum recursion depth is N, and we need to store the `used` array and the temporary solution list `sol`.

## Key Insight
The key insight here is to sort the input array and skip over identical elements that have not been used yet, which allows us to efficiently generate all unique permutations while avoiding duplicates. This approach takes advantage of the fact that identical elements are grouped together after sorting, making it easy to identify and skip over duplicates.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 40.12%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-07-31 |
| 💻 Language | Python |