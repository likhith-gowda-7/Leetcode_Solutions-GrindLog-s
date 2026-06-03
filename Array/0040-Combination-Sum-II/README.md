# 40. Combination Sum II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/combination-sum-ii/)


## 📝 Problem Description

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

 

Example 1:**

```

**Input:** candidates = [10,1,2,7,6,1,5], target = 8
**Output:** 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

```

Example 2:**

```

**Input:** candidates = [2,5,2,1,2], target = 5
**Output:** 
[
[1,2,2],
[5]
]

```

 

**Constraints:**

	- `1 <= candidates.length <= 100`

	- `1 <= candidates[i] <= 50`

	- `1 <= target <= 30`

## 🧠 Solution Explanation

### Intuition
This solution works by utilizing a backtracking approach to find all unique combinations of numbers that sum up to the target. The key idea is to sort the input array and then use a recursive function to explore all possible combinations. By skipping duplicate numbers, we ensure that the solution set does not contain duplicate combinations.

### Approach
1. Sort the input array `nums` in ascending order.
2. Define a recursive function `bt` that takes two parameters: `idx` (the current index) and `curr_sum` (the current sum of the combination).
3. If `curr_sum` equals the target, append the current combination to the result list `res`.
4. If `idx` reaches the end of the array, return without adding the current combination to `res`.
5. Include the current number in the combination by appending it to `sol` and recursively calling `bt` with the updated `curr_sum` and `idx+1`.
6. Skip the current number by recursively calling `bt` with the same `curr_sum` and `idx+1`, while also skipping any duplicate numbers.

### Time Complexity
The time complexity is O(2^n) due to the recursive nature of the backtracking approach, where n is the length of the input array. However, the actual time complexity is reduced by pruning branches that exceed the target sum and skipping duplicate numbers.

### Space Complexity
The space complexity is O(n) due to the recursive call stack and the storage of the current combination `sol`. The maximum depth of the recursion tree is n, which occurs when the target sum is equal to the sum of all numbers in the input array.

### Key Insight
The key insight behind this solution is the use of sorting and skipping duplicate numbers to ensure that the solution set does not contain duplicate combinations. By sorting the input array, we can easily skip duplicate numbers and avoid exploring redundant branches in the recursion tree.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 87.07%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-07-26 |
| 💻 Language | Python |