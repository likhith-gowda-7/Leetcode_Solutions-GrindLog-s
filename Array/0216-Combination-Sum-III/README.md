# 216. Combination Sum III


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/combination-sum-iii/)


## 📝 Problem Description

Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:

	- Only numbers `1` through `9` are used.

	- Each number is used **at most once**.

Return *a list of all possible valid combinations*. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:**

```

**Input:** k = 3, n = 7
**Output:** [[1,2,4]]
**Explanation:**
1 + 2 + 4 = 7
There are no other valid combinations.
```

Example 2:**

```

**Input:** k = 3, n = 9
**Output:** [[1,2,6],[1,3,5],[2,3,4]]
**Explanation:**
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

```

Example 3:**

```

**Input:** k = 4, n = 1
**Output:** []
**Explanation:** There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

```

 

**Constraints:**

	- `2 <= k <= 9`

	- `1 <= n <= 60`

## 🧠 Solution Explanation

## Intuition
The problem can be solved using a backtracking approach, where we recursively try to add numbers from 1 to 9 to our current combination, ensuring that the sum does not exceed `n` and that we do not use more than `k` numbers. This approach works because it allows us to systematically explore all possible combinations of numbers that sum up to `n`. By using backtracking, we can efficiently prune branches that will not lead to a valid solution.

## Approach
1. Define a recursive function `backtrack` that takes two parameters: `start` (the starting number for the current iteration) and `curr_sum` (the current sum of the numbers in the combination).
2. In the `backtrack` function, check if the current combination has `k` numbers and if its sum equals `n`. If so, add the combination to the result list.
3. If the current combination has more than `k` numbers, return immediately without exploring further branches.
4. Iterate over the numbers from `start` to 9, and for each number, check if adding it to the current sum would exceed `n`. If so, return immediately without exploring further branches.
5. Add the current number to the combination, recursively call `backtrack` with the updated combination and sum, and then remove the number from the combination (backtracking).

## Time Complexity
The time complexity is O(9^k), where k is the number of elements in the combination. This is because in the worst case, we might need to explore all possible combinations of k numbers from 1 to 9.

## Space Complexity
The space complexity is O(k), where k is the number of elements in the combination. This is because we need to store the current combination, which can have up to k elements.

## Key Insight
The key insight in this solution is the use of backtracking to efficiently explore all possible combinations of numbers that sum up to `n`, while ensuring that we do not exceed `k` numbers in each combination. By pruning branches that will not lead to a valid solution, we can significantly reduce the search space and improve the performance of the algorithm.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-07-25 |
| 💻 Language | Python |