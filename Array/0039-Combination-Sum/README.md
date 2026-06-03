# 39. Combination Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/combination-sum/)


## 📝 Problem Description

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of *`candidates`* where the chosen numbers sum to *`target`*.* You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

 

Example 1:**

```

**Input:** candidates = [2,3,6,7], target = 7
**Output:** [[2,2,3],[7]]
**Explanation:**
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

```

Example 2:**

```

**Input:** candidates = [2,3,5], target = 8
**Output:** [[2,2,2,2],[2,3,3],[3,5]]

```

Example 3:**

```

**Input:** candidates = [2], target = 1
**Output:** []

```

 

**Constraints:**

	- `1 <= candidates.length <= 30`

	- `2 <= candidates[i] <= 40`

	- All elements of `candidates` are **distinct**.

	- `1 <= target <= 40`

## 🧠 Solution Explanation

## Intuition
The Combination Sum problem can be solved using a backtracking approach, where we recursively try to include or exclude each candidate number to reach the target sum. This approach works because we can use each number an unlimited number of times, allowing us to explore all possible combinations. By using backtracking, we can efficiently explore the solution space without having to explicitly generate all possible combinations.

## Approach
1. Initialize an empty result list `res` to store the valid combinations and an empty solution list `sol` to store the current combination being explored.
2. Define a recursive `backtrack` function that takes the current index `idx` and the current sum `curr_sum` as parameters.
3. Within the `backtrack` function, check if the current sum equals the target sum, and if so, append a copy of the current solution to the result list.
4. If the current index exceeds the length of the candidates list or the current sum exceeds the target sum, return immediately to prune the search tree.
5. Recursively call the `backtrack` function, first including the current candidate number and then excluding it by incrementing the index.

## Time Complexity
The time complexity is O(N^(T/M) + 1), where N is the length of the candidates list, T is the target sum, and M is the minimum value in the candidates list. This is because in the worst case, we may need to explore all possible combinations, and the maximum depth of the recursion tree is proportional to the target sum.

## Space Complexity
The space complexity is O(T/M), which is the maximum depth of the recursion tree. This is because we need to store the current solution being explored, which can grow up to the target sum in the worst case.

## Key Insight
The key insight behind this solution is the use of backtracking to efficiently explore the solution space, allowing us to avoid explicitly generating all possible combinations and instead focus on finding the valid combinations that sum up to the target. By using a recursive approach and pruning the search tree when the current sum exceeds the target sum, we can significantly reduce the number of combinations that need to be explored.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 13 ms (Beats 26.22%) |
| 💾 Memory | 17 MB (Beats 100%) |
| 📅 Solved | 2025-12-19 |
| 💻 Language | Python |