> 📌 **Cross-listed:** Primary location is [Array/0078-Subsets](../../Array/0078-Subsets). This problem also appears under: **Array**, **Backtracking**, **Bit Manipulation**

# 78. Subsets


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/subsets/)


## 📝 Problem Description

Given an integer array `nums` of **unique** elements, return *all possible* *subsets* *(the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

 

Example 1:**

```

**Input:** nums = [1,2,3]
**Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

```

Example 2:**

```

**Input:** nums = [0]
**Output:** [[],[0]]

```

 

**Constraints:**

	- `1 <= nums.length <= 10`

	- `-10 <= nums[i] <= 10`

	- All the numbers of `nums` are **unique**.

## 🧠 Solution Explanation

## Intuition
The solution uses a backtracking approach to generate all possible subsets of the given array. This approach works because it systematically explores all possible combinations of including or excluding each element from the subset. By recursively calling the backtrack function, we can efficiently generate all possible subsets.

## Approach
1. Initialize an empty result list `res` and an empty solution list `sol`.
2. Define a recursive backtrack function that takes an index `idx` as a parameter.
3. In the backtrack function, check if the current index `idx` is equal to the length of the input array `n`. If true, append a copy of the current solution `sol` to the result list `res`.
4. Recursively call the backtrack function with `idx + 1` to explore the case where the current element is not included in the subset.
5. Append the current element `nums[idx]` to the solution list `sol` and recursively call the backtrack function with `idx + 1` to explore the case where the current element is included in the subset.
6. After the recursive call, remove the last element from the solution list `sol` to undo the changes and backtrack.

## Time Complexity
The time complexity is O(2^n), where n is the length of the input array. This is because each element can be either included or excluded from the subset, resulting in 2^n possible combinations.

## Space Complexity
The space complexity is O(n), where n is the length of the input array. This is because the maximum depth of the recursion call stack is n, and we need to store the current solution list `sol` of size n.

## Key Insight
The key insight behind this solution is the use of backtracking to systematically explore all possible combinations of including or excluding each element from the subset. By using a recursive approach and undoing the changes after each recursive call, we can efficiently generate all possible subsets without duplicates.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 67.27%) |
| 📅 Solved | 2026-04-14 |
| 💻 Language | Python |