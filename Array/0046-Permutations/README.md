# 46. Permutations


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/permutations/)


## 📝 Problem Description

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

 

Example 1:**

```
**Input:** nums = [1,2,3]
**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```
Example 2:**

```
**Input:** nums = [0,1]
**Output:** [[0,1],[1,0]]

```
Example 3:**

```
**Input:** nums = [1]
**Output:** [[1]]

```

 

**Constraints:**

	- `1 <= nums.length <= 6`

	- `-10 <= nums[i] <= 10`

	- All the integers of `nums` are **unique**.

## 🧠 Solution Explanation

## Intuition
The solution uses a backtracking approach to generate all permutations of the input array. This works because backtracking allows us to explore all possible branches of the permutation tree, where each branch represents a different permutation. By recursively adding and removing elements from the current permutation, we can efficiently generate all possible permutations.

## Approach
1. Initialize an empty result list `res` to store the generated permutations and an empty solution list `sol` to store the current permutation being built.
2. Create a `used` array to keep track of which elements have been used in the current permutation.
3. Define a recursive `backtrack` function that checks if the current permutation is complete (i.e., its length is equal to the length of the input array).
4. If the permutation is complete, append a copy of it to the result list.
5. Otherwise, iterate over the input array and for each unused element, mark it as used, add it to the current permutation, and recursively call the `backtrack` function.
6. After the recursive call returns, undo the changes by removing the last added element from the current permutation and marking it as unused.

## Time Complexity
The time complexity is O(N!), where N is the length of the input array. This is because there are N! possible permutations, and the algorithm generates each one exactly once.

## Space Complexity
The space complexity is O(N), where N is the length of the input array. This is because the maximum depth of the recursion tree is N, and the space used by the `used` array and the current permutation is proportional to N.

## Key Insight
The key insight behind this solution is the use of backtracking to efficiently explore the permutation tree. By recursively adding and removing elements from the current permutation, we can generate all possible permutations without having to explicitly store them all in memory at once. This approach allows us to solve the problem using a relatively small amount of extra memory.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-08-01 |
| 💻 Language | Python |